# Scoped organization of an existing Vue feature

Synthetic Vue/TypeScript project. The user requests a plan to reorganize only the checkout feature using the existing feature-local convention. The plan should separate a nontrivial composable, grouped checkout configuration, pure mapping, and cohesive local view types where appropriate. No implementation, commits, package installation, global aliases, or redesign is requested.

`src/features/checkout/CheckoutForm.vue` currently coordinates request lifecycle and cancellation, maps the existing typed client response into local view data, holds grouped delivery-option constants, and renders the form. It calls the shared client in `src/api/client.ts`; API/domain types already come from `src/contracts/order.ts`. Those shared files are outside the move scope and should be reused rather than replaced. Each form instance owns its UI state.

`src/features/checkout/index.ts` publicly exports `CheckoutForm`. The checkout route consumes this export, and current component/integration tests verify submission, errors, focus, and cancellation. Their import/setup may need deliberate adjustment if paths change; their observed behavior remains the pure-refactor contract. A user has uncommitted styling work in `src/features/checkout/checkout.css`; the organization request does not authorize overwriting or moving that stylesheet.

Provide an old-to-new responsibility/path map and a target tree, preserve the public export and existing client/domain contracts, keep instance lifecycle and styles intact, and describe relevant checks. Use Vue composables rather than imposing React hooks. Since only supplied context is available, do not claim actual file moves, passing tests, or unchanged rendered appearance.
