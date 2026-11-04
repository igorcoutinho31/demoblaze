import os
from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver

BASE_URL = "https://www.demoblaze.com"
EVIDENCIAS_DIR = Path(__file__).parent / "evidencias"


@pytest.fixture
def driver():
    """Abre o Chrome, entrega o driver ao teste e fecha ao final.

    Para rodar sem abrir janela: HEADLESS=1 pytest
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1366,900")
    if os.getenv("HEADLESS") == "1":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(0)  # usamos apenas esperas explícitas (WebDriverWait)
    drv.get(BASE_URL)
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Salva um print em evidencias/ sempre que um teste falhar."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv is not None:
            EVIDENCIAS_DIR.mkdir(exist_ok=True)
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            arquivo = EVIDENCIAS_DIR / f"FALHA_{item.name}_{stamp}.png"
            try:
                drv.switch_to.alert.accept()  # print não sai com alerta aberto
            except Exception:
                pass
            drv.save_screenshot(str(arquivo))
