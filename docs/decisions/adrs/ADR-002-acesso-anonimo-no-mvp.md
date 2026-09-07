# ADR-002 — Manter acesso anônimo e adiar autenticação no MVP

- **Status:** Proposta para revisão
- **Data:** 2026-08-14

## Contexto

O objetivo da primeira fase é validar se uma pessoa encontra eventos próximos de forma simples e rápida. O PRD define dois fluxos: visitante no MVP e usuário autenticado em uma fase posterior.

## Decisão proposta

Permitir exploração, busca, filtros, detalhes e favoritos temporários **sem cadastro ou login** no MVP. Cadastro, login, recuperação de senha e notificações personalizadas ficam fora do escopo inicial.

## Motivação

- Reduz o escopo e a superfície de segurança da primeira entrega.
- Remove fricção para testar a descoberta de eventos.
- Direciona o esforço para a hipótese central: encontrar eventos relevantes.
- Evita implementar identidade, autorização e recuperação de senha antes de haver necessidade comprovada.

## Consequências

- Não haverá perfil persistente, recomendações individualizadas nem favoritos permanentes no MVP.
- Favoritos do visitante serão associados somente à sessão local/temporária.
- O modelo deve prever uma migração ou sincronização futura de favoritos após login.

## Alternativas consideradas

- Exigir conta antes da primeira busca.
- Implementar login social já no MVP.
- Permitir login opcional desde a primeira versão.

## Pontos para revisão

- Definir o prazo de expiração de uma sessão visitante.
- Definir se o favorito temporário será persistido no servidor, no navegador ou em ambos.
