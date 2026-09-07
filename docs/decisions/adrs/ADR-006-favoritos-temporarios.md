# ADR-006 — Modelar favoritos de visitante como temporários

- **Status:** Proposta para revisão
- **Data:** 2026-08-14
- **Decisores:** Responsável pelo projeto

## Contexto

O MVP deve permitir adicionar, remover e consultar favoritos, mas não terá autenticação nem perfil persistente. O PRD prevê sincronizar favoritos após login em uma fase futura.

## Decisão proposta

No modo visitante, tratar um favorito como um recurso temporário ligado a uma **sessão visitante**, e não como um favorito permanente de usuário.

## Motivação

- Preserva a funcionalidade de favoritos sem antecipar autenticação.
- Torna explícita a limitação de duração e propriedade dos dados.
- Evita confundir favorito temporário com dado persistente de uma conta.
- Cria uma ponte clara para sincronização após login.

## Consequências

- O modelo de domínio deve distinguir `FavoritoTemporário` de um futuro `FavoritoDoUsuário` ou suportar ambos por meio de um proprietário explícito.
- A interface deve comunicar quando os favoritos podem expirar.
- A futura sincronização deve definir regra para duplicidades e conflitos.

## Alternativas consideradas

- Salvar favoritos somente em `localStorage`.
- Não oferecer favoritos no MVP.
- Criar uma conta anônima invisível para cada visitante.

## Pontos para revisão

- Escolher a fonte de persistência inicial: navegador, backend ou estratégia híbrida.
- Definir se o visitante pode exportar ou compartilhar a lista antes do login.
