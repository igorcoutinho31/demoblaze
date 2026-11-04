"""Base dos Page Objects: esperas explícitas e leitura de alertas JavaScript."""
import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PASTA_EVIDENCIAS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "evidencias")


class BasePage:
    TIMEOUT = 10

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def abrir_site(self):
        self.driver.get(self.base_url + "/")
        return self

    def clicar(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def digitar(self, locator, texto):
        campo = self.wait.until(EC.visibility_of_element_located(locator))
        campo.clear()
        campo.send_keys(texto)

    def texto_de(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def esperar_visivel(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def ler_alerta_e_aceitar(self, timeout=5):
        """Espera o alerta JavaScript, devolve o texto dele e clica em OK."""
        alerta = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        texto = alerta.text
        alerta.accept()
        return texto

    def salvar_evidencia(self, nome):
        """Salva um print em evidencias/<nome>.png (útil também quando o teste passa)."""
        os.makedirs(PASTA_EVIDENCIAS, exist_ok=True)
        self.driver.save_screenshot(os.path.join(PASTA_EVIDENCIAS, f"{nome}.png"))
