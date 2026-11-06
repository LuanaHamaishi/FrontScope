# Revisão, impacto e investigação

## Review

Confirme qual mudança revisar: working tree, staged, commits ou PR e sua base. Quando Git estiver disponível, operações de leitura como status, diff e inspeção de arquivos ajudam; não faça fetch, checkout ou reset implicitamente. Para PRs, não confunda diff entre pontas com diff desde o ancestral comum. Se a base estiver ausente, peça-a ou limite a revisão ao material fornecido.

Leia o diff e o contexto completo das linhas afetadas. Siga tipos, callers, consumidores e testes que possam confirmar ou refutar uma suspeita. Diferencie defeito introduzido, problema preexistente e exposição de problema anterior; não atribua ao PR um defeito inalterado sem demonstrar relação.

Para cada candidato, procure:

- Trigger e entrada concreta; resultado antes/depois e contrato esperado.
- Evidência de alcançabilidade: caller, configuração, fluxo de UI ou teste.
- Explicação causal e impacto para usuário/consumidor.
- Contraexemplo que refute a hipótese: guard existente, validação anterior, contrato diferente ou código morto.

Analise estados vazios, zero, falsos, nulos, erros, loading, concorrência, cancelamento e desmontagem quando pertinentes. Confira tipos/serialização, eventos, compatibilidade de API e autorização efetiva, sem aplicar checklists irrelevantes. Referencie linhas do arquivo atual ou identifique explicitamente o lado do diff. Se não houver numeração confiável, use símbolo/trecho e escopo; não invente linhas.

Um problema plausível sem premissa comprovada é risco potencial. Preferência sem custo concreto é sugestão opcional. Um diff limpo pode resultar em zero achados.

## Impact

Construa um mapa pequeno: mudança → contrato → consumidores → comportamento → validação. Inclua exports públicos, pacotes downstream, rotas, persistência, estado e integrações apenas quando houver dependência. Diferencie impacto direto demonstrado e indireto inferido. Para APIs públicas, avalie consumidores externos desconhecidos como lacuna; a busca local não os exclui.

Escolha regressões que distingam antes/depois: entradas de fronteira, erro, fluxo nominal e integração relevante. Declare o limite de cobertura da busca.

## Debug

Registre esperado, observado, ambiente/versões e passos mínimos. Separe hipóteses por evidência e escolha uma observação que as diferencie. Busque causa, não somente um local onde o sintoma aparece. Não atribua causa definitiva com base em correlação. Sem reprodução, apresente diagnóstico estático e o próximo experimento. Não afirme que uma correção resolveu o problema sem validação correspondente.
