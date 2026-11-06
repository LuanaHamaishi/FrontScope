# Svelte: leitura condicional

Confirme versão e modo de reatividade (legado ou runes), escopo de compilação e SSR quando aplicável. Siga props, estado derivado, efeitos e eventos conforme esse modo; semânticas de atribuição e APIs variam. Analise cleanup e diferenças entre inicialização no servidor e no browser antes de concluir defeito.

Módulos locais podem isolar cálculo ou integração para um consumidor. Não promova estado por instância a estado de módulo compartilhado inadvertidamente, sobretudo com SSR. Não recomende memoização/hooks de React nem migração de modo como refatoração automática.
