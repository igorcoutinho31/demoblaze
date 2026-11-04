# A3 — Garantia da Qualidade de Software · Grupo 2 · Demoblaze

Testes automatizados (Python + Selenium + pytest, padrão Page Objects) para o
case **Demoblaze (Product Store)** — https://www.demoblaze.com

## Estrutura

```
conftest.py          # BASE_URL, fixture do Chrome, print automático em falha
pages/               # Page Objects (seletores e ações de cada tela)
  base_page.py       # esperas explícitas, leitura de alertas JS
  signup_page.py     # modal Sign up
  login_page.py      # modal Log in
tests/
  dados.py           # dados fictícios / gerador de usuário único
  test_ct01_cadastro.py
evidencias/          # prints gerados pelos testes
```

## Como rodar

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate   |   Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt

pytest                                  # abre o Chrome
HEADLESS=1 pytest                       # sem abrir janela (Linux/Mac)
pytest --html=report.html --self-contained-html   # relatório HTML
```

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

## Regras

Somente o site do case, sem testes de carga, apenas dados fictícios.
Testes que falham permanecem no relatório.

**Declaração de uso de IA:** a estrutura inicial do projeto foi gerada com
auxílio do Claude Code (Anthropic) e revisada pelo grupo.
