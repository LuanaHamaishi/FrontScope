# Supplied context

React 18.3.1 package, TypeScript, no global state library. Small components keep visual state locally. Data arrives validated by the domain; `initial` is boolean. No performance failure has been reported. Scope is this component only, without editing authorization. Any code line references are local to the block.

```tsx
import { useState } from 'react';

export function Details({ initial = false }: { initial?: boolean }) {
  const [open, setOpen] = useState(initial);
  const label = open ? 'Hide details' : 'Show details';
  return (
    <section>
      <button aria-expanded={open} onClick={() => setOpen(!open)}>{label}</button>
      {open && <p>Product details</p>}
    </section>
  );
}
```
