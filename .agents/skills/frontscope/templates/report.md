# Contrato de relatório FrontScope

Use português brasileiro por padrão. Preencha somente dados disponíveis; campos inaplicáveis devem ser marcados como tal, sem inventar evidência. Ajuste extensão ao escopo, mantendo as distinções abaixo.

## Resumo executivo

Modo, profundidade, alvo/base e conclusão breve. Se não houver problemas acionáveis, diga “Nenhum problema acionável encontrado no escopo analisado”, sem certificar o restante do projeto.

## Contexto e limites

Registre fatos confirmados e fontes, convenções inferidas, restrições explícitas, desconhecidos e capacidades/permissões que afetaram o trabalho. Identifique evidências fornecidas pelo usuário versus observadas por ferramentas. Não inclua segredos.

## Achados

Ordene por impacto; separe **confirmados**, **riscos potenciais** e **sugestões opcionais**. As categorias podem ficar vazias. Para cada item acionável:

| Campo | Conteúdo |
| --- | --- |
| Título | Problema concreto ou recomendação opcional identificada |
| Classificação | Confirmado / risco potencial / sugestão opcional |
| Severidade | Critical / High / Moderate / Suggestion |
| Confiança | Alta / média / baixa, com razão e premissa pendente |
| Local | Arquivo e linha verificável, símbolo ou escopo; lado do diff se necessário |
| Evidência | Trecho/saída/contrato, trigger e relação causal |
| Impacto técnico | Comportamento afetado, consumidor e consequências |
| Ação recomendada | Menor correção adequada, alternativa e trade-off quando pertinente |
| Validação | Caso observável que confirma a correção ou refuta o risco |

Severidade e confiança são eixos distintos:

- **Critical**: risco severo demonstrado à segurança, dados ou funcionalidade. Não use para hipótese sem demonstração.
- **High**: defeito significativo, regressão provável ou contrato quebrado.
- **Moderate**: custo relevante de manutenção, confiabilidade ou desempenho, com mecanismo explicado.
- **Suggestion**: melhoria opcional ou preferência contextual; não apresente como defeito.

Não promova preferência a Moderate. Um risco pode ter alto impacto e baixa confiança: exponha a premissa ainda não comprovada. Não duplique a mesma causa em múltiplos achados para inflar o relatório.

## Validações realizadas

Para cada check: comando/ferramenta ou inspeção, escopo/ambiente, resultado observado e evidência de saída/término. Classifique execução como aprovado, falhou ou bloqueado; análise estática é inspeção, não teste executado. Atribua logs fornecidos a quem os forneceu. Não converta um roteiro em aprovação.

## Validações não realizadas

Check, motivo (capacidade, permissão, artefato ou escopo), consequência e próximo passo. Em modos visuais, inclua capacidades/ambiente, baseline e controles ausentes.

## Mudanças e riscos restantes

Quando houve execução autorizada: arquivos/contratos alterados, por quê, comportamento preservado/intencionalmente alterado e checks correspondentes. Sempre inclua incertezas e riscos não cobertos; se não houver risco adicional identificado, limite essa declaração ao escopo. Recomendações de próximos passos não são ações já executadas.
