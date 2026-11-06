# Navegador e validação visual: adaptador do host

Este é um protocolo de instruções v0.1, não uma implementação de driver. O host pode fornecer browser automation, terminal com suíte existente, screenshots anexados ou nenhuma dessas capacidades. Playwright é opcional; sua presença no manifesto não prova navegador instalado, servidor disponível ou autorização para executar.

## Detecção e escolha

Antes de qualquer ação, registre capacidades como **disponível**, **indisponível** ou **desconhecida**, com evidência. Avalie separadamente: navegação/interação, captura, leitura de imagens, comparação, console/runtime, servidor de teste e armazenamento local de artefatos. Verifique também permissão, alvo/ambiente e dados envolvidos.

| Condição observada | Adaptador e resultado permitido |
| --- | --- |
| Ferramenta de browser + ambiente autorizado | Use as operações reais do host; registre passos e resultados |
| Terminal + suíte existente executável e autorizada | Inspecione config/scripts e execute o alvo pertinente; não instale browser/pacotes implicitamente |
| Apenas capturas fornecidas e leitura de imagem | Compare o que é visível; não alegue interação, console ou medições não fornecidas |
| Sem browser/imagem ou com autorização ausente | Faça análise estática delimitada e entregue roteiro manual **não executado** |

Ferramenta falhou ou ambiente não iniciou: registre erro, interrompa a ação dependente e use fallback. Não repita instalações nem amplie permissões silenciosamente. Nenhum navegador é requisito para uma revisão de código funcionar.

## Contrato do adaptador

Mapeie operações lógicas para capacidades que realmente existem, sem inventar APIs: preparar estado → abrir alvo → configurar viewport → interagir → observar/capturar → inspecionar console → comparar → relatar. Operação não suportada deve retornar no relatório “não executada” e motivo. Não force um driver único nem prometa automação futura pronta.

Entradas mínimas: alvo local/teste autorizado, caso/estado, revisão base e candidata quando comparadas, viewport e evidência de baseline. Saída: capacidades e permissões, ambiente, passos, observações, artefatos locais autorizados, diferenças, classificação e lacunas. Não publique nem envie artefatos a serviços externos sem autorização.

## Execução por modo

- `visual-review`: compare estados equivalentes de base/candidata. Relacione diferença a linhas de estilo/template/estado somente se houver evidência. Diferencie mudança esperada, possível regressão e inconclusivo; diferença visual isolada não é defeito confirmado.
- `browser-test`: defina passos e resultado observável antes de interagir. Cubra o comportamento pedido, erros de runtime/console disponíveis, foco e teclado relevantes. Diferencie resultado funcional de aparência.
- `responsive-audit`: derive viewports de breakpoints e dispositivos relevantes; verifique overflow, conteúdo cortado, ordem, alvos de interação e foco. Sem renderização, descreva riscos de CSS como hipóteses e proponha larguras a testar. Não afirme responsividade validada por ler media queries.

Controle versão do browser, SO/DPR, viewport, zoom, fontes carregadas, locale/fuso, animações, relógio/dados dinâmicos, rede e estado determinístico. Se algum controle estiver ausente, registre o efeito na comparação. Tolerância de pixels deve ter justificativa; não esconda diffs com máscaras amplas.

Use dados sintéticos. Antes de capturar/transmitir informações sensíveis, obtenha autorização; prefira estado sem dados sensíveis. Nunca sobrescreva baseline aprovado sem autorização específica. Atualizar baseline não demonstra correção. Sem baseline comparável, relate observações atuais, não uma “regressão comprovada”.

## Fallback utilizável

Entregue: motivo da indisponibilidade, observação estática com arquivo/símbolo, caso de teste, ambiente/viewport propostos, passos manuais, resultado esperado e evidência a coletar. Exemplo de roteiro: abrir estado sintético de checkout em larguras derivadas dos breakpoints; percorrer por Tab; submeter erro conhecido; verificar foco, overflow e mensagem; registrar console e captura local autorizada. Rotule tudo que não foi executado. Não é preciso instalar ferramentas para emitir esse relatório.
