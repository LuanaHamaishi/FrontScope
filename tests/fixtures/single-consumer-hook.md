# Supplied context

React 18.3.1, TypeScript. The `invoices/` feature colocates local modules. `useInvoiceFilters.ts` was extracted to coordinate two filter controls and allow their behavior to be tested separately from presentation. `InvoiceTable.tsx` is its only consumer, confirmed by the supplied search. Lists contain at most 50 items; there is no performance symptom. `InvoiceRows` is a design system component receiving the filtered items. No other consumers, mandatory sharing rule, or editing authorization exists.

`invoices/useInvoiceFilters.ts`:

```ts
import { useState } from 'react';

type Invoice = { id: string; customer: string; paid: boolean };

export function useInvoiceFilters(invoices: Invoice[]) {
  const [query, setQuery] = useState('');
  const [unpaidOnly, setUnpaidOnly] = useState(false);
  const visibleInvoices = invoices.filter(invoice =>
    invoice.customer.toLowerCase().includes(query.toLowerCase()) &&
    (!unpaidOnly || !invoice.paid)
  );
  return { query, setQuery, unpaidOnly, setUnpaidOnly, visibleInvoices };
}
```

`InvoiceTable` invokes the hook with current items, binds `query` to a labeled input and `unpaidOnly` to a labeled checkbox, and passes `visibleInvoices` to `InvoiceRows`. Each instance owns its filters. This contract includes no external effects or URL synchronization. Having one consumer is the reason for the requested assessment, not a previously established defect.
