FROM pgvector/pgvector:pg18

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-venv ca-certificates curl \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --uid 1000 space \
    && python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:/usr/lib/postgresql/18/bin:${PATH}" \
    PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
RUN pip install --upgrade pip \
    && pip install --no-deps --index-url https://download.pytorch.org/whl/cpu 'torch==2.14.1+cpu'

WORKDIR /app
COPY pyproject.toml ./
COPY api ./api
RUN pip install .
COPY eval ./eval
COPY scripts ./scripts
COPY infra ./infra
COPY deploy/hf/entrypoint.sh ./deploy/hf/entrypoint.sh
RUN chown -R 1000:1000 /app

USER 1000
ENV HOME=/home/space HF_HOME=/home/space/.cache/huggingface \
    DATA_DIR=/home/space/data CUDA_VISIBLE_DEVICES="" TOKENIZERS_PARALLELISM=false
EXPOSE 7860
ENTRYPOINT ["sh", "/app/deploy/hf/entrypoint.sh"]
