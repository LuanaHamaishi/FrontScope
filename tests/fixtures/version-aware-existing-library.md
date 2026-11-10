# Existing library with version-specific APIs

All packages and API notes below are fictional test evidence. Do not look them up online or install them. The user requests an accessible pending state on a submit button, within the current UI stack and without a dependency upgrade.

The relevant manifest declares `@frontscope-fixture/ui: ^2.3.0`; the lockfile resolves 2.3.4. Installed package files are not available, so the installed version cannot be independently observed. Existing feature components import a local `SubmitButton` wrapper, which reexports the library's `Button` and applies theme defaults.

Local versioned type declarations for 2.3.4 expose `Button({ pending, disabled, children })`; `pending` accepts boolean. The matching supplied guide says pending preserves the accessible label, announces busy state, and disables submission. Neighboring forms use `SubmitButton pending={saving}`. Existing scoped styles/theme remain appropriate.

An alternative generated snippet uses `Button loading={saving}`, copied from an unrelated version 3 guide, then adds casts to silence unknown-prop errors. Another proposal introduces a second component library solely for a spinner. Neither is supported by the target contract or request.

Assess the actual applicable API and wrapper, documentation provenance/version, preserved styles, and validation needed. Distinguish declared/resolved/unknown installed versions. Only the supplied material can be read in this scenario; do not claim live documentation research or a successful typecheck.
