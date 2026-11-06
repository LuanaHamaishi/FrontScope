# Arquitetura, responsabilidades e refatoração

## Avaliação arquitetural

Compare fronteiras declaradas com imports e fluxos reais. Procure ciclos relevantes, dependência de domínio em detalhes de transporte/UI, contratos instáveis e mudanças que atravessam módulos sem necessidade. Explique o custo observado: propagação de alterações, testes difíceis, estado divergente ou acoplamento entre entregas. Um diretório por feature ou camada pode ser adequado; não imponha Clean Architecture, Atomic Design, FSD ou outro padrão.

Em workspaces e microfrontends, identifique dono do contrato, direção das dependências, versionamento e ciclo de entrega. Uma extração compartilhada pode aumentar acoplamento e coordenação. Dependências e configurações existentes vêm antes de recomendações de reorganização.

## Locality First, Reusability When Needed

Escolha e justifique uma das três saídas:

| Saída | Quando faz sentido | Custo a considerar |
| --- | --- | --- |
| Manter no componente/módulo | Estado e transformação pequenos, coesos com a UI e fáceis de testar/entender | Extração adicionaria navegação sem isolar mudança real |
| Extrair módulo local junto ao consumidor | Regra/efeito com contrato próprio, complexidade independente ou fronteira útil de teste | Mais um contrato e coordenação de estado |
| Promover a compartilhado | Responsabilidade estável entre consumidores/domínios e dono claro | Acoplamento de versões, API pública e generalização |

Um único consumidor pode justificar um hook/composable, serviço, validador, mapper, adaptador ou componente **local**. Considere coesão, clareza, complexidade, testabilidade, direção das dependências, manutenção e convenções. Não exija reutilização nem a invente para justificar extração.

Separe preocupações de componente (interação/apresentação), feature (orquestração de um fluxo) e domínio (regra e contratos). Evite chamar toda lógica sem JSX/template de regra de domínio. Funções puras simples podem permanecer locais. Comprimento e quantidade de funções não provam mistura de responsabilidades.

Exemplo de decisão, não estrutura obrigatória: num checkout que calcula tributos, serializa requisições, acessa API e desenha formulário, um cálculo puro e um cliente HTTP ao lado do componente podem isolar mudanças e testes. O estado visual pode continuar no componente. Não crie automaticamente pastas `hooks/`, `services/`, `helpers/` ou `context/`; nem eleve módulos a `shared/` sem benefício demonstrado.

## Refactor

Antes de editar, exponha objetivo, evidência de custo, menor mudança proposta, alternativa de manter e trade-off. Preserve contratos observáveis: valores, erros, efeitos, ordem, timing, foco e acessibilidade relevantes. Diferencie melhoria estrutural de alteração intencional de comportamento.

Quando autorizado, trabalhe em passos revisáveis e preserve a API externa quando possível. Se uma extração altera captura de estado, ciclo de vida ou escopo de dependência, valide essa semântica no framework detectado. Use testes de comportamento existentes e adicione proteção proporcional ao risco quando necessário; não testes que apenas espelhem a nova estrutura. Se não houver validação executável, declare a lacuna.

Em `explain`, descreva mecanismo, cenário em que a alternativa ajuda e cenário em que não ajuda. Diagramas de dependência/fluxo podem ajudar, mas rotule inferências e exemplos; não apresente uma arquitetura idealizada como inventário real.
