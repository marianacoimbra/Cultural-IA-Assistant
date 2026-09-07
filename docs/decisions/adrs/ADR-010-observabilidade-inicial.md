# ADR-010 — Adotar observabilidade inicial proporcional ao MVP

- **Status:** Proposta para revisão
- **Data:** 2026-08-14
- **Decisores:** Responsável pelo projeto

## Contexto

O projeto prevê OpenTelemetry, Prometheus, Grafana, Loki e Tempo em fases futuras. Mesmo no MVP, erros e comportamento básico da API precisam ser visíveis, mas a pilha completa de observabilidade não deve bloquear a entrega.

## Decisão proposta

No MVP, implementar logs estruturados, correlação básica por requisição, endpoint de saúde e tratamento consistente de erros. Adiar coleta distribuída, dashboards e stack completa de métricas para a fase de observabilidade.

## Motivação

- Oferece diagnóstico mínimo viável desde o início.
- Mantém a operação proporcional à complexidade do produto.
- Cria convenções de logs que podem ser exportadas posteriormente para ferramentas de observabilidade.
- Evita instalar uma plataforma operacional extensa sem tráfego ou serviços distribuídos.

## Consequências

- Logs não podem conter credenciais nem dados pessoais desnecessários.
- A API deve expor uma verificação de saúde simples.
- Métricas formais de latência, disponibilidade e erro serão incorporadas em uma ADR futura quando a infraestrutura justificar.

## Alternativas consideradas

- Não implementar nenhum mecanismo de observabilidade no MVP.
- Adotar toda a stack OpenTelemetry + Prometheus + Grafana desde o início.
- Usar somente logs informais no console.

## Pontos para revisão

- Definir o formato de logs e o identificador de correlação.
- Definir se métricas mínimas de contagem e latência entram ainda no MVP.
