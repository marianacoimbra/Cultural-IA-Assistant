# Arquitetura inicial proposta

## Visão geral

A arquitetura inicial será simples, modular e adequada para estudo e portfólio.

## Stack sugerida

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Docker

### Frontend

- React
- Vite
- TypeScript ou JavaScript
- Axios
- Tailwind CSS opcional

## Estrutura proposta

```text
backend/
  app/
    api/
    core/
    models/
    schemas/
    services/
frontend/
  src/
    components/
    pages/
    services/
    styles/
infra/
  docker/
```

## Fluxo principal

1. O usuário acessa a aplicação pelo frontend.
2. O frontend chama a API do backend.
3. O backend consulta o banco de dados.
4. O resultado é devolvido ao frontend e exibido ao usuário.

## Módulos iniciais

### Backend

- Autenticação
- Gestão de usuários
- CRUD de eventos
- Favoritos
- Busca e filtros

### Frontend

- Tela de login
- Tela de cadastro
- Listagem de eventos
- Tela de detalhes
- Perfil de preferências

## Prioridade de implementação

1. Backend com endpoints básicos
2. Frontend com fluxo de cadastro e visualização
3. Favoritos e perfis
4. Melhorias visuais e documentação

## Objetivo arquitetural

Manter a solução simples, mas com organização suficiente para demonstrar boas decisões técnicas sem overcomplicar o projeto.
