# Contexto fornecido

Pacote React 18.3.1, TypeScript, sem biblioteca de estado global. Componentes pequenos mantêm estado visual local. Os dados já chegam validados do domínio; `initial` é booleano. Não há relato de falha de desempenho. O escopo é somente este componente, sem autorização de edição. Os números abaixo são locais ao bloco.

```tsx
import { useState } from 'react';

export function Details({ initial = false }: { initial?: boolean }) {
  const [open, setOpen] = useState(initial);
  const label = open ? 'Ocultar detalhes' : 'Mostrar detalhes';
  return (
    <section>
      <button aria-expanded={open} onClick={() => setOpen(!open)}>{label}</button>
      {open && <p>Detalhes do produto</p>}
    </section>
  );
}
```
