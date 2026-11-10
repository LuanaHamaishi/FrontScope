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

When authorized, work in reviewable steps and preserve external APIs where possible. If extraction changes state capture, lifecycle, or dependency scope, validate that framework's semantics. Follow [context-aware test validation](quality.md#context-aware-test-validation): preserve behavioral expectations for a pure refactor, adapt test setup to legitimate structural changes, and add/update coverage when behavior or integration changes. Explain the rationale instead of mechanically freezing tests or rewriting them to accept a regression. Relevant test work can be part of the authorized implementation; respect any explicit restriction and state unavailable validation.

In `explain`, describe the mechanism, when an alternative helps, and when it does not. Dependency/flow diagrams can help, but label inferences and examples; do not present an idealized architecture as a real inventory.

## Project organization

Use `structure` for a new project/feature layout or an explicitly requested reorganization. This is an on-demand workflow in FrontScope, not a separate skill dependency. Start with the existing context and keep the responsibility decisions above; users do not need to name an extra mode or memorize a fixed folder pattern.

### Choose the convention and its scope

Identify framework/language, module/workspace boundaries, component model, styling, state/data libraries, test infrastructure, and current imports/exports. For a new project, distinguish actual decisions from proposed choices; do not invent installed tooling. If stack or ownership is missing and materially changes the layout, clarify it while presenting a framework-neutral responsibility map.

When a user chooses explicit separation into local modules, treat that as the organization convention for meaningful responsibilities in the target scope. Follow it consistently for new work rather than repeatedly arguing for another preference. Explain any exception where separation would introduce empty modules, circular dependencies, duplicated types, or state ownership problems. A chosen convention does not authorize reorganizing unrelated files or make every existing alternative a defect.

For an existing project, inspect actual consumers, aliases, public exports, generated files, and existing user changes before moving files. Present the target layout, old-to-new ownership/path mapping, behavioral invariants, and validation. If the user requests only advice, remain read-only. If implementation is already authorized, apply a small migration within that scope without asking again for routine moves already covered by the request. Do not overwrite styles/configuration or mix in unrelated dependency changes.

### Place responsibilities deliberately

| Responsibility | Suitable local boundary | Keep in mind |
| --- | --- | --- |
| Rendering and interaction | Component/template and its relevant styles | Keep simple cohesive UI state local; preserve semantic, focus, theme, and responsive behavior |
| Stateful behavior or lifecycle orchestration | React hook, Vue composable, or the framework's appropriate service/module | One consumer is enough; preserve instance scope, cleanup, dependencies, and library ownership rather than duplicating state |
| Pure transformations, validation, mapping, or calculation | Domain-named local function/module | A pure function does not need to become a hook; avoid an unbounded generic utilities bin |
| Stable configuration/constants | Local constants/configuration module when it clarifies a contract or meaningful group | Derived/reactive values are not constants; one trivial private literal may remain beside its use unless the chosen convention requires otherwise |
| Types and interfaces | A cohesive local type module, or the owning module's exports | Group by contract; do not require a file for every interface or duplicate generated/library/domain types. Use type-only imports where appropriate to the actual compiler |
| API and external integration | Existing client/adapter or a feature-local integration module | Reuse repository libraries and contracts; avoid a second client/state layer without a demonstrated need |
| Tests | Existing unit/component/integration placement conventions | Protect behavior and boundaries, not the number or names of extracted files |

Keep files beside their component/feature owner before promoting to shared packages. Extracting a single-consumer hook, function, or contract is valid when it improves clarity or follows the selected convention. Shared placement requires stable ownership and dependency justification, not simply two superficially similar functions. Plain JavaScript does not require new TypeScript interfaces; Angular/Svelte/Vue do not require React hooks.

For illustration, a React/TypeScript customer-search feature with asynchronous orchestration, a typed API result, mapping, and grouped search configuration could use:

```text
features/customer-search/
  CustomerSearch.tsx
  useCustomerSearch.ts
  customerSearch.types.ts
  customerSearch.constants.ts
  customerSearch.mapper.ts
  customerSearch.api.ts
  CustomerSearch.test.tsx
```

This example assumes each responsibility actually exists. It is not a scaffold to copy into every component: omit unneeded files, reuse existing clients/types, and adapt naming/placement to the chosen stack and conventions. Hooks, constants, pure functions, and interfaces may share a cohesive module where that is the deliberate choice. Do not create placeholder directories, barrel exports, path aliases, or a global state layer solely to make the tree look complete.

### Deliver and validate the organization

Explain what stays, what moves locally, what becomes shared, and why. Include the purpose of each proposed module and the cost of additional indirection. For migrations, check imports, public contracts, cycles, style scope, runtime/lifecycle behavior, and tests using the actual project tooling. Test imports/setup may change legitimately while behavioral expectations remain stable for a pure refactor. Report proposed structure separately from files actually created or moved, and state any type/build/runtime/visual checks not performed.
