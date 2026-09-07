# ADR-008 — Padronizar o ambiente local com Docker

- **Status:** Proposta para revisão
- **Data:** 2026-08-14
- **Decisores:** Responsável pelo projeto

## Contexto

O projeto usa serviços com dependências distintas, especialmente backend e PostgreSQL. A configuração manual de cada ambiente pode dificultar reprodução, onboarding e evolução para deploy.

## Decisão proposta

Usar **Docker** e Docker Compose para disponibilizar pelo menos o backend e o banco de dados no desenvolvimento local. O frontend pode ser containerizado conforme a necessidade, sem ser obrigatório no primeiro incremento.

## Motivação

- Reduz diferenças entre ambientes de desenvolvimento.
- Facilita subir e remover dependências locais de forma reproduzível.
- Aproxima o projeto de práticas de entrega e operação usadas no mercado.
- Cria uma base para CI e deploy posterior sem introduzir Kubernetes no MVP.

## Consequências

- Variáveis de ambiente, portas e volumes devem ser documentados.
- O repositório precisa manter arquivos de configuração de desenvolvimento sem segredos reais.
- O tempo de build e a experiência em máquinas locais devem ser monitorados para evitar complexidade desnecessária.

## Alternativas consideradas

- Executar tudo diretamente na máquina.
- Containerizar apenas o PostgreSQL.
- Adotar Kubernetes desde o início.

## Pontos para revisão

- Definir se o frontend entra no Compose inicial.
- Definir estratégia para dados de exemplo e reset do banco em desenvolvimento.
