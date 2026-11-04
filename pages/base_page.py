from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

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

    def screenshot(self, caminho):
        self.driver.save_screenshot(str(caminho))
