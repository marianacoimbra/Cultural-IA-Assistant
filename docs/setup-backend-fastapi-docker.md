# Setup do backend com FastAPI e Docker

## Objetivo do bloco

Criar uma base sólida de backend para o projeto, usando FastAPI para a API e Docker para isolar o ambiente de execução. Esse setup serve como ponto de partida para aprender arquitetura de APIs, containers e desenvolvimento profissional.

## Por que fazer isso primeiro

- O backend é a espinha dorsal do projeto.
- FastAPI permite aprender uma stack moderna, limpa e bem adotada no mercado.
- Docker ajuda a reproduzir o ambiente de forma consistente, evitando problemas entre máquinas diferentes.
- Esse setup cria uma base reutilizável para futuras features como autenticação, eventos e favoritos.

---

## Bloco 1 — Entender a proposta

### O que fazer

- Ler o objetivo do projeto e o escopo do MVP.
- Definir o que a API precisa fazer no início.
- Identificar os primeiros endpoints: saúde da aplicação, cadastro, login e eventos.

### Por que isso é importante

Sem clareza sobre o escopo, o desenvolvimento pode ficar disperso. Essa etapa ajuda a aprender a transformar requisitos em uma arquitetura inicial.

### Entregável

Uma lista simples de endpoints e responsabilidades da API.

---

## Bloco 2 — Preparar o ambiente local

### O que fazer

- Instalar Python.
- Criar um ambiente virtual.
- Instalar FastAPI, Uvicorn e outras dependências mínimas.
- Instalar Docker e Docker Compose.

### Por que isso é importante

Essa etapa ensina boas práticas de desenvolvimento: ambientes isolados e reprodutibilidade.

### Entregável

Ambiente local preparado para rodar a aplicação.

---

## Bloco 3 — Criar a aplicação FastAPI inicial

### O que fazer

- Criar um projeto mínimo com FastAPI.
- Criar uma rota de teste como /health.
- Rodar a aplicação localmente.

### Por que isso é importante

Você aprende a estrutura básica de uma API moderna, o ciclo de execução e como validar o funcionamento do servidor.

### Entregável

Uma API respondendo em localhost com uma rota simples.

---

## Bloco 4 — Organizar a estrutura do backend

### O que fazer

- Separar o código em pastas como app, api, models, schemas e services.
- Criar arquivos para organização inicial.
- Definir onde ficará a configuração da aplicação.

### Por que isso é importante

Aprender organização de código é essencial para projetos crescerem sem virar um caos. Isso também melhora muito a leitura do projeto em portfólio.

### Entregável

Estrutura limpa do backend, mesmo que simples.

---

## Bloco 5 — Criar o container com Docker

### O que fazer

- Criar um Dockerfile para o backend.
- Criar um docker-compose.yml para subir o serviço.
- Configurar a aplicação para rodar dentro do container.

### Por que isso é importante

Docker é uma habilidade muito valorizada. Aprender isso agora ajuda a entender ambientes de produção e implantação.

### Entregável

O backend rodando via Docker.

---

## Bloco 6 — Conectar com banco de dados

### O que fazer

- Adicionar PostgreSQL ao ambiente.
- Configurar conexão com o banco.
- Criar o primeiro modelo simples, como usuário ou evento.

### Por que isso é importante

A maioria das aplicações reais depende de banco de dados. Essa etapa ensina o fluxo completo entre API, aplicação e persistência.

### Entregável

Aplicação conectada a um banco de dados local.

---

## Bloco 7 — Testar e documentar

### O que fazer

- Validar endpoints com requests ou Swagger.
- Verificar se a documentação automática do FastAPI funciona.
- Registrar comandos de execução no README.

### Por que isso é importante

Aprender a validar e documentar o trabalho é fundamental para manter qualidade e demonstrar profissionalismo.

### Entregável

API funcional, documentada e com instruções claras.

---

## Sequência recomendada

1. Entender a proposta
2. Preparar o ambiente
3. Criar a API mínima
4. Organizar o projeto
5. Criar o Dockerfile
6. Subir com Docker Compose
7. Conectar ao banco
8. Testar e documentar

## Resultado esperado

Ao final desse bloco, você terá um backend com FastAPI rodando em container, com base para evoluir para autenticação, eventos e integração com o frontend.
