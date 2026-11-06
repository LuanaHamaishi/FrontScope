# Saídas guiadas de exemplo

Exemplos redigidos pelo agente que implementou a skill, aplicando suas instruções aos fixtures. Não são avaliações cegas, execuções do Copilot/Claude ou resultados de uma suíte de modelos. Os resultados JavaScript citados foram observados no check local indicado; nenhum browser foi usado.

## Review / standard — regressão

Resumo: regressão confirmada no cálculo do checkout. Revisão de leitura limitada à função e ao contrato fornecido.

Contexto: JavaScript puro; o caller fornece `discountPercent=0` para compras sem promoção. Contrato confirmado pelo fixture, não por aplicativo real. Infraestrutura e demais consumidores desconhecidos.

**Confirmado — High — confiança alta: zero passa a receber desconto padrão.** Local: `tests/fixtures/regression/after.mjs`, linha 2, `total`. A troca de `??` por `||` substitui zero por 10. O check `node tests/check-fixtures.mjs` observou `total(100, 0)=100` na base e `90` na candidata. Como o valor é usado na emissão do pedido, uma compra sem promoção recebe desconto indevido. Ação mínima: preservar o teste de nulidade da base. Validar explicitamente null/undefined acrescentaria código sem benefício demonstrado neste contrato. Proteção recomendada: zero, null/undefined e desconto explícito, incluindo o caller do pedido.

Riscos potenciais e sugestões opcionais: nenhum adicional identificado neste escopo. Não se revisou o restante do checkout.

Validações realizadas: inspeção de contrato/base/candidata; execução local de `node tests/check-fixtures.mjs`, reprodução da regressão e controle negativo, término 0. Esse término aprova o harness, **não** a candidata.

Validações não realizadas: testes integrados do pedido, build e browser; app/infraestrutura não fazem parte do fixture. Nenhum código foi corrigido. Integração real do valor emitido permanece dependente do contrato fornecido.

## Review / quick — controle limpo

Resumo: nenhum problema acionável encontrado no escopo analisado. A candidata retorna a mesma expressão antes atribuída a uma variável local.

Contexto do fixture: entrada inteira não negativa, função pura e sem requisito de variável intermediária. Arquitetura da aplicação é desconhecida e irrelevante para essa equivalência local.

Achados confirmados, riscos potenciais e sugestões opcionais: nenhum. Não há justificativa para extração, memoização ou abstração adicional.

Validações realizadas: inspeção das funções e comparação executável em `node tests/check-fixtures.mjs` para 0, 1, 2, 10 e 1000; saídas iguais, término 0. A amostra não é prova exaustiva para qualquer valor JavaScript; a conclusão usa também o contrato e a expressão idêntica.

Validações não realizadas: aplicação, build, browser e demais consumidores. Sem alterações. Nenhum risco adicional identificado na mudança local; não é aprovação do projeto inteiro.

## Responsive-audit + visual-review — sem navegador

Resumo: risco estático de overflow com largura fixa; regressão visual inconclusiva. Nenhum teste visual ou responsivo foi executado.

Contexto: browser, terminal, imagem, captura e console indisponíveis conforme fixture. Baseline, HTML, layout pai e estilos globais desconhecidos. `.order-summary` muda de largura fluida limitada para 960px.

**Risco potencial — Moderate — confiança média: largura fixa pode exceder o espaço disponível.** Local: `.order-summary` no CSS candidato, símbolo sem arquivo completo. Se o espaço for menor que 960px e nenhum estilo/contêiner compensar, o elemento poderá transbordar. O efeito depende do layout ausente. Recomenda-se inspecionar o contexto e preservar dimensionamento fluido se essa for a intenção; não editar automaticamente.

Validação realizada: comparação estática dos trechos CSS. Não há captura, pixels comparados, console ou navegação observada.

Validações não realizadas e roteiro manual: definir dados sintéticos e ambiente estável; confirmar breakpoints. Como exemplos propostos, testar larguras 360, 768 e 1280 CSS px, registrando browser/DPR/fontes/zoom. Abrir o mesmo estado na base/candidata, observar overflow e conteúdo cortado, navegar por teclado e registrar console/capturas locais autorizadas. Só classificar defeito após observar efeito indevido e relacioná-lo à mudança. Obter baseline comparável sem sobrescrever aprovação existente. Não capturar informação sensível sem permissão.

Riscos restantes: layout real, baseline e comportamento não observados. Roteiro acima **não executado**.
