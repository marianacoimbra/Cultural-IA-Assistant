# ADR-009 — Adiar IA generativa, RAG e multiagentes para após o MVP

- **Status:** Proposta para revisão
- **Data:** 2026-08-14
- **Decisores:** Responsável pelo projeto

## Contexto

O produto tem visão de longo prazo com assistente conversacional, memória e agentes especializados. Contudo, o problema inicial é validar a descoberta de eventos e a experiência de navegação para visitantes.

## Decisão proposta

Não incluir LLMs, RAG, agentes especializados, vector store ou orquestração multiagente no MVP. A primeira evolução de personalização deve usar regras e ranking simples, antes de adicionar IA generativa.

## Motivação

- Mantém o MVP focado e mensurável.
- Reduz custo, variabilidade e complexidade operacional.
- Permite estabelecer dados, métricas e contratos de domínio antes de automatizações mais sofisticadas.
- Evita atribuir à IA um problema que busca, filtros e bom catálogo podem resolver inicialmente.

## Consequências

- Explicações do MVP devem ser determinísticas ou limitadas à informação disponível no evento.
- O design deve preservar extensibilidade, mas não criar abstrações de agentes sem uso concreto.
- As métricas de uso e favoritos serão insumos para decidir se e onde IA agrega valor.

## Alternativas consideradas

- Lançar um chatbot com LLM desde o MVP.
- Construir todos os agentes antes da interface de busca.
- Não planejar nenhuma evolução de IA.

## Pontos para revisão

- Definir o critério de entrada da Fase 2 (personalização simples).
- Definir quais métricas justificariam introduzir agentes na Fase 4.
