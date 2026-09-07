# ADR-005 — Usar React com Vite no frontend

- **Status:** Proposta para revisão
- **Data:** 2026-08-14
- **Decisores:** Responsável pelo projeto

## Contexto

O frontend precisa suportar busca, filtros, listagem, detalhes e favoritos em uma experiência web rápida. O projeto também busca aprendizado prático em desenvolvimento frontend moderno.

## Decisão proposta

Usar **React com Vite** para o frontend web. Adotar TypeScript é recomendado, mas fica pendente de confirmação nesta ADR.

## Motivação

- Ecossistema consolidado para interfaces baseadas em componentes.
- Vite fornece ambiente de desenvolvimento leve e rápido.
- Integração simples com uma API REST FastAPI.
- Boa base para evolução de páginas, estado de filtros e fluxos autenticados posteriores.

## Consequências

- Componentes devem separar apresentação, acesso à API e estado de interface.
- Será necessário definir biblioteca de roteamento, estratégia de estado e padrão de estilos.
- A decisão não obriga uma biblioteca visual específica; Tailwind CSS continua opcional.

## Alternativas consideradas

- Next.js.
- Vue ou Angular.

## Pontos para revisão

- Confirmar TypeScript como padrão do projeto.
- Definir se SEO e renderização no servidor serão requisitos futuros que justifiquem Next.js.
