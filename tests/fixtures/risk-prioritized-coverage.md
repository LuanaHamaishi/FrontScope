# Coverage priorities for a scoped change

Synthetic application context, not real financial or customer data. The user asks for a test plan for these changes using the existing unit/component/integration infrastructure. Actual project execution and browser access are unavailable; commit, installation, and production access are not authorized.

- Checkout retry handling touches submission coordination and the API adapter. An accidental double submission can create two orders. The server contract supports an idempotency key, and the client must preserve it across a retry. Recovery requires staff intervention. This is a critical business flow.
- Recoverable catalog sorting affects the displayed order of a single list. The chosen sort mode should remain consistent after a data refresh; no persisted data or authorization is changed.
- A static decorative caption gains a margin scoped to one isolated panel. No focus, contrast, visibility, breakpoint, or interaction behavior changes are specified. Appearance still has not been observed in a browser.
- A separate focus-style change removes the visible outline from the primary keyboard action in checkout. This affects a critical accessible journey even though it is a small CSS change.

Prioritize the requested protection, explain uncertainty and test levels, and distinguish potential risks from confirmed defects. Do not declare all CSS low risk, label a missing test a demonstrated Critical vulnerability, demand E2E everywhere, or report a fabricated risk percentage. Proposed test cases must include meaningful failure/boundary outcomes rather than just checking mocked call counts.
