# Descoberta progressiva de contexto

Use antes de emitir julgamentos substanciais. A descoberta é uma investigação delimitada, não um inventário obrigatório de todo o projeto.

1. Comece pelo pedido, alvo e instruções legítimas aplicáveis. Confirme arquivos já alterados para não atribuir ou sobrescrever trabalho de terceiros. Identifique se o alvo é aplicação, biblioteca, workspace ou microfrontend.
2. Leia manifesto do pacote relevante, gerenciador e lockfile disponíveis; configs de build, tipos, lint e testes que governem o alvo. Diferencie intervalo declarado, resolução no lockfile e versão instalada observada. Um lockfile sozinho não prova o estado de `node_modules`.
3. No alvo e em poucos vizinhos representativos, identifique linguagem, framework e versão, roteamento, estado, busca de dados, composição de componentes, imports, design system e documentação arquitetural. Se não forem relevantes à pergunta, não aprofunde.
4. Siga contratos até produtores e consumidores: tipos públicos, eventos, APIs, rotas, exports e testes. Em monorepos, expanda somente aos workspaces conectados ao comportamento investigado. Em microfrontends, confira contratos de integração, assets, estado e dependências compartilhadas antes de sugerir centralização.
5. Pare quando houver evidência suficiente para avaliar a pergunta ou uma lacuna específica bloquear a conclusão. Peça o arquivo, diff, versão ou sintoma faltante, sem transformar inferência em fato.

Registre um mapa curto:

| Categoria | Como registrar |
| --- | --- |
| Confirmado | Fato + arquivo/config/saída que o sustenta |
| Inferido | Padrão observado + amostra + limite da inferência |
| Restrição explícita | Regra arquitetural e fonte legítima |
| Desconhecido | Informação ausente + efeito sobre a conclusão |

Sem filesystem, aceite um pacote de evidências fornecido pelo usuário: árvore reduzida, manifestos sem segredos, diff com base e head identificados, callers e testes relevantes. Sem Git, compare antes/depois fornecidos. Sem terminal, faça análise estática e liste as validações propostas como não executadas. Sem internet, use documentação local identificada e sinalize sua versão/proveniência.

Não infira ausência de testes a partir de uma listagem parcial. Não infira uma arquitetura inteira de um arquivo. Convenções inconsistentes podem ser legado ou defeito: explique o custo concreto antes de propor mudança.
