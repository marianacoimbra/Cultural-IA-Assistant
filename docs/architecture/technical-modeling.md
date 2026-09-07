# Technical Modeling

## Objective

Translate the Cultural AI Assistant domain into an understandable, evolvable software solution aligned with the MVP scope.

### Little personal Journal
While trying to build and develop this project, I faced a lot of difficulties when it came to answer the questions: 
- Where do I start?
- What do I actually write here?
- Does this makes sense?

So I decided to take some steps back..

So, I decided to first reserch for the best techniques and tools to answer those questions echoing in my head.

My biggest desire was to bring a real value with this Idea, right? So..

Here come the questions that really matters:
- Who will use my app?
People interested in culture and social events—yet too tired to keep up with every media outlet and event announcement—who have specific tastes but are bombarded daily with numerous ads that do not align with their personal preferences or financial circumstances.
Primarily people living in large metropolitan areas where there are many events and extensive promotion of them, or people visiting new places who want to find—in one central location—the options that best match their profile.

- What happens from the begginning to the end

- What components exists?
- How the data talks within itself? (how it flows)

## Artifacts

| Artifact | Purpose | Status |
| --- | --- | --- |
| [Context Diagram](context-diagram.excalidraw) | Show the high-level relationships between the User, Cultural AI Assistant, and Event Sources. | Created |
| [Container Diagram](containers-diagram.excalidraw) | Show the frontend, FastAPI API, PostgreSQL, and future LLM. | Created |
| [Component Diagram](components-diagram.excalidraw) | Detail the API, services, repositories, adapters, and external dependencies. | Created |
| [Data Model](../data/modelagem-de-dados.md) | Translate domain entities into tables, keys, relationships, and constraints. | Created |
| [API Contract](../api/contrato-api.md) | Define endpoints, input and output schemas, errors, and versioning. | Created |

## Context Diagram

The context diagram uses a simplified C4 view and establishes the main boundaries:

```text
Usuário
  ↓ searches, filters, and favorites events
Cultural AI Assistant
  ↓ queries and normalizes data
Event Sources
```

### Responsibilities

| Element | Responsibility |
| --- | --- |
| User | Explores cultural events and interacts with search, filters, details, and favorites. |
| Cultural AI Assistant | Provides the discovery experience; coordinates search, filtering, normalization, and event presentation. |
| Event Sources | Provide external event data, such as descriptions, dates, locations, prices, and availability. |

## Artifact Boundaries

The diagram does not detail the internal implementation. The database, frontend, FastAPI, services, repositories, and future authentication mechanisms belong to the next modeling levels.

## Container Diagram

The C4 container diagram details the main technical building blocks:

```text
Usuário
  ↓ HTTPS
Frontend Web (React + Vite)
  ↓ REST / JSON
Backend / API (FastAPI)
  ├─→ PostgreSQL via SQL
  └─→ LLM via API — pós-MVP
```

The LLM is an external system planned for future evolution and is called by the backend. It is not accessed by PostgreSQL.

## Component Diagram

The diagram details the interior of the Backend/API container and implements the layered architecture defined in [ADR-004](adrs/ADR-004-arquitetura-em-camadas.md):

```text
API Routers → Services → Repositories → PostgreSQL
                    └→ Event Source Adapter → Fonte de Eventos
                    └→ Profile & Recommendation Service → LLM (pós-MVP)
```

The event discovery and favorites components are part of the MVP. Profile, recommendation, and LLM integration are highlighted as post-MVP evolution.

## Data Model

The proposed relational model uses PostgreSQL and explicitly separates the MVP from future personalization entities. See the [data specification](modelagem-de-dados.md) and the [editable diagram](modelo-de-dados.excalidraw) for the tables, keys, and integrity rules.

## API Contract

The contract was defined in OpenAPI 3.1.0, with discovery and temporary favorites features in the MVP and authenticated features reserved for later phases. See the [reader-friendly view](contrato-api.md) and the [OpenAPI specification](openapi.json).
