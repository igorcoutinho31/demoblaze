# A3 — Garantia da Qualidade de Software · Grupo 2 · Demoblaze

Testes automatizados (Python + Selenium + pytest, padrão Page Objects) para o
case **Demoblaze (Product Store)**: https://www.demoblaze.com

Projeto construído a partir do kit inicial da disciplina (Prof. Leandro Negreiros).

## Entregáveis

| Arquivo | O que é |
| --- | --- |
| `docs/Relatorio_A3_Grupo2.pdf` | Relatório final (também em `.docx`) |
| `docs/Slides_A3_Grupo2.pdf` | Slides da apresentação em PDF |
| `docs/slides/index.html` | Slides em HTML: abra no navegador e use ← → para navegar |
| `docs/slides/roteiro_de_fala.md` | Anotações de fala de cada slide |
| `evidencias/` | Prints salvos pelos testes |

## Estrutura

```
conftest.py              fixtures driver/base_url e print automático em falha (kit)
verificar_ambiente.py    confere Python, Selenium e Chrome no Demoblaze (kit)
pages/                   Page Objects: seletores e ações de cada tela
  base_page.py           esperas explícitas, alertas JavaScript, evidências
  signup_page.py         modal Sign up
  login_page.py          modal Log in
  catalogo_page.py       vitrine, categorias e página do produto
  carrinho_page.py       carrinho
  compra_page.py         modal Place Order
tests/
  dados.py               dados fictícios e gerador de usuário único
  test_cadastro_login.py fluxo 1: CT01 a CT04 e CT09
  test_catalogo_carrinho_compra.py  fluxos 2 e 3: CT05 a CT08, CT10 e CT11
  test_validacoes.py     validações que o site deveria ter: CT12 a CT14
evidencias/              prints gerados pelos testes
docs/                    relatório, slides e modelo do relatório A3
```

## Como rodar

```bash
python3 -m pip install -r requirements.txt
python3 verificar_ambiente.py     # deve mostrar AMBIENTE OK
python3 -m pytest
```

| Comando | Para quê |
| --- | --- |
| `python3 -m pytest` | roda todos os testes |
| `pytest tests/test_cadastro_login.py` | roda um arquivo |
| `pytest -k ct01` | roda testes cujo nome contém "ct01" |
| `pytest -m cadastro` | roda só os testes do fluxo de cadastro |
| `pytest -m validacao` | roda só os testes de validação (CT12 a CT14) |
| `pytest -m "not validacao"` | roda tudo menos as validações |
| `HEADLESS=1 pytest` | roda sem abrir a janela (Windows: `set HEADLESS=1 && pytest`) |

Precisa do Google Chrome instalado; o Selenium baixa o driver sozinho.

## Casos de teste

| ID | Caso | Técnica | Automatizado |
|----|------|---------|--------------|
| CT01 | Cadastro com usuário novo mostra alerta de sucesso | PE (válida) | ✅ |
| CT02 | Cadastro com usuário já existente é recusado | PE (inválida) | ✅ |
| CT03 | Login válido mostra "Welcome <usuário>" | PE (válida) | ✅ |
| CT04 | Login com senha errada mostra alerta de erro | PE (inválida) | ✅ |
| CT05 | Filtro por categoria mostra só produtos da categoria | PE | ✅ |
| CT06 | Adicionar produto ao carrinho e conferir o total | — | ✅ |
| CT07 | Compra com nome e cartão vazios é recusada | VL (0 caractere) | ✅ |
| CT08 | Compra completa mostra a confirmação | — | ✅ |
| CT09 | Login com usuário não cadastrado mostra erro | PE (inválida) | ✅ |
| CT10 | Página do produto mostra nome, preço, imagem e descrição | — | ✅ |
| CT11 | Remover produto do carrinho atualiza itens e total | — | ✅ |
| CT12 | Cadastro com senha de 7 caracteres é recusado | VL | ✅ |
| CT13 | Compra com cartão com letras é recusada | PE (inválida) | ✅ |
| CT14 | Compra com mês 13 é recusada | VL | ✅ |

CT12 a CT14 esperam que o site recuse dados inválidos. Se o site aceitar, o teste falha:
isso é um **defeito** e vai para o relatório (seção 4.1) com o print da pasta `evidencias/`.

## Checkpoints

| Data | Checkpoint |
|------|-----------|
| 04/11 | Primeiro teste rodando no Demoblaze e capítulo 1 iniciado |
| 11/11 | 8 casos especificados e 2 testes rodando |
| 18/11 | 5 testes rodando e defeitos registrados com evidência |
| 25/11 | Métricas, análise ética, relatório em rascunho e slides |
| 02/12 | Entrega (relatório PDF, projeto, slides) e demo de 10 min |

## Regras

Somente o site do case, sem testes de carga, apenas dados fictícios.
Teste que falha não se apaga: é um defeito e vai para o relatório.

**Declaração de uso de IA:** a adaptação do kit para o Demoblaze foi feita com
auxílio do Claude Code (Anthropic) e revisada pelo grupo.

## Problemas comuns

**`session not created: Chrome failed to start: crashed` / `DevToolsActivePort file doesn't exist`**
(o Chrome abre e fecha na hora). Tente, nesta ordem:

1. Feche todas as janelas do Chrome e rode de novo.
2. Desligue o sandbox (PowerShell): `$env:CI="1"; python3 -m pytest`
3. Rode sem janela: `$env:HEADLESS="1"; $env:CI="1"; python3 -m pytest`
4. Rode `python3 verificar_ambiente.py` e mostre a saída ao professor:
   pode ser bloqueio da rede/política do laboratório.

Para limpar as variáveis depois: `Remove-Item Env:CI, Env:HEADLESS`
