# Progressive context discovery

Use before substantial engineering judgments. Discovery is a scoped investigation, not a mandatory inventory of the entire project.

1. Start with the request, target, and applicable legitimate instructions. Identify existing changes so you do not attribute or overwrite someone else's work. Establish whether the target is an application, library, workspace, or microfrontend.
2. Read the relevant package manifest, package manager information, available lockfile, and build/type/lint/test configuration governing the target. Distinguish declared ranges, lockfile resolutions, and observed installed versions. A lockfile alone does not prove the state of `node_modules`.
3. In the target and a few representative neighbors, identify language, framework/version, routing, state, data fetching, component composition, imports, design system, and architectural documentation. Do not investigate irrelevant topics further.
4. Follow contracts to producers and consumers: public types, events, APIs, routes, exports, and tests. In monorepos, expand only to workspaces connected to the behavior under investigation. In microfrontends, examine integration contracts, assets, state, and shared dependencies before suggesting centralization.
5. Stop when evidence is sufficient to assess the question or a specific gap blocks a conclusion. Request the missing file, diff, version, or symptom without presenting inference as fact.

Record a short context map:

| Category | Record |
| --- | --- |
| Confirmed | Fact plus supporting file/configuration/output |
| Inferred | Observed pattern, sample, and inference limits |
| Explicit constraint | Architectural rule and its legitimate source |
| Unknown | Missing information and its effect on the conclusion |

Without filesystem access, accept user-supplied evidence: a reduced tree, manifests without secrets, a diff with identified base/head, relevant callers, and tests. Without Git, compare supplied before/after material. Without a terminal, perform static analysis and list proposed validations as not performed. Without internet, use identified local documentation and state its version/provenance.

Do not infer missing tests from a partial listing or an entire architecture from one file. Inconsistent conventions may be legacy or defects: explain the concrete cost before proposing a change.
