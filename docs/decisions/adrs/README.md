# ADRs — Architecture Decision Records

Esta pasta reúne propostas de decisões arquiteturais para o Cultural AI Assistant. Todas as ADRs abaixo estão em estado de **proposta para revisão**: elas descrevem uma direção recomendada, mas ainda não devem ser tratadas como decisões definitivas.

## Como revisar

Para cada ADR, valide:

1. Se o problema está bem descrito.
2. Se a decisão proposta atende ao estágio atual do produto.
3. Se os trade-offs e alternativas são aceitáveis.
4. Se há alguma decisão relevante ausente.

Após aprovação, altere o status para `Aceita`. Se a decisão for substituída, marque a ADR anterior como `Substituída por ADR-XXX`; não a apague, para preservar o histórico.

## Índice

| ADR | Tema | Estado |
| --- | --- | --- |
| [ADR-001](ADR-001-fastapi.md) | Framework do backend: FastAPI | Proposta para revisão |
| [ADR-002](ADR-002-acesso-anonimo-no-mvp.md) | Acesso anônimo e autenticação pós-MVP | Proposta para revisão |
| [ADR-003](ADR-003-postgresql.md) | Banco de dados relacional: PostgreSQL | Proposta para revisão |
| [ADR-004](ADR-004-arquitetura-em-camadas.md) | Arquitetura em camadas no backend | Proposta para revisão |
| [ADR-005](ADR-005-react-vite-frontend.md) | Frontend em React com Vite | Proposta para revisão |
| [ADR-006](ADR-006-favoritos-temporarios.md) | Favoritos temporários para visitantes | Proposta para revisão |
| [ADR-007](ADR-007-fontes-de-eventos.md) | Fonte de eventos desacoplada por contrato | Proposta para revisão |
| [ADR-008](ADR-008-docker-desenvolvimento-local.md) | Docker para ambiente local | Proposta para revisão |
| [ADR-009](ADR-009-adiar-ia-e-multiagentes.md) | Adiar IA generativa e multiagentes | Proposta para revisão |
| [ADR-010](ADR-010-observabilidade-inicial.md) | Observabilidade inicial proporcional ao MVP | Proposta para revisão |

## Modelo adotado

Cada ADR contém: contexto, decisão proposta, motivação, consequências, alternativas e pontos a validar. Esse formato torna explícito o motivo de cada escolha e reduz ambiguidades em mudanças futuras.
