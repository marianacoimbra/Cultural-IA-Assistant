# ADR-003 — Usar PostgreSQL como banco de dados relacional

- **Status:** Proposta para revisão
- **Data:** 2026-08-14

## Contexto

O domínio possui entidades relacionadas, como eventos, localizações, categorias, favoritos, contas, perfis, interações e recomendações. O banco precisa atender o MVP e continuar viável para as próximas fases.

## Decisão proposta

Usar **PostgreSQL** como banco de dados relacional principal.

## Motivação

- Ampla adoção no mercado e boa documentação.
- Integridade referencial e consultas adequadas para o domínio relacional.
- Compatibilidade sólida com SQLAlchemy e FastAPI.
- Possibilidade de evolução para consultas geoespaciais, JSON e extensões como pgvector sem trocar de banco inicialmente.
- Facilidade de execução em Docker e provedores cloud.

## Consequências

- O esquema e as migrations passam a ser parte do código versionado.
- Será necessário definir estratégia de migrations e dados de desenvolvimento.
- Redis e vector store, quando existirem, serão complementares; não substituem a fonte de verdade relacional.

## Alternativas consideradas

- SQLite no MVP
- MongoDB
- Banco gerenciado sem esquema relacional

## Pontos para revisão

- Confirmar ORM e ferramenta de migration (por exemplo, SQLAlchemy e Alembic).
- Decidir em que fase consultas por distância exigirão PostGIS.
