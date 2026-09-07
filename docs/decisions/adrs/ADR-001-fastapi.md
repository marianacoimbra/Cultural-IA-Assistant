# ADR-001 — Usar FastAPI no backend

- **Status:** Proposta para revisão
- **Data:** 2026-08-14

## Contexto

O MVP precisa expor uma API HTTP para busca, filtros, detalhes de eventos e favoritos temporários. O projeto também tem objetivo educacional em APIs, tipagem, validação, documentação e arquitetura de software.

## Decisão proposta

Usar **Python com FastAPI** como framework principal do backend.

## Motivação

- Tipagem e validação de contratos com Pydantic.
- Documentação interativa automática via OpenAPI/Swagger.
- Boa adequação a APIs assíncronas e integração futura com IA.
- Curva de aprendizado compatível com o objetivo de portfólio.
- Ecossistema maduro para testes, banco de dados e autenticação futura.

## Consequências

- Endpoints devem usar schemas de entrada e saída explícitos.
- A documentação da API será derivada dos contratos, não mantida manualmente em duplicidade.
- A equipe precisará definir convenções para async, tratamento de erro e injeção de dependências quando o backend crescer.

## Alternativas consideradas

- Flask
- Django REST Framework
- Node.js com Express ou NestJS

## Pontos para revisão

- Confirmar se o backend será integralmente assíncrono ou se o MVP pode usar operações síncronas onde isso simplificar a implementação.
- Definir a versão mínima de Python suportada.
