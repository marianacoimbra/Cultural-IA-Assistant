# Kanban de Desenvolvimento - Cultural IA Assistant

## Objetivo

Construir um MVP funcional para estudo e portfólio, priorizando um produto simples, bem documentado e demonstrável.

## Estratégia

- Focar no fluxo principal: cadastro, autenticação, busca de eventos, favoritos e interface.
- Entregar valor de forma incremental.
- Garantir que cada etapa gere algo demonstrável para o portfólio.
- Documentar decisões técnicas e resultados ao longo do processo.

---

## Fases do projeto

### Fase 0 - Planejamento e base

Objetivo: definir a base do projeto e reduzir risco de rework.

- [ ] Definir escopo do MVP e critérios de aceite
- [ ] Definir stack principal (ex.: FastAPI + PostgreSQL + React/Vite + Docker)
- [ ] Criar estrutura inicial de pastas do backend, frontend e infraestrutura
- [ ] Definir modelo de domínio: usuário, evento, favorito, perfil
- [ ] Escrever README inicial com setup, arquitetura e objetivos
- [ ] Criar ambiente local com Docker Compose

### Fase 1 - Backend MVP

Objetivo: construir a API principal e a lógica de negócio do produto.

- [ ] Configurar projeto backend
- [ ] Criar banco de dados e migrações
- [ ] Implementar autenticação básica (registro, login, recuperação de senha)
- [ ] Criar modelos de usuário, evento, favorito e preferência
- [ ] Implementar endpoints de CRUD para eventos
- [ ] Implementar busca e filtros por localização, categoria e data
- [ ] Implementar endpoints de favoritos
- [ ] Criar documentação da API (Swagger / Redoc)
- [ ] Adicionar testes unitários e de integração básicos

### Fase 2 - Frontend MVP

Objetivo: transformar a API em uma experiência usable para o usuário.

- [ ] Configurar projeto frontend
- [ ] Criar layout base da aplicação
- [ ] Implementar tela de cadastro e login
- [ ] Implementar tela de listagem de eventos
- [ ] Implementar filtros e busca
- [ ] Implementar tela de detalhes do evento
- [ ] Implementar favoritos no frontend
- [ ] Implementar perfil de preferências do usuário
- [ ] Criar navegação entre páginas e estados de carregamento/erro

### Fase 3 - Qualidade e confiabilidade

Objetivo: deixar o projeto mais robusto e profissional.

- [ ] Adicionar testes no frontend
- [ ] Configurar linting e formatação
- [ ] Configurar CI para testes automáticos
- [ ] Adicionar tratamento de erros e validações
- [ ] Implementar logs básicos e observabilidade
- [ ] Criar ambiente de staging ou preview
- [ ] Revisar segurança básica (senhas, tokens, validações)

### Fase 4 - Portfólio e divulgação

Objetivo: transformar o projeto em um material forte para demonstrar habilidades.

- [ ] Criar demo funcional localmente
- [ ] Tirar screenshots da aplicação
- [ ] Melhorar README com arquitetura, decisões e aprendizados
- [ ] Documentar fluxo de uso e funcionalidades principais
- [ ] Preparar deploy público ou demo acessível
- [ ] Organizar repositório com estrutura limpa e commits bem descritos

### Fase 5 - Evolução futura

Objetivo: expandir o projeto além do MVP com foco em aprendizado.

- [ ] Implementar recomendações simples com ranking
- [ ] Integrar IA generativa para explicação de recomendações
- [ ] Explorar agentes especializados
- [ ] Implementar cache e busca mais avançada
- [ ] Adicionar memória de preferências e contexto do usuário

---

## Quadro Kanban sugerido

### Backlog

- [ ] Definir escopo do MVP
- [ ] Escolher stack técnico
- [ ] Planejar modelo de dados
- [ ] Criar documentação inicial

### A fazer

- [ ] Configurar ambiente local
- [ ] Implementar autenticação
- [ ] Construir API de eventos
- [ ] Criar frontend inicial
- [ ] Implementar favoritos e perfil

### Em andamento

- [ ] Nenhuma tarefa iniciada ainda

### Concluído

- [ ] Nenhuma tarefa concluída ainda

---

## Entregas recomendadas por sprint

### Sprint 1

- Estrutura do repositório
- Ambiente Docker
- Banco de dados e modelos básicos

### Sprint 2

- Autenticação
- Endpoints de eventos
- Listagem no frontend

### Sprint 3

- Favoritos
- Perfil de preferências
- Testes básicos

### Sprint 4

- Polimento visual
- Documentação
- Deploy demo

---

## Critérios de sucesso para o MVP

O MVP estará pronto quando for possível:

- cadastrar e autenticar um usuário
- buscar eventos
- filtrar eventos por contexto relevante
- salvar favoritos
- demonstrar a aplicação de forma clara em uma demo
