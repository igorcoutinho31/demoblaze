"""
Configuracao compartilhada pelos testes (o pytest carrega este arquivo sozinho).

- Cria e fecha o navegador para cada teste (fixture "driver").
- Tira um print da tela quando um teste falha (pasta "evidencias").

Variaveis de ambiente opcionais:
  BASE_URL  endereco do sistema (padrao: https://www.demoblaze.com)
  HEADLESS  use HEADLESS=1 para rodar sem abrir a janela do navegador
"""
import os
from datetime import datetime

import pytest
from selenium import webdriver

BASE_URL = os.getenv("BASE_URL", "https://www.demoblaze.com").rstrip("/")
PASTA_EVIDENCIAS = os.path.join(os.path.dirname(__file__), "evidencias")


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def driver():
    opcoes = webdriver.ChromeOptions()
    if os.getenv("HEADLESS") == "1":
        opcoes.add_argument("--headless=new")
    if os.getenv("CI") == "1":  # servidores/containers (ex.: GitHub Actions)
        opcoes.add_argument("--no-sandbox")
        opcoes.add_argument("--disable-dev-shm-usage")
    opcoes.add_argument("--window-size=1280,900")
    # Evita o aviso do Chrome de "senha vazada" que cobre a tela no cadastro/login
    opcoes.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    if os.getenv("CHROME_BINARY"):
        opcoes.binary_location = os.getenv("CHROME_BINARY")

    # O Selenium Manager baixa sozinho o driver compativel com o Chrome instalado.
    navegador = webdriver.Chrome(options=opcoes)
    navegador.implicitly_wait(2)
    yield navegador
    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Quando um teste falha, salva um print da tela como evidencia do defeito."""
    resultado = yield
    relatorio = resultado.get_result()
    if relatorio.when == "call" and relatorio.failed:
        navegador = item.funcargs.get("driver")
        if navegador:
            try:  # com alerta JavaScript aberto o print falha; fecha antes
                navegador.switch_to.alert.accept()
            except Exception:
                pass
            os.makedirs(PASTA_EVIDENCIAS, exist_ok=True)
            momento = datetime.now().strftime("%Y%m%d-%H%M%S")
            nome = "".join(c if c.isalnum() else "_" for c in item.name)
            navegador.save_screenshot(os.path.join(PASTA_EVIDENCIAS, f"{momento}_{nome}.png"))
