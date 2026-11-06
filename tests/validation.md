# Registro de validação — v0.1.0

Data: 6 de novembro de 2026 (America/Sao_Paulo). Checks locais executados no workspace Windows/PowerShell. Nenhuma instalação de pacotes foi necessária.

## Evidências observadas

| Comando/check | Resultado |
| --- | --- |
| `python -X utf8 tests/validate.py` | 16 documentos, 36 links locais e oito cenários; perfil de frontmatter, correspondência nome/diretório, links, isolamento dos recursos e manifesto validados; término 0 |
| `node tests/check-fixtures.mjs` | Regressão reproduzida: base retorna 100 e candidata 90 para desconto zero; demais quatro entradas comparadas; controle limpo com saídas iguais nas cinco entradas; término 0 |
| `python -X utf8 tests/probe_codex.py` | Descoberta nativa via `skills/list`: `name=frontscope`, `scope=repo`, `enabled=true`, caminho para `.agents/skills/frontscope/SKILL.md`; sem turno de modelo; término 0 |
| `git diff --check` | Sem erros de whitespace no diff rastreado; término 0. Arquivos novos também conferidos por inspeção local de whitespace |
| Experimento isolado do validador, via Python/stdin | Em cópia temporária, pacote íntegro aceito; nome divergente e recurso referenciado ausente rejeitados. Arquivos originais preservados; término 0 |

Binário observado: `codex-cli 0.164.0-alpha.11.1`. A consulta de descoberta foi feita primeiro diretamente pelo protocolo local e depois disponibilizada na sonda reproduzível. Ela verifica este caminho, não outra instalação com nome igual. O parser nativo aceitou os metadados e habilitou a skill.

Para reproduzir o experimento negativo, copie o pacote, README e testes para um diretório temporário e execute o validador dessa cópia: primeiro sem alterações (esperado 0), depois com `name` diferente do diretório (esperado 1); restaure o arquivo e renomeie `references/context.md` (esperado 1). Não altere a instalação em uso para esse teste. Esses são checks de integridade, não avaliações de comportamento do agente.

## O que estes checks não demonstram

- Os oito cenários foram empacotados com entradas e rubricas, mas não executados como bateria independente em sessões novas de modelo. Três relatórios guiados em [examples.md](examples.md) demonstram regressão, controle limpo e fallback; não são ensaio cego.
- Não houve revisão integrada em nova sessão Codex/VS Code, teste de seleção automática ou descoberta/execução em Copilot e Claude Code. Compatibilidade ponta a ponta permanece não verificada.
- React/Vue são fixtures de código para avaliação de decisão; não houve montagem dos componentes em um framework. Angular/Svelte têm orientação, sem execução específica.
- Browser, screenshots, comparação visual, profiling e scanners de segurança/dependências não foram executados. Não há baseline aprovado ou resultado de acessibilidade integral.
- `skills-ref` não foi executado. O validador local é restrito ao perfil YAML deste pacote. O `quick_validate.py` da skill-creator não foi executado porque PyYAML está ausente (detecção por `importlib.util.find_spec('yaml')` retornou falso); nenhum pacote foi instalado para suprir essa ferramenta opcional.
- Um check de fixtures JS não é suíte de testes da aplicação nem prova de revisão correta de qualquer repositório.

Siga o [protocolo de avaliação](README.md) para executar os casos em agentes reais com as mesmas entradas e gabarito separado.
