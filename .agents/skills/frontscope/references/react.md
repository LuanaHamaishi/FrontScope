# React: leitura condicional

Confirme versão, runtime/SSR e convenções do projeto. Siga ownership de estado, props, identidade de elementos/keys e contratos de efeitos. Para suspeita de stale closure, corrida ou dependência ausente, mostre sequência de render/efeito que produz o erro e guards existentes. Observe cleanup e cancelamento; não suponha que toda execução duplicada em desenvolvimento ocorra em produção.

Hook local pode isolar um efeito/coordenar estado para um único consumidor. Uma função pura não precisa virar hook. Não prescreva Context, memo, useMemo ou useCallback sem fronteira/benefício concretos. Re-render isolado não prova gargalo; consulte evidência e versão antes de recomendar otimizações ou APIs.
