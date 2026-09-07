# Documentation

This folder contains the project documentation and the architectural foundation for Cultural IA Assistant.

It is organized to make the product, domain, technical decisions, setup, and evolution easy to understand for developers, contributors, and reviewers.

## Documentation map

### Product and strategy
- [product/PRD.md](product/PRD.md) — product requirements document, business goals, MVP scope, and roadmap
- [product/vision.md](product/vision.md) — optional product vision summary if added later

### Architecture and technical modeling
- [architecture/initial-architecture.md](architecture/initial-architecture.md) — initial architecture proposal
- [architecture/technical-modeling.md](architecture/technical-modeling.md) — technical modeling and system boundaries
- [architecture/glossary.md](architecture/glossary.md) — core domain glossary

### API and contracts
- [api/contrato-api.md](api/contrato-api.md) — API contract and MVP resource definitions
- [api/openapi.json](api/openapi.json) — executable OpenAPI specification

### Data and modeling
- [modelagem-de-dados.md](modelagem-de-dados.md) — relational data model and MVP evolution
- [domain-model.excalidraw](domain-model.excalidraw) — editable domain model diagram
- [modelo-de-dados.excalidraw](modelo-de-dados.excalidraw) — editable data model diagram

### Design decisions
- [decisions/adrs/README.md](decisions/adrs/README.md) — ADR index and review process
- [decisions/adrs/ADR-001-fastapi.md](decisions/adrs/ADR-001-fastapi.md) — backend framework decision
- [decisions/adrs/ADR-002-acesso-anonimo-no-mvp.md](decisions/adrs/ADR-002-acesso-anonimo-no-mvp.md) — anonymous access strategy
- [decisions/adrs/ADR-003-postgresql.md](decisions/adrs/ADR-003-postgresql.md) — relational database choice
- [decisions/adrs/ADR-004-arquitetura-em-camadas.md](decisions/adrs/ADR-004-arquitetura-em-camadas.md) — layering strategy
- [decisions/adrs/ADR-005-react-vite-frontend.md](decisions/adrs/ADR-005-react-vite-frontend.md) — frontend stack choice
- [decisions/adrs/ADR-006-favoritos-temporarios.md](decisions/adrs/ADR-006-favoritos-temporarios.md) — temporary favorites approach
- [decisions/adrs/ADR-007-fontes-de-eventos.md](decisions/adrs/ADR-007-fontes-de-eventos.md) — event source abstraction
- [decisions/adrs/ADR-008-docker-desenvolvimento-local.md](decisions/adrs/ADR-008-docker-desenvolvimento-local.md) — local environment standardization
- [decisions/adrs/ADR-009-adiar-ia-e-multiagentes.md](decisions/adrs/ADR-009-adiar-ia-e-multiagentes.md) — AI and multi-agent deferral
- [decisions/adrs/ADR-010-observabilidade-inicial.md](decisions/adrs/ADR-010-observabilidade-inicial.md) — MVP observability strategy

### Setup and environment
- [setup/setup-backend-fastapi-docker.md](setup/setup-backend-fastapi-docker.md) — backend setup instructions
- [setup/setup-frontend-react.md](setup/setup-frontend-react.md) — frontend setup instructions
- [roadmap/roadmap-mensal.md](roadmap/roadmap-mensal.md) — roadmap and milestone planning

### Project organization and planning
- [organizacao_projeto.md](organizacao_projeto.md) — project organization recommendations and structure guidance
- [kanban.md](kanban.md) — task and delivery planning
- [backlog-semanal.md](backlog-semanal.md) — weekly backlog
- [git-flow-ci-cd-estudo.md](git-flow-ci-cd-estudo.md) — workflow and CI/CD study notes

### Diagrams and visual artifacts
- [diagrama-de-contexto.excalidraw](diagrama-de-contexto.excalidraw)
- [diagrama-de-containers.excalidraw](diagrama-de-containers.excalidraw)
- [diagrama-de-componentes.excalidraw](diagrama-de-componentes.excalidraw)
- [event-storming.excalidraw](event-storming.excalidraw)
- [event-storming.drawio](event-storming.drawio)
- [modelo-de-dados.excalidraw](modelo-de-dados.excalidraw)
- [domain-model.excalidraw](domain-model.excalidraw)

## Recommended reading order

If you are new to the project, this is the best order to read the documents:

1. [product/PRD.md](product/PRD.md)
2. [architecture/glossary.md](architecture/glossary.md)
3. [architecture/initial-architecture.md](architecture/initial-architecture.md)
4. [architecture/technical-modeling.md](architecture/technical-modeling.md)
5. [api/contrato-api.md](api/contrato-api.md)
6. [modelagem-de-dados.md](modelagem-de-dados.md)
7. [decisions/adrs/README.md](decisions/adrs/README.md)
8. [setup/setup-backend-fastapi-docker.md](setup/setup-backend-fastapi-docker.md)
9. [setup/setup-frontend-react.md](setup/setup-frontend-react.md)

## Purpose of this documentation

The documentation exists to keep the project understandable, reviewable, and extensible.

It captures:
- the problem and product vision;
- the MVP scope and future roadmap;
- the technical boundaries and architecture decisions;
- the API contract and data model;
- the setup path for local development.

## Documentation standards

This folder follows a review-friendly structure:
- documents are grouped by concern;
- ADRs explain the why behind each decision;
- diagrams are stored alongside the technical explanations;
- setup and implementation docs stay separated from product strategy.

## Suggested next step

Start with the product and architecture documents, then move to API and setup. That sequence gives the clearest picture of the product before implementation details.

---

This folder is the technical and product memory of the project. It should evolve together with the codebase and remain the place where decisions, trade-offs, and design intent are preserved.
