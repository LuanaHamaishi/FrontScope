# Architecture, responsibilities, and refactoring

## Architectural assessment

Compare declared boundaries with actual imports and flows. Look for relevant cycles, domain dependencies on transport/UI details, unstable contracts, and changes unnecessarily crossing modules. Explain the observed cost: change propagation, difficult testing, divergent state, or coupled delivery. Feature-based and layer-based structures can both be appropriate; do not impose Clean Architecture, Atomic Design, FSD, or another pattern.

In workspaces and microfrontends, identify contract ownership, dependency direction, versioning, and delivery lifecycle. Shared extraction can increase coupling and coordination. Inspect existing dependencies and configuration before recommending reorganization.

## Locality First, Reusability When Needed

Choose and justify one of three outcomes:

| Outcome | When appropriate | Cost to consider |
| --- | --- | --- |
| Keep in the component/module | State and transformations are small, cohesive with the UI, and easy to test/understand | Extraction would add navigation without isolating a real change boundary |
| Extract a local module near its consumer | A rule/effect has its own contract, independent complexity, or useful testing boundary | Another contract and state coordination |
| Promote to shared | Stable responsibility across consumers/domains with clear ownership | Version coupling, public API, and generalization |

One consumer can justify a **local** hook/composable, service, validator, mapper, adapter, or component. Consider cohesion, clarity, complexity, testability, dependency direction, maintenance, and conventions. Do not require reuse or invent it to justify extraction.

Separate component concerns (interaction/presentation), feature concerns (flow orchestration), and domain concerns (rules/contracts). Not all logic outside JSX/templates is domain logic. Simple pure functions may remain local. Length and function count do not prove mixed responsibilities.

Decision example, not a required structure: in a checkout that calculates taxes, serializes requests, calls an API, and renders a form, a pure calculation and an HTTP client beside the component may isolate changes and tests. Visual state can remain in the component. Do not automatically create `hooks/`, `services/`, `helpers/`, or `context/` folders, or promote modules into `shared/` without demonstrated benefit.

## Refactor

Before editing, explain the goal, evidence of cost, minimal proposed change, alternative of keeping the implementation, and trade-off. Preserve observable contracts: values, errors, effects, ordering, timing, focus, and relevant accessibility behavior. Distinguish structural improvement from intentional behavior changes.

When authorized, work in reviewable steps and preserve external APIs where possible. If extraction changes state capture, lifecycle, or dependency scope, validate that framework's semantics. Use existing behavior tests and add protection proportional to risk when necessary, not tests that mirror the new structure. State gaps when executable validation is unavailable.

In `explain`, describe the mechanism, when an alternative helps, and when it does not. Dependency/flow diagrams can help, but label inferences and examples; do not present an idealized architecture as a real inventory.
