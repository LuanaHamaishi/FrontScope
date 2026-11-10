# Safe frontend changes

Use for implementation and reviews involving presentation, shared UI, or library contracts. The goal is a correct requested change that fits its repository. Do not judge code as defective merely because it resembles an AI-generated style; identify concrete behavior, compatibility, maintenance, or accessibility costs.

## Define the change boundary

Identify requested behavior, affected files/consumers, existing user changes, and what should remain observable. Read surrounding code before replacing it. Prefer focused edits over rebuilding a file from a template, re-scaffolding a feature, replacing configuration, or formatting unrelated files. Trace shared abstractions before changing them. File replacement can be justified, but explain why it is necessary and preserve unrelated behavior/work; file length alone is not justification.

Before delivery, review the final diff against the request and existing consumers. Check for lost handlers, accessibility attributes, error/loading states, exports, tests, and styling. This is a self-review, not an independent review claim. Do not assume reviewing a diff eliminates the need to inspect context.

## Preserve presentation outside the intended change

Inspect the target component, relevant stylesheet/imports, style scoping, design-system components, tokens, variants, theme, and breakpoints. Use the project's existing CSS/modules/utilities/component-library conventions. In a behavior-only change, keep layout, spacing, typography, colors, responsive behavior, interaction states, and semantic/accessibility behavior unless a necessary change is demonstrated.

Do not reset global CSS, replace a theme, edit shared tokens, introduce broad selectors, override vendor styles, or add escalating specificity/`!important` simply to make one component look right. Follow cascade and consumers first. Prefer an existing component variant or a scoped rule when appropriate. A shared-style change may be correct if intentionally required: identify its broader effects and validate relevant consumers.

When design changes are requested, implement their actual scope rather than freezing all styles. Preserve unrelated parts, and explain any shared impact. For a new validation message, for example, reuse existing error tokens and component state instead of redesigning every input.

Use available authorized visual/component checks for affected states. Without a browser or comparable baseline, state that appearance was not verified; a small CSS diff or successful unit test does not establish visual equivalence. A color change can affect critical accessibility even if it looks cosmetic.

## Investigate existing libraries before choosing implementation

1. Identify the relevant workspace manifest and lockfile, actual imports/wrappers, configuration, local type declarations, and representative usage. Distinguish declared, resolved, and observed installed versions; a dependency's presence does not prove it is used or supports a proposed API.
2. Reuse appropriate existing components, form/validation/state/data utilities, and test tooling when they satisfy the requirement. Check actual configuration and supported extension points. Do not invent a parallel framework, generic wrapper, or replacement library merely because it is familiar. Existing tools can still be unsuitable; explain the concrete gap and alternatives rather than forcing reuse.
3. For unfamiliar or version-sensitive APIs, consult official version-appropriate documentation, release notes, or repository-local types/source through approved tools. Record the version/source supporting the decision. Do not use latest-version examples for an older installation without checking compatibility. Do not invent an import, option, event, or prop; use typecheck and callers as additional evidence, not permission to suppress errors with casts or ignored diagnostics.
4. Without documentation/network access, continue from identified local evidence and expose unresolved API assumptions. Ask for missing evidence when it blocks correctness. Do not upload private code to research a public API or claim documentation was consulted when it was not.

Dependency installation/upgrades, replacements, and config changes must fit task authorization and host permissions. Prefer the smallest viable change; do not silently change the lockfile to obtain an API used by generated code.

## Review generated code for concrete defects

Look for unsupported imports/props, incompatible types, invented domain defaults, duplicate state, missing cleanup, swallowed errors, hardcoded placeholder data, empty handlers, fake success paths, and unnecessary dependencies or abstractions. Judge each by actual contracts, reachable paths, and maintenance cost. Do not introduce `any`, `as unknown as`, ignored diagnostics, or blanket catches merely to make validation green. A legitimate exception needs a documented reason and a safe boundary.

Replace scaffolding placeholders with real in-scope behavior, or clearly identify incomplete work. Tests should exercise that behavior rather than blessing a stub. Preserve established naming and useful conventions without treating an unsafe precedent as mandatory.

## Turn demonstrated recurring errors into useful checks

Inspect the repository's lint/typecheck/test commands and existing hooks/CI before proposing another check. Distinguish an absent check, an existing broken check, a command that is not connected to the normal workflow, and a judgment-based concern. A reproducible mechanical mistake may justify an existing lint rule, type restriction, or focused regression test; do not create duplicate rules or a platform for a one-off preference.

Prefer a cheap deterministic check where it captures the demonstrated failure. Explain its coverage and limits. Hooks, CI changes, repository policies, and new tools must fit the request and permissions; their absence alone is not automatically a high-severity defect. Keep contextual decisions in focused references instead of expanding global instructions with every incident. Do not depend on another skill, specific agent, session-log access, or an extra reviewer being available.
