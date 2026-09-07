# Contrato de API

- **Status:** Proposta para revisão
- **Especificação executável:** [openapi.json](openapi.json)
- **Formato:** OpenAPI 3.1.0
- **Versão-base proposta:** `/api/v1`

## Objetivo

Definir o contrato entre frontend e backend antes da implementação completa. O contrato esclarece recursos, parâmetros, corpos de requisição, respostas, erros e a separação entre o MVP visitante e a evolução autenticada.

O arquivo [openapi.json](openapi.json) é a fonte de verdade para geração de documentação interativa, clientes e testes de contrato quando a API for implementada.

## Convenções

| Convenção | Definição |
| --- | --- |
| Base URL | `/api/v1` é proposta para o contrato público. |
| Formato | Requisições e respostas usam `application/json`. |
| Nomes | API expõe propriedades em `camelCase`; banco de dados usa `snake_case`. |
| Datas | ISO 8601 com timezone, por exemplo `2026-08-14T18:30:00Z`. |
| IDs | UUIDs gerados pelo sistema. |
| Paginação | `page` começa em `1`; `pageSize` varia de `1` a `50`. |
| Erros | `application/problem+json`, com `type`, `title`, `status`, `detail` e erros de campo quando aplicável. |

## Recursos do MVP

| Método | Rota | Finalidade |
| --- | --- | --- |
| `GET` | `/health` | Verificar disponibilidade da API. |
| `GET` | `/events` | Buscar e filtrar eventos. |
| `GET` | `/events/{eventId}` | Consultar detalhes de um evento. |
| `GET` | `/categories` | Listar categorias ativas. |
| `POST` | `/visitor-sessions` | Criar sessão anônima. |
| `GET` | `/visitor-sessions/{sessionId}/favorites` | Consultar favoritos temporários. |
| `POST` | `/visitor-sessions/{sessionId}/favorites` | Adicionar favorito temporário. |
| `DELETE` | `/visitor-sessions/{sessionId}/favorites/{eventId}` | Remover favorito temporário. |

### Busca de eventos

`GET /events` aceita os seguintes filtros opcionais: `q`, `city`, `category`, `latitude`, `longitude`, `radiusKm`, `startsAt`, `endsAt`, `maxPrice` e `sort`.

Regras propostas:

- `latitude` e `longitude` devem ser enviados juntos.
- `radiusKm` só pode ser usado com latitude e longitude.
- `startsAt` não pode ser posterior a `endsAt`.
- `category` é o `slug` estável da categoria, não seu nome de exibição.
- Quando localização não estiver disponível, a API não deve inventar `distanceKm`.

### Favoritos temporários

O `sessionId` identifica a sessão visitante e não substitui uma conta. O mesmo evento não pode ser adicionado duas vezes na mesma sessão; nesse caso, a API retorna `409 Conflict`.

## Recursos pós-MVP

Essas rotas estão especificadas para orientar a evolução, mas não devem ser implementadas no MVP:

| Método | Rota | Finalidade |
| --- | --- | --- |
| `POST` | `/auth/register` | Criar uma conta. |
| `POST` | `/auth/login` | Obter token de acesso. |
| `GET` / `PUT` | `/me/profile` | Consultar ou atualizar perfil cultural. |
| `POST` | `/me/interactions` | Registrar interação que alimenta personalização. |
| `GET` | `/me/recommendations` | Consultar recomendações personalizadas. |

Essas rotas exigem `Authorization: Bearer <token>`. A escolha final de provedor, fluxo de token e mecanismos como OAuth2/OIDC deve receber ADR própria antes da implementação.

## Situação do código atual

O backend atual contém endpoints de protótipo (`/healthcheck`, `/mock/profile`, `/mock/recommendations` e `/profile/interpret`) que não correspondem ainda ao contrato alvo. Eles não foram alterados neste artefato.

O trabalho de implementação posterior deve:

1. Adotar o prefixo e os schemas definidos pelo contrato.
2. Substituir mocks por recursos de domínio (`events`, `categories`, sessões e favoritos).
3. Atualizar a configuração FastAPI para expor esta especificação em `/openapi.json` e documentação em `/docs`.
4. Implementar testes de contrato para os endpoints do MVP.

## Pontos para revisão

1. O prefixo público `/api/v1` deve ser adotado agora ou somente quando houver consumidores externos?
2. A primeira fonte de eventos aceita os filtros definidos diretamente ou o backend precisará filtrá-los após normalização?
3. Sessões visitantes devem usar o ID na URL, cookie `HttpOnly`, ou ambos?
4. O payload de favoritos deve retornar o evento completo, como proposto, ou apenas `eventId`?
5. O fluxo de autenticação pós-MVP será credencial própria, OAuth2/OIDC, login social, ou uma combinação?
