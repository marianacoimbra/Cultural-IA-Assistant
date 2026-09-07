# ADR-004 — Organizar o backend em arquitetura em camadas

- **Status:** Proposta para revisão
- **Data:** 2026-08-14

## Contexto

O projeto precisa manter endpoints simples, regras de negócio testáveis e acesso a dados isolado, sem adotar uma arquitetura excessivamente complexa antes de existir produto funcional.

## Decisão proposta

Estruturar o backend nas camadas abaixo:

```text
API
 ↓
Services
 ↓
Repositories
 ↓
Banco de dados / fontes externas
```

Schemas Pydantic ficam na fronteira da API; modelos ORM pertencem à infraestrutura de persistência; `core/` concentra configuração, logging e dependências compartilhadas.

## Motivação

- Separa HTTP, regras de negócio e persistência.
- Facilita testes unitários de services e testes de integração de repositories.
- Mantém a estrutura reconhecível e compatível com FastAPI.
- Permite adicionar fontes externas e agentes futuros sem acoplar esses detalhes às rotas.

## Consequências

- Rotas não devem conter regras de negócio nem consultas SQL diretas.
- Services não devem depender de detalhes de HTTP.
- Repositories são introduzidos quando houver persistência real; mocks simples podem ser usados durante o protótipo.

## Alternativas consideradas

- Código concentrado diretamente nos endpoints.
- Clean Architecture ou Hexagonal completa desde o início.
- Organização apenas por tipo técnico, sem services.

## Pontos para revisão

- Definir quando um módulo deve deixar de ser simples o suficiente para justificar um repository.
- Definir se a organização de pastas será por camada, por domínio, ou híbrida quando o produto crescer.
