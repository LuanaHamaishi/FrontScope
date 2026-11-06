# Supplied context

React 18.3.1, TypeScript, `checkout/` feature. The submission flow calls the function below with validated arguments and already handles API errors. The service accepts the displayed body. Taxes vary by region and change independently of presentation. Transport, tax rules, and the form belong to the same team; there are no other consumers. Feature modules are conventionally colocated. The request concerns responsibilities, without editing or changing tax rules. Omitting cents/rounding is a deliberate fixture simplification.

```tsx
export function Checkout() {
  async function submitOrder(net: number, region: 'A' | 'B') {
    const tax = region === 'A' ? net * 0.18 : net * 0.12;
    const response = await fetch('/api/orders', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ net, tax, gross: net + tax, region }),
    });
    if (!response.ok) throw new Error(`Order rejected: ${response.status}`);
    return response.json();
  }
  // Known OrderForm contract: calls onSubmit and handles rejections.
  return <OrderForm onSubmit={submitOrder} />;
}
```

`OrderForm` comes from the design system and is outside this change. Its implementation is unavailable in this fixture.
