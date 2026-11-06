# Contexto fornecido

React 18.3.1, TypeScript, feature `checkout/`. `submitOrder` chama esta função com argumentos validados e já trata erros da API. O serviço aceita o corpo mostrado. Tributos variam por região e mudam independentemente da apresentação. Transporte, regra tributária e formulário são mantidos pela mesma equipe; não há outros consumidores. A convenção é colocar módulos da feature lado a lado. A análise pedida é de responsabilidades, sem edição ou mudança da regra tributária. Omitir centavos/arredondamento aqui é uma simplificação deliberada do fixture.

```tsx
export function Checkout() {
  async function submitOrder(net: number, region: 'A' | 'B') {
    const tax = region === 'A' ? net * 0.18 : net * 0.12;
    const response = await fetch('/api/orders', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ net, tax, gross: net + tax, region }),
    });
    if (!response.ok) throw new Error(`Pedido recusado: ${response.status}`);
    return response.json();
  }
  // OrderForm possui contrato conhecido: chama onSubmit e trata rejeições.
  return <OrderForm onSubmit={submitOrder} />;
}
```

`OrderForm` é fornecido pelo design system e não faz parte da mudança. Sua implementação não está disponível neste fixture.
