"""Page Object do carrinho de compras."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CarrinhoPage(BasePage):
    BOTAO_CARRINHO = (By.ID, "cartur")
    LINHAS = (By.CSS_SELECTOR, "#tbodyid tr")
    NOMES = (By.CSS_SELECTOR, "#tbodyid tr td:nth-child(2)")
    PRECOS = (By.CSS_SELECTOR, "#tbodyid tr td:nth-child(3)")
    TOTAL = (By.ID, "totalp")
    BOTAO_COMPRA = (By.XPATH, "//button[contains(., 'Place Order')]")

    def abrir(self):
        self.clicar(self.BOTAO_CARRINHO)
        return self

    def aguardar_itens(self, quantidade=1):
        """Os itens chegam com atraso e um de cada vez: espera ter `quantidade` linhas."""
        self.wait.until(lambda d: len(d.find_elements(*self.LINHAS)) >= quantidade)

    def aguardar_quantidade_exata(self, quantidade):
        """Espera o carrinho ter exatamente `quantidade` linhas (ex.: depois de remover um item)."""
        self.wait.until(lambda d: len(d.find_elements(*self.LINHAS)) == quantidade)

    def remover_produto(self, nome):
        """Clica em 'Delete' na linha do produto e espera o carrinho recarregar."""
        linhas = self.driver.find_elements(*self.LINHAS)
        linha = next(l for l in linhas if nome in l.text)
        quantidade = len(linhas)
        linha.find_element(By.LINK_TEXT, "Delete").click()
        self.wait.until(EC.staleness_of(linha))
        self.aguardar_quantidade_exata(quantidade - 1)

    def nomes_produtos(self):
        return [e.text.strip() for e in self.driver.find_elements(*self.NOMES)]

    def precos_produtos(self):
        return [
            int(e.text) for e in self.driver.find_elements(*self.PRECOS)
            if e.text.strip().isdigit()
        ]

    def total(self):
        """Espera o total ser calculado (começa vazio) e devolve como número."""
        self.wait.until(lambda d: d.find_element(*self.TOTAL).text.strip().isdigit())
        return int(self.texto_de(self.TOTAL))

    def finalizar_compra(self):
        self.clicar(self.BOTAO_COMPRA)
