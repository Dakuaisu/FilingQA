import Link from "next/link";

import { AnswerView } from "@/components/answer-view";
import { AskForm } from "@/components/ask-form";
import { query } from "@/lib/api";

// A live answer takes up to about a minute (router, retrieval, generation, gate); hosts that
// cap server function time (Vercel) need the allowance.
export const maxDuration = 120;

const ERROR_TEXT: Record<number, string> = {
  400: "The request was not understood.",
  422: "The question is too long for the retriever. Shorten it and ask again.",
  503: "The answering service is unavailable right now.",
};

export default async function AnswerPage({ searchParams }: { searchParams: Promise<{ q?: string | string[] }> }) {
  const raw = (await searchParams).q;
  const q = (Array.isArray(raw) ? raw[0] : raw)?.trim() ?? "";
  if (!q) {
    return (
      <p>
        No question given. <Link href="/">Ask one.</Link>
      </p>
    );
  }
  const r = await query(q);
  return (
    <div className="space-y-6">
      <AskForm defaultValue={q} />
      <h1 className="text-lg font-medium" data-testid="question">
        {q}
      </h1>
      {r.ok ? (
        <>
          <AnswerView
            data={{
              verdict: r.body.verdict,
              confidence: r.body.confidence,
              verification_pending: r.body.verification_pending,
              abstain_reason: r.body.abstain_reason,
              nearest_evidence: r.body.nearest_evidence,
              claims: r.body.claims,
              citations: r.body.citations,
            }}
          />
          <div className="space-y-1 text-xs text-muted-foreground">
            {r.body.model_served && (
              <p data-testid="generator-model">
                Generator model: <code>{r.body.model_served}</code> · No fixed temperature
              </p>
            )}
            <p data-testid="latency-cost">
              {(r.body.metadata.latency_ms / 1000).toFixed(1)} s ·{" "}
              {r.body.metadata.cost_usd === null
                ? "No per-query price available"
                : `$${r.body.metadata.cost_usd.toFixed(4)}`} · intent {r.body.metadata.intent ?? "?"} ·{" "}
              {r.body.metadata.chunks_used} of {r.body.metadata.chunks_retrieved} retrieved chunks used
            </p>
          </div>
        </>
      ) : (
        <div role="alert" data-testid="error" className="rounded-md border border-red-300 bg-red-50 p-4 text-sm text-red-900">
          <p className="font-medium">{ERROR_TEXT[r.status] ?? `The request failed (${r.status}).`}</p>
          <p className="mt-1 text-xs text-red-800">{r.detail}</p>
        </div>
      )}
    </div>
  );
}
