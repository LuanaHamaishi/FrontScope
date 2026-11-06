# Observed convention and trust boundary

TypeScript frontend; framework choice does not affect this case. Supplied architecture documentation requires displaying user content as text. The endpoints return a user-controlled string, not authorized HTML. These routes have no sanitizer, Trusted Types policy, or earlier transformation. CSP allows inline handlers in this fixture environment. The component uses existing, non-null document elements.

Two neighboring legacy files use `element.innerHTML = response.displayName`. Repetition is evidence of an existing pattern, but no architectural decision approves this behavior.

Base `profile/renderName.ts`:

```ts
export function renderName(element: HTMLElement, displayName: string) {
  element.textContent = displayName;
}
```

Candidate:

```ts
export function renderName(element: HTMLElement, displayName: string) {
  element.innerHTML = displayName;
}
```

The caller passes `response.displayName` directly, controlled by another user. A value may contain `<img src=x onerror=alert(1)>`; do not execute this content. The diff justification is consistency with the two legacy files. Scope: review this change without fixing neighbors, opening a browser, editing source, or accessing the network. No test or payload execution results were supplied.
