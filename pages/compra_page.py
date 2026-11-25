"""Page Object da finalização da compra (modal Place Order)."""
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class CompraPage(BasePage):
    MODAL = (By.ID, "orderModal")

    NOME = (By.ID, "name")
    PAIS = (By.ID, "country")
    CIDADE = (By.ID, "city")
    CARTAO = (By.ID, "card")
    MES = (By.ID, "month")
    ANO = (By.ID, "year")

    BOTAO_COMPRAR = (By.CSS_SELECTOR, "#orderModal button[onclick='purchaseOrder()']")

    CONFIRMACAO = (By.CSS_SELECTOR, ".sweet-alert h2")
    BOTAO_OK = (By.CSS_SELECTOR, ".sweet-alert button.confirm")

    def aguardar_modal(self):
        self.esperar_visivel(self.MODAL)
        return self

    def preencher_dados(self, nome, pais, cidade, cartao, mes, ano):
        self.digitar(self.NOME, nome)
        self.digitar(self.PAIS, pais)
        self.digitar(self.CIDADE, cidade)
        self.digitar(self.CARTAO, cartao)
        self.digitar(self.MES, mes)
        self.digitar(self.ANO, ano)

    def confirmar(self):
        self.clicar(self.BOTAO_COMPRAR)

    def comprar_sem_dados(self):
        """Clica em 'Purchase' sem preencher nada e devolve o texto do alerta."""
        self.clicar(self.BOTAO_COMPRAR)
        return self.ler_alerta_e_aceitar()

    def resultado_da_compra(self, timeout=10):
        """Depois de clicar em 'Purchase', devolve ("recusada", texto do alerta)
        ou ("confirmada", texto da janela de confirmação)."""
        def verificar(d):
            try:
                return ("recusada", d.switch_to.alert.text)
            except NoAlertPresentException:
                pass
            janelas = [e for e in d.find_elements(*self.CONFIRMACAO) if e.is_displayed()]
            return ("confirmada", janelas[0].text) if janelas else False

        tipo, texto = WebDriverWait(self.driver, timeout).until(verificar)
        if tipo == "recusada":
            self.driver.switch_to.alert.accept()
        return tipo, texto

    def texto_confirmacao(self):
        return self.texto_de(self.CONFIRMACAO)

    def fechar_confirmacao(self):
        self.clicar(self.BOTAO_OK)
