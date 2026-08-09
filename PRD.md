# Product Requirements Document (PRD)

## Projeto

Cultural AI Assistant

## Autor

Mariana Victoria

## Status

Discovery / MVP Definition

## Versão

1.0

---

# 1. Visão

Criar uma plataforma inteligente capaz de recomendar eventos, shows, apresentações artísticas, experiências culturais e atividades de lazer próximas ao usuário utilizando inteligência artificial, sistemas multiagentes e mecanismos de personalização.

A experiência do produto deve contemplar dois fluxos principais:

1. Fluxo casual / visitante: o usuário pode explorar a aplicação de forma esporádica, conhecer uma cidade ou descobrir eventos sem precisar criar conta.
2. Fluxo autenticado: o usuário pode fazer login somente após o MVP para que o sistema reconheça seu perfil, preferências e interesses, oferecendo recomendações mais relevantes e, em etapas posteriores, notificações periódicas sobre eventos próximos.

O projeto possui dois objetivos simultâneos:

1. Resolver um problema real de descoberta de eventos culturais.
2. Servir como laboratório de aprendizado avançado em Engenharia de Software, IA, DevOps, Segurança, Observabilidade e Arquitetura de Sistemas.

---

# 2. Problema

Atualmente existem diversas plataformas que listam eventos, porém elas apresentam algumas limitações:

* Grande volume de informações irrelevantes.
* Pouca personalização.
* Necessidade de múltiplas pesquisas.
* Falta de explicação sobre as recomendações.
* Pouca integração entre localização, orçamento, disponibilidade e interesses pessoais.

Além disso, a maioria dos sistemas utiliza IA apenas para geração de texto, sem explorar agentes especializados capazes de raciocinar sobre diferentes aspectos da decisão.

---

# 3. Oportunidade

Criar um assistente inteligente que:

* Descubra eventos próximos.
* Entenda preferências do usuário.
* Aprenda com interações anteriores.
* Explique recomendações.
* Monte roteiros completos.
* Considere orçamento e logística.
* Utilize agentes especializados para tomada de decisão.

---

# 4. Objetivos de Negócio

## Curto Prazo

Entregar um MVP funcional capaz de:

* Permitir exploração casual de eventos sem login.
* Buscar eventos.
* Filtrar por localização.
* Permitir favoritos básicos.

## Médio Prazo

Implementar recomendações inteligentes, com cadastro opcional e personalização baseada em perfil e interesses.

## Longo Prazo

Criar uma plataforma multiagente com memória, planejamento e personalização contínua.

---

# 5. Objetivos Técnicos

O projeto deverá permitir aprendizado prático em:

* Desenvolvimento Backend
* Desenvolvimento Frontend
* APIs
* Arquitetura de Software
* Banco de Dados
* DevOps
* SRE
* Observabilidade
* Segurança
* Inteligência Artificial
* Orquestração de Agentes
* RAG
* Infraestrutura Cloud Native

---

# 6. Público-Alvo

## Usuário Cultural

Pessoa interessada em:

* Shows
* Festivais
* Museus
* Teatro
* Eventos gastronômicos
* Exposições
* Feiras
* Eventos gratuitos

## Usuário Turista

Pessoa visitando uma cidade e buscando atividades relevantes próximas.

---

# 7. Escopo MVP

## Funcionalidades

### Acesso e Exploração

* Exploração casual sem necessidade de cadastro
* Busca por cidade, localização e contexto
* Experiência simples para conhecer a plataforma e descobrir eventos rapidamente

### Cadastro e Login

* Cadastro e login serão introduzidos apenas após o MVP, como evolução do produto
* Recuperação de senha pode ser considerada em uma etapa posterior

### Perfil e Personalização

* Preferências culturais
* Categorias favoritas
* Histórico de interações e comportamento de uso

### Eventos

* Listagem
* Busca
* Filtros
* Distância

### Favoritos

* Adicionar
* Remover
* Consultar
* Em modo casual, os favoritos podem funcionar como lista temporária e ser sincronizados após login, em uma fase futura

---

# 8. Fluxos de Uso

## Fluxo 1 — Uso Casual / Visitante

Objetivo:

Permitir que qualquer pessoa experimente a plataforma sem cadastro, para descobrir eventos e conhecer uma cidade de forma rápida e simples.

Características:

* Uso anônimo
* Busca por eventos próximos
* Filtros básicos
* Sem necessidade de histórico ou perfil persistido

## Fluxo 2 — Usuário Autenticado / Personalização Pós-MVP

Objetivo:

Permitir que o usuário faça login para que o sistema reconheça seu perfil, preferências e interesses, oferecendo recomendações mais relevantes e, em um estágio posterior, notificações periódicas sobre eventos próximos.

Características:

* Cadastro e login após o MVP
* Perfil de interesses
* Recomendação personalizada
* Notificações futuras com eventos relevantes

---

# 9. Fora do Escopo do MVP

Não desenvolver inicialmente:

* Agentes
* IA Generativa
* RAG
* Kubernetes
* Terraform
* Grafana
* Recomendações avançadas

Esses itens serão implementados posteriormente.

---

# 10. Roadmap Evolutivo

## Fase 1

Produto Funcional

Objetivo:

Usuário encontra eventos próximos em modo visitante.

Tecnologias:

* FastAPI
* PostgreSQL
* Docker

---

## Fase 2

Personalização

Objetivo:

Usuário pode criar conta e receber recomendações simples com base em perfil e interesses.

Tecnologias:

* Perfil
* Categorias
* Ranking

---

## Fase 3

IA Conversacional

Objetivo:

Usuário conversa com o sistema.

Tecnologias:

* LLM
* Prompt Engineering

---

## Fase 4

Sistema Multiagente

Objetivo:

Delegar decisões para agentes especializados.

Agentes:

* Event Agent
* Location Agent
* Preference Agent
* Recommendation Agent

Tecnologias:

* LangGraph

---

## Fase 5

Memória e Notificações

Objetivo:

Aprender continuamente e enviar notificações relevantes com base em contexto, preferências e histórico.

Tecnologias:

* Redis
* Vetor Store

---

## Fase 6

Observabilidade

Objetivo:

Monitorar todo o ecossistema.

Tecnologias:

* OpenTelemetry
* Prometheus
* Grafana
* Loki
* Tempo

---

## Fase 7

Segurança

Objetivo:

Implementar arquitetura DevSecOps.

Tecnologias:

* OAuth2
* OIDC
* RBAC
* Vault
* Trivy
* Semgrep

---

## Fase 8

Cloud Native

Objetivo:

Operação em ambiente distribuído.

Tecnologias:

* Kubernetes
* Helm
* Terraform
* ArgoCD

---

# 10. Arquitetura Alvo

Frontend

↓

API Gateway

↓

Orquestrador de Agentes

↓

Event Agent

Location Agent

Preference Agent

↓

Recommendation Agent

↓

Banco de Dados + Vetor Store + Redis

---

# 11. Métricas de Sucesso

## Produto

* Eventos consultados
* Favoritos criados
* Taxa de retorno do usuário

## IA

* Precisão das recomendações
* Feedback positivo

## Plataforma

* Latência
* Disponibilidade
* Erros por serviço

---

# 12. Objetivo de Portfólio

Ao final do projeto, o repositório deverá demonstrar competências em:

* Engenharia de Software
* Arquitetura
* APIs
* Inteligência Artificial
* Multiagentes
* DevOps
* SRE
* Observabilidade
* Segurança
* Kubernetes
* GitOps
* Cloud Native

O projeto deverá ser documentado como um estudo de caso completo, incluindo diagramas, ADRs, documentação técnica, decisões arquiteturais, dashboards, pipelines e evidências de operação em produção.
