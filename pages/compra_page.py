"""Page Object da finalização da compra (modal Place Order)."""
from selenium.webdriver.common.by import By

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

    def texto_confirmacao(self):
        return self.texto_de(self.CONFIRMACAO)

    def fechar_confirmacao(self):
        self.clicar(self.BOTAO_OK)
