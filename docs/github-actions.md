# GitHub Actions

O repositório possui dois workflows em `.github/workflows`.

## CI

`CI` executa em cada `push` e em cada pull request. Seus jobs são independentes,
exceto pelo *smoke test*, que roda após a compilação:

1. **Sintaxe Python**: instala exatamente as dependências de `uv.lock` e compila
   todos os arquivos Python;
2. **Qualidade estática**: usa Ruff para encontrar problemas de estilo, imports
   inválidos ou não usados e erros simples;
3. **Aplicação inicializa**: sobe a API, sem acessar a Ticketmaster, e consulta
   `/healthcheck`. A chave usada é falsa e existe só para satisfazer a
   configuração na CI.
4. **Arquivos e segredos sensíveis**: rejeita arquivos `.env` versionados
   (somente `.env.example` é aceito) e usa Gitleaks para detectar senhas,
   tokens e chaves de API no código e no histórico disponível no checkout.

Ao detectar um segredo verdadeiro, remova-o do código e **revogue/rotacione-o**
no provedor de origem; removê-lo apenas em um commit posterior não o remove do
histórico Git.

## Releases

`Release` é manual, pois escolher `patch`, `minor` ou `major` é uma decisão de
produto. No GitHub, vá a **Actions > Release > Run workflow**, escolha a versão
e execute-o na branch `main`. Ele cria uma tag anotada, por exemplo `v0.2.0`.

| Escolha | Exemplo | Quando usar |
| --- | --- | --- |
| `patch` | `v0.2.0` → `v0.2.1` | Correção compatível |
| `minor` | `v0.2.0` → `v0.3.0` | Nova funcionalidade compatível |
| `major` | `v0.2.0` → `v1.0.0` | Mudança incompatível |

O workflow requer que o `GITHUB_TOKEN` tenha permissão **Contents: read and
write**. Caso a organização bloqueie essa permissão, habilite-a em **Settings >
Actions > General > Workflow permissions**. Se regras de proteção impedirem
tags, permita o padrão `v*` para o GitHub Actions.

## Próximos experimentos

- Adicionar `pytest` e uma cobertura mínima; o smoke test não substitui testes
  unitários e de integração.
- Executar `ruff format --check` para padronizar formatação.
- Validar OpenAPI e publicar a documentação como artefato.
- Adicionar CodeQL para análise de segurança.
- Criar uma imagem Docker e publicá-la no GitHub Container Registry após uma
  release.
- Usar ambientes (`staging` e `production`) com aprovação manual antes de
  deploys.
