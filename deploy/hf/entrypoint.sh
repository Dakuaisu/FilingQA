#!/bin/sh
set -eu
umask 077

export FILINGQA_GENERATION_BACKEND=anthropic_api
export FILINGQA_TIER_SMALL=claude-haiku-5-5
export FILINGQA_TIER_LARGE=claude-haiku-5-5
export FILINGQA_PROSE_CHECK=nli
export CUDA_VISIBLE_DEVICES=""
export PGDATA="$HOME/postgres" PGHOST="$HOME/pgsocket" PGUSER=filingqa PGDATABASE=filingqa
export DATABASE_URL="host=$PGHOST port=5432 user=$PGUSER dbname=$PGDATABASE"
mkdir -p "$PGHOST" "$DATA_DIR"

set -- $(python -c 'import yaml; s=yaml.safe_load(open("api/corpus_snapshot_rebuild.yaml"))["snapshot"]; print(s["hosted"], s["archive"], s["sha256"], s["bytes"])')
hosted=$1 archive=$2 expected_sha=$3 expected_bytes=$4
case "$hosted" in
  https://github.com/*/*/releases/tag/*) ;;
  *) printf '%s\n' 'Invalid hosted snapshot release URL' >&2; exit 1 ;;
esac
case "$archive" in
  *[!A-Za-z0-9._-]*|'') printf '%s\n' 'Invalid snapshot archive name' >&2; exit 1 ;;
esac
url="${hosted%/tag/*}/download/${hosted##*/}/$archive"
snapshot="$HOME/$archive"
curl --fail --location --silent --show-error --retry 2 --output "$snapshot" "$url"
actual_sha=$(sha256sum "$snapshot" | cut -d ' ' -f 1)
actual_bytes=$(wc -c < "$snapshot" | tr -d ' ')
if [ "$actual_sha" != "$expected_sha" ] || [ "$actual_bytes" != "$expected_bytes" ]; then
  printf '%s\n' 'Snapshot digest or size mismatch; refusing to restore' >&2
  exit 1
fi
printf 'Snapshot verified: %s bytes sha256 %s\n' "$actual_bytes" "$actual_sha"

initdb -D "$PGDATA" -U "$PGUSER" --auth=trust --no-instructions > /dev/null
pg_ctl -D "$PGDATA" -l "$HOME/postgres.log" -o "-k $PGHOST -h '' -p 5432" -w start > /dev/null
cleanup() { pg_ctl -D "$PGDATA" -m fast -w stop > /dev/null || true; }
trap cleanup EXIT INT TERM
createdb "$PGDATABASE"
python -m api.db
pg_restore --no-owner --no-acl --data-only --single-transaction --disable-triggers \
  -d "$PGDATABASE" "$snapshot"
psql -v ON_ERROR_STOP=1 -c 'REINDEX INDEX chunks_hnsw' -c 'ANALYZE'
python -m scripts.verify_freeze --snapshot
printf '%s\n' 'Snapshot restored and verified; starting API on port 7860'
uvicorn api.server:app --host 0.0.0.0 --port 7860 &
child=$!
wait "$child"
