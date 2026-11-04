# A3 — Garantia da Qualidade de Software · Grupo 2 · Demoblaze

Testes automatizados (Python + Selenium + pytest, padrão Page Objects) para o
case **Demoblaze (Product Store)**: https://www.demoblaze.com

Projeto construído a partir do kit inicial da disciplina (Prof. Leandro Negreiros).

## Estrutura

```
conftest.py              fixtures driver/base_url e print automático em falha (kit)
verificar_ambiente.py    confere Python, Selenium e Chrome no Demoblaze (kit)
pages/                   Page Objects: seletores e ações de cada tela
  base_page.py           esperas explícitas, alertas JavaScript, evidências
  signup_page.py         modal Sign up
  login_page.py          modal Log in
tests/
  dados.py               dados fictícios e gerador de usuário único
  test_cadastro_login.py fluxo 1: CT01, CT02...
evidencias/              prints gerados pelos testes
docs/                    modelo do relatório A3
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
| `HEADLESS=1 pytest` | roda sem abrir a janela (Windows: `set HEADLESS=1 && pytest`) |

Precisa do Google Chrome instalado; o Selenium baixa o driver sozinho.

## Casos de teste

| ID | Caso | Técnica | Automatizado |
|----|------|---------|--------------|
| CT01 | Cadastro com usuário novo mostra alerta de sucesso | PE (válida) | ✅ |
| CT02 | Cadastro com usuário já existente é recusado | PE (inválida) | ⏳ |
| CT03 | Login válido mostra "Welcome <usuário>" | PE (válida) | ⏳ |
| CT04 | Login com senha errada mostra alerta de erro | PE (inválida) | ⏳ |
| CT05 | Filtro por categoria mostra só produtos da categoria | PE | ⏳ |
| CT06 | Adicionar produto ao carrinho e conferir o total | — | ⏳ |
| CT07 | Compra com nome e cartão vazios é recusada | VL (0 caractere) | ⏳ |
| CT08 | Compra completa mostra a confirmação | — | ⏳ |

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
