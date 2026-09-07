# Modelagem de Dados

- **Status:** Proposta para revisão
- **Banco alvo:** PostgreSQL
- **Base de decisão:** [ADR-003 — PostgreSQL](adrs/ADR-003-postgresql.md), [Domain Model](domain-model.excalidraw) e [Glossário](glossario.md)

## Objetivo

Traduzir o domínio do Cultural AI Assistant em um modelo relacional que suporte o MVP de descoberta de eventos e evolua para personalização, recomendações e notificações sem redesenho estrutural.

O diagrama editável está em [modelo-de-dados.excalidraw](modelo-de-dados.excalidraw).

## Escopo por fase

| Fase | Tabelas | Finalidade |
| --- | --- | --- |
| MVP | `event_sources`, `events`, `locations`, `categories`, `event_categories`, `visitor_sessions`, `temporary_favorites` | Catálogo, busca, filtros e favoritos temporários para visitantes. |
| Pós-MVP | `users`, `cultural_profiles`, `interests`, `profile_interests`, `interactions`, `recommendations`, `notifications` | Conta, personalização, aprendizado de comportamento e comunicação relevante. |

## Relações principais

```text
event_sources 1 ── 0..* events
locations     1 ── 0..* events
events        N ── N categories       (via event_categories)
visitor_sessions 1 ── 0..* temporary_favorites
events        1 ── 0..* temporary_favorites

users         1 ── 1 cultural_profiles
cultural_profiles N ── N interests   (via profile_interests)
users         1 ── 0..* interactions ── 1 events
users         1 ── 0..* recommendations ── 1 events
recommendations 1 ── 0..* notifications
```

## Regras e restrições propostas

### Eventos e fontes

- `events.source_id` referencia uma fonte cadastrada em `event_sources`.
- A combinação `source_id + external_id` deve ser única para evitar duplicidade ao importar dados.
- Todo evento deve possuir uma localização, mas campos de endereço e coordenadas podem estar indisponíveis conforme a fonte.
- Uma categoria deve ter `slug` único e estável; eventos podem ter várias categorias.

### Sessões e favoritos do MVP

- `visitor_sessions` não deve armazenar dados pessoais no MVP.
- `temporary_favorites` deve ter a restrição única `(session_id, event_id)`.
- Favoritos temporários expiram quando a sessão expira e não representam favoritos permanentes de usuário.
- A política de limpeza de sessões e favoritos expirados precisa ser definida antes da implementação.

### Dados de personalização pós-MVP

- `cultural_profiles.user_id` é único: uma conta possui no máximo um perfil cultural.
- `profile_interests` permite registrar interesse declarado ou inferido pelo campo `source`; `weight` é opcional para ranking.
- `interactions.type` deve usar um conjunto controlado, por exemplo: `search`, `view`, `favorite`, `remove_favorite`, `positive_feedback` e `negative_feedback`.
- `recommendations` persiste a sugestão, seu `score`, a justificativa opcional e sua validade para auditoria e explicação futura.
- `notifications` registra tentativas e estado de entrega, sem armazenar o conteúdo completo quando não for necessário.

## Índices iniciais recomendados

| Tabela | Índice ou restrição | Motivo |
| --- | --- | --- |
| `event_sources` | `UNIQUE(name)` | Identificar cada integração. |
| `events` | `UNIQUE(source_id, external_id)` | Evitar eventos duplicados da mesma origem. |
| `events` | `(starts_at)` | Consultar eventos por data. |
| `events` | `(location_id)` | Filtrar e relacionar por localização. |
| `categories` | `UNIQUE(slug)` | Usar categoria como identificador estável. |
| `event_categories` | `PRIMARY KEY(event_id, category_id)` | Evitar categoria duplicada no mesmo evento. |
| `temporary_favorites` | `UNIQUE(session_id, event_id)` | Evitar favorito duplicado por sessão. |
| `interactions` | `(user_id, occurred_at DESC)` | Consultar histórico do usuário. |
| `recommendations` | `(user_id, generated_at DESC)` | Consultar recomendações recentes. |

## Decisões a revisar antes de implementar

1. Os eventos normalizados serão persistidos no PostgreSQL, consultados sob demanda, ou ambos?
2. O MVP precisa de busca textual no banco ou a busca inicial ocorre na fonte externa?
3. Distância geográfica será calculada com latitude/longitude simples ou exigirá PostGIS já na primeira fase?
4. A sessão visitante ficará somente no navegador, no backend, ou em estratégia híbrida?
5. Quais campos de dados externos podem ser armazenados de acordo com a licença de cada fonte?
