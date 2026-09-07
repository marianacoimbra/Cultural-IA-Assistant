# ADR-007 — Isolar fontes de eventos atrás de um contrato

- **Status:** Proposta para revisão
- **Data:** 2026-08-14
- **Decisores:** Responsável pelo projeto

## Contexto

O produto precisa encontrar eventos, mas o PRD não define uma fonte externa definitiva. Fontes diferentes podem ter formatos, licenças, limites de uso e cobertura geográfica distintos.

## Decisão proposta

Definir um contrato interno para busca e normalização de eventos, implementado inicialmente por dados mockados ou por um único adaptador de fonte. As rotas e services não devem depender do formato específico de um provedor.

## Motivação

- Permite validar a experiência antes de depender de uma integração externa.
- Evita acoplamento ao modelo de dados de um fornecedor.
- Facilita trocar ou combinar fontes no futuro.
- Concentra normalização de data, preço, localização e categoria em uma única fronteira.

## Consequências

- Será necessário manter um modelo canônico de `Evento`.
- Cada integração futura terá um adaptador e tratamento de falhas próprios.
- Cobertura e atualização de dados dependerão da fonte selecionada; isso não deve ser escondido pela interface.

## Alternativas consideradas

- Acoplar diretamente a API a um único provedor.
- Construir um catálogo manual antes de qualquer contrato.
- Agregar múltiplas fontes desde o primeiro sprint.

## Pontos para revisão

- Selecionar a primeira fonte de dados considerando licença, cobertura e disponibilidade de API.
- Definir se eventos normalizados serão armazenados localmente ou consultados sob demanda.
