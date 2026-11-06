# Guided output examples

These examples were written by the implementing agent using the skill instructions and fixtures. They are not blind evaluations, Copilot/Claude executions, or results from a model evaluation suite. JavaScript results cited below were observed in the named local check; no browser was used.

## Review / standard — regression

Summary: confirmed regression in checkout calculation. Read-only review limited to the function and supplied contract.

Context: pure JavaScript; the caller supplies `discountPercent=0` for purchases without a promotion. The contract is confirmed by the fixture, not a real application. Infrastructure and other consumers are unknown.

**F-001 — Confirmed — High — high confidence: zero receives the default discount.** Location: `tests/fixtures/regression/after.mjs`, line 2, `total`. Replacing `??` with `||` substitutes 10 for zero. The `node tests/check-fixtures.mjs` check observed `total(100, 0)=100` in the base and `90` in the candidate. Since this value is used to produce the order amount, a purchase without a promotion receives an unintended discount. Minimal action: preserve the base's nullish check. Explicitly checking null/undefined would add code without demonstrated benefit for this contract. Recommended protection: zero, null/undefined, and explicit discounts, including the order caller.

Potential risks and optional suggestions: none additionally identified within this scope. The rest of checkout was not reviewed.

Suggested plan for F-001, not executed: preserve the zero-discount case in a regression test; restore the nullish operator when a fix is authorized; run relevant tests and verify integration of the order amount. Fixture inspection does not authorize changing a real application.

Validations performed: contract/base/candidate inspection; local execution of `node tests/check-fixtures.mjs`, regression reproduction and negative control, exit 0. That exit validates the harness, **not** the candidate.

Validations not performed: order integration tests, build, and browser; application/infrastructure are outside the fixture. No code was fixed. Actual order integration remains dependent on the supplied contract.

## Review / quick — clean control

Summary: no actionable findings identified within the inspected scope. The candidate returns the same expression previously assigned to a local variable.

Fixture context: nonnegative integer input, pure function, no requirement for an intermediate variable. Application architecture is unknown and irrelevant to this local equivalence.

Confirmed findings, potential risks, and optional suggestions: none. There is no justification for extraction, memoization, or additional abstraction.

Validations performed: function inspection and executable comparison through `node tests/check-fixtures.mjs` for 0, 1, 2, 10, and 1000; identical outputs, exit 0. This sample is not an exhaustive proof for arbitrary JavaScript values; the conclusion also uses the contract and identical expression.

Validations not performed: application, build, browser, and other consumers. No changes. No additional risk identified in the local change; this does not approve the entire project.

## Responsive-audit + visual-review — no browser

Summary: static overflow risk from fixed width; visual regression is inconclusive. No visual or responsive test was executed.

Context: browser, terminal, image, capture, and console unavailable according to the fixture. Baseline, HTML, parent layout, and global styles unknown. `.order-summary` changes from bounded fluid width to 960px.

**F-001 — Potential risk — Moderate — medium confidence: fixed width may exceed available space.** Location: `.order-summary` in the supplied candidate CSS, symbol without a full file. If available space is below 960px and no style/container compensates, the element may overflow. The effect depends on missing layout context. Inspect that context and preserve fluid sizing if intended; do not edit automatically. This ID belongs to this report, not the previous example.

Validation performed: static CSS comparison. No capture, compared pixels, console, or navigation observed.

Validations not performed and manual plan: define synthetic data and a stable environment; confirm breakpoints. As proposed examples, test 360, 768, and 1280 CSS px, recording browser/DPR/fonts/zoom. Open equivalent base/candidate states, inspect overflow and clipped content, navigate with the keyboard, and record console/authorized local captures. Classify a defect only after observing an unintended effect and connecting it to the change. Obtain a comparable baseline without overwriting existing approval. Do not capture sensitive information without permission.

Residual risks: actual layout, baseline, and behavior remain unobserved. The plan above is **not executed**.
