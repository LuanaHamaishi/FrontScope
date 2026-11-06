# Contrato do checkout

Função JavaScript pura usada no resumo e na emissão do valor do pedido. `subtotal` é um número não negativo e `discountPercent` é validado antes da chamada: número entre 0 e 100, null ou undefined. Zero significa sem desconto; null/undefined aplicam o desconto padrão de 10%. O caller envia `total(100, 0)` na compra sem promoção. `before.mjs` é base e `after.mjs` é candidata. Não há autorização para editar, executar instalações ou acessar rede. Se houver terminal, a execução de checks locais sem rede está autorizada.
