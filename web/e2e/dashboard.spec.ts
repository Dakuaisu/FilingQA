import { expect, test } from "@playwright/test";

test("the dashboard shows the gate failing, with a reason on every row", async ({ page }) => {
  await page.goto("/dashboard");
  await expect(page.getByTestId("gate-status")).toContainText("The CI eval gate fails.");
  await expect(page.getByTestId("gate-status")).toContainText("No gated run exists (F-59).");
  await expect(page.getByTestId("gate-status")).not.toContainText(/development runs/i);
  const rows = page.getByTestId("gate-row");
  await expect(rows).toHaveCount(21);
  await expect(page.getByTestId("gate-table")).not.toContainText("PASS");
  await expect(page.getByTestId("gate-table")).toContainText("pending: judge answer correctness (F-105)");
  const later = page.getByTestId("pending-with-run");
  await expect(later).toContainText(/historical/i);
  await expect(later).toContainText("cost per query (needs a priced run, F-134)");
  await expect(later.locator("li")).toHaveCount(4);
});

test("historical candidate retrieval is separate from the CI gate", async ({ page }) => {
  await page.goto("/dashboard");
  const cur = page.getByTestId("retrieval-current");
  await expect(cur.getByRole("heading")).toHaveText(/historical candidate retrieval/i);
  await expect(cur).toContainText("Retrieval run 5b3c3ac13e5e, Config 3 (PRD 11.6)");
  await expect(cur).toContainText("unreviewed candidates");
  await expect(page.getByTestId("retrieval-aggregate")).toContainText("0.537");
  await expect(page.getByTestId("retrieval-aggregate")).toContainText("0.82");
  await expect(page.getByTestId("retrieval-xbrl_auto")).toContainText("0.375");
  await expect(page.getByTestId("retrieval-xbrl_auto")).toContainText("misses");
  await expect(page.getByTestId("retrieval-llm_seeded")).toContainText("F-110");
});

test("historical runs are listed without access-channel text, tooltips, or scores", async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 900 });
  await page.goto("/dashboard");
  await expect(page.getByRole("main")).not.toContainText(/claude_cli|anthropic_api|api key|development run|not a result/i);
  const history = page.getByTestId("historical-runs");
  await expect(history.getByRole("heading")).toHaveText(/historical evaluation runs/i);
  await expect(history).toContainText("a4e39a65c2c8");
  await expect(history).not.toContainText(/\b\d\.\d{2,}/);
  await expect(history.locator("[title]")).toHaveCount(0);
  await expect(page.getByTestId("owner-blocked").locator("tr")).toHaveCount(9);
  expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBe(375);
});
