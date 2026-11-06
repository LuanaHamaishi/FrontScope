# Avaliação da skill

Há duas camadas: integridade dos artefatos e comportamento de um agente. Checks estruturais não aprovam decisões de engenharia. Os fixtures têm entradas fixas; respostas de modelos variam e não são testes determinísticos.

## Checks locais reproduzíveis

Na raiz do repositório:

```powershell
python -X utf8 tests/validate.py
node tests/check-fixtures.mjs
python -X utf8 tests/probe_codex.py
git diff --check
```

Python 3.9+ é necessário somente para os validadores; Node com suporte a módulos `.mjs` somente para executar os exemplos JavaScript. Nenhum deles é exigido pela skill para revisar código. A sonda requer Codex instalado, usa sua configuração existente e inicia/encerra apenas um app-server local, sem turno de modelo. É opcional e pode ficar bloqueada por política do host. Ela não testa Copilot, Claude, seleção automática ou execução de uma revisão.

`validate.py` verifica o perfil YAML restrito usado no pacote (strings e metadata), naming/diretório, links relativos, isolamento dos recursos e integridade do manifesto. Não é parser YAML geral nem validador oficial completo. `check-fixtures.mjs` prova o trigger da regressão e a equivalência do controle nas entradas testadas. Seu sucesso significa que **o defeito do fixture foi reproduzido**, não que a candidata está correta.

Validador externo opcional: `skills-ref validate .agents/skills/frontscope`, conforme a [especificação oficial](https://agentskills.io/specification). Só execute se já disponível ou se sua instalação estiver autorizada. O `quick_validate.py` da skill-creator precisa de PyYAML; sua ausência não exige instalação para usar FrontScope.

## Avaliação comportamental

O [manifesto](cases.json) guarda prompts, entradas e rubricas. Para não contaminar a resposta com o gabarito:

1. Inicie sessão nova no agente-alvo com a skill instalada. Registre host/versão, modelo, data, permissões e capacidades. Verifique descoberta separadamente.
2. Forneça o `prompt` de **um** caso e somente seus arquivos `inputs`, além da skill. Não forneça `accept`/`reject`, exemplos de saída ou resultados anteriores. Restrinja ferramentas conforme o fixture. Se precisar de isolamento, use workspace temporário sem acesso aos gabaritos.
3. Guarde relatório, atividade de ferramentas e alterações observadas em local autorizado. Logs de execução só valem se produzidos nesse ensaio. Compare somente a base/candidata listadas.
4. Confronte a resposta com **todos** os critérios `accept`/`reject`: atendido, não atendido ou inconclusivo, com trecho da resposta. Qualquer rejeição observada reprova o caso; evidência ausente não permite aprovação presumida.
5. Confira ausência de escrita, instalação ou acesso externo indevido. Para comparar agentes/modelos, repita entradas em sessões novas e registre variação. Uma resposta isolada não é garantia.

Descoberta explícita e seleção automática são ensaios separados. No segundo, use intenção natural sem citar a skill e observe se o host carrega o arquivo e somente as referências pertinentes.

| Critério do briefing | Caso |
| --- | --- |
| Componente coeso; evitar extração/overengineering | `local-react`, `local-vue`, `clean` |
| Responsabilidades misturadas; módulos locais | `mixed` |
| Regressão significativa | `regression` |
| Diff limpo sem achados inventados | `clean` |
| Upgrade com notas e uso no código | `upgrade` |
| Relatório com evidência, severidade e incerteza | `regression` e rubricas dos demais |
| Browser ausente com fallback | `browser-unavailable` |
| Princípios comparáveis em duas tecnologias | `local-react` e `local-vue` |
| Resistência a instrução injetada | `injection` |

[examples.md](examples.md) contém demonstrações produzidas durante a implementação, não ensaios independentes ou prova de execução integrada. O registro dos checks está em [validation.md](validation.md).

## Próximos ensaios com repositórios de amostra

- Apps React e Vue pequenos com lockfile e suíte já instalados: casos de localidade e depois diff real com caller/teste de regressão. Usar cópias de teste sem dados privados.
- Workspace com biblioteca compartilhada: `impact/deep` sobre contrato entre dois pacotes; verificar se a investigação fica nos consumidores conectados.
- Upgrade real em branch de teste: notas oficiais das versões exatas, peers e build + fluxo de runtime. Comparar pré e pós-upgrade.
- UI sintética com suíte de browser existente: console, foco, viewports e diferença intencional; testar proteção de baseline e fallback quando o browser falhar.

Angular/Svelte, grandes monorepos, imagem e autorização de modificações precisam de ensaios próprios antes de declarar esses comportamentos verificados. As referências oferecem orientação, não certificação das integrações.
