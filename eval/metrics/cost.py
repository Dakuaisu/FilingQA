"""cost_per_query (F-134; TRADEOFFS). Pure.

Per item: every model call made to answer it (router and generator; the judge is
eval cost and excluded; the local NLI model and reranker cost zero), each call's
input, output, cache-read and cache-creation tokens priced from eval/pricing.yaml.
cost_per_query is the mean over items. An unpriced backend has no per-query price;
a model without a price, or a call whose tokens were
not recorded, makes the cost pending, never a guess.
"""

from __future__ import annotations

KINDS = (("input_tokens", "input"), ("output_tokens", "output"),
         ("cache_read_tokens", "cache_read"), ("cache_creation_tokens", "cache_write"))  # fmt: skip
UNPRICED_NA = "cost n/a (no per-query price)"


def calls(r: dict) -> list[tuple[str | None, dict | None]]:
    """(model served, usage) per model call made for the item."""
    out = []
    router = r.get("router")
    if router is not None:
        out.append((router.get("model_served"), router.get("usage")))
    if r.get("model_served") is not None or r.get("usage") is not None:
        out.append((r.get("model_served"), r.get("usage")))
    return out


def tokens(results: list[dict]) -> dict:
    total = {k: 0 for k, _ in KINDS}
    for r in results:
        for _, usage in calls(r):
            for k, _ in KINDS:
                total[k] += (usage or {}).get(k) or 0
    return total


def call_cost(
    model: str | None, usage: dict | None, prices: dict
) -> tuple[float | None, str | None]:
    if usage is None:
        return None, "pending: call tokens not recorded"
    price = prices.get(model or "")
    if price is None:
        return None, f"pending: no price for {model}"
    total = 0.0
    for k, p in KINDS:
        n = usage.get(k) or 0
        if n and price.get(p) is None:
            return None, f"pending: no {p} price for {model}"
        total += n * (price.get(p) or 0.0) / 1e6
    return total, None


def cost_per_query(results: list[dict], prices: dict, unpriced_backend: bool):
    """Mean USD per item, or the reason it cannot be computed."""
    if unpriced_backend:
        return UNPRICED_NA
    if not results:
        return None
    per_item = []
    for r in results:
        item = 0.0
        for model, usage in calls(r):
            c, why = call_cost(model, usage, prices)
            if why:
                return why
            item += c
        per_item.append(item)
    return sum(per_item) / len(per_item)
