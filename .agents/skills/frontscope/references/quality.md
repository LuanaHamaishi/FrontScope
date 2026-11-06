# Desempenho, confiabilidade, segurança e acessibilidade

## Optimize

Comece pelo sintoma, fluxo, volume de dados e orçamento quando disponível. Separe perfil medido de hipótese estática. Avalie renderização/reatividade, recomputação, árvore de componentes, waterfalls de rede, tamanho do bundle, loading, cache e liberação de recursos. Para cada hipótese, indique mecanismo e medição: profiler do host/framework, trace, waterfall ou análise de bundle **se disponíveis**.

Memoização tem custos de comparação, memória e invalidação; cache pode servir dados incorretos e exigir limites. Justifique por cálculo/identidade/fluxo concreto e meça antes/depois quando autorizado. Não use quantidade de renders como defeito sem impacto. Sem instrumentos, forneça experimento, não percentuais de melhoria.

## Test

Mapeie risco → comportamento → nível de teste → asserção observável. Use unitários para regra isolada, integração para contratos/efeitos, componente para interação semântica e E2E para jornada crítica. Considere erros, vazio, concorrência, cancelamento e limites de dados pertinentes. Priorize proteção de regressão reproduzível, não meta arbitrária de cobertura.

Mocks devem respeitar contratos reais e não ocultar a incompatibilidade investigada; evite mockar precisamente a fronteira que o teste pretende validar. Melhore testabilidade com uma fronteira local quando houver necessidade, sem criar abstrações apenas para satisfazer mocks. Confira infraestrutura e comandos existentes antes de sugerir novas ferramentas.

Só classifique um check como aprovado após observar comando, escopo, saída e término. Diferencie aprovado, falhou, bloqueado e não executado. Resultado fornecido pelo usuário deve ser atribuído a ele; proposta de comando não é execução.

## Segurança e acessibilidade

Siga dados até sinks relevantes: HTML dinâmico, URLs, navegação, mensagens entre origens e storage. Confira fronteira de confiança, escape/sanitização no contexto correto, dados sensíveis em bundle/log/storage, validação no servidor e origem efetiva. Não confunda validação frontend com autorização. Para dependências, use evidência atual de advisory quando disponível e autorizado; falta de scanner não permite declarar ausência de vulnerabilidades.

Inspecione semântica HTML, nome acessível, rótulos, ordem/foco, teclado, estados, mensagens de erro e uso apropriado de ARIA. Elementos nativos podem resolver interações sem scripts extras. Contraste e layout podem exigir renderização; análise estática não comprova aparência, experiência com leitor de tela ou conformidade integral. Uma revisão leve não substitui auditoria completa de segurança/acessibilidade.

## Audit e explain

Em `audit`, delimite pacote, fluxos e amostra antes de ampliar. Carregue referências específicas apenas para problemas relevantes. Priorize por impacto e confiança, expondo partes não examinadas. Em `explain`, ensine mecanismo e trade-offs com exemplos rotulados; não transforme preferências em exigências.
