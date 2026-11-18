"""Page Object do catálogo de produtos (vitrine, categorias e página do produto)."""
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CatalogoPage(BasePage):
    PHONES = (By.LINK_TEXT, "Phones")
    LAPTOPS = (By.LINK_TEXT, "Laptops")
    MONITORS = (By.LINK_TEXT, "Monitors")

    PRODUTOS = (By.CSS_SELECTOR, "#tbodyid .card-title a")
    TITULO_PRODUTO = (By.CSS_SELECTOR, "h2.name")
    PRECO_PRODUTO = (By.CSS_SELECTOR, "h3.price-container")
    BOTAO_ADICIONAR = (By.CSS_SELECTOR, "a[onclick^='addToCart']")

    def abrir(self):
        self.abrir_site()
        self.esperar_visivel(self.PRODUTOS)
        return self

    def selecionar_categoria(self, categoria):
        """Clica na categoria e espera a vitrine trocar de produtos."""
        categorias = {
            "Phones": self.PHONES,
            "Laptops": self.LAPTOPS,
            "Monitors": self.MONITORS,
        }
        # A vitrine é recarregada por JavaScript: guardamos um produto antigo
        # e esperamos ele sumir, para não ler a lista de antes do filtro.
        produto_antigo = self.esperar_visivel(self.PRODUTOS)
        self.clicar(categorias[categoria])
        self.wait.until(EC.staleness_of(produto_antigo))
        self.esperar_visivel(self.PRODUTOS)
        return self

    def nomes_produtos(self):
        elementos = self.wait.until(lambda d: d.find_elements(*self.PRODUTOS))
        return [e.text.strip() for e in elementos if e.text.strip()]

    def abrir_produto(self, nome):
        self.clicar((By.LINK_TEXT, nome))
        self.esperar_visivel(self.TITULO_PRODUTO)
        return self

    def nome_produto(self):
        return self.texto_de(self.TITULO_PRODUTO)

    def preco_produto(self):
        """Lê o preço da página do produto (ex.: '$360 *includes tax' -> 360)."""
        texto = self.texto_de(self.PRECO_PRODUTO)
        resultado = re.search(r"\d+", texto)
        if not resultado:
            raise AssertionError(f"Preço não identificado em {texto!r}.")
        return int(resultado.group())

    def adicionar_carrinho(self):
        """Clica em 'Add to cart' e devolve o texto do alerta."""
        self.clicar(self.BOTAO_ADICIONAR)
        return self.ler_alerta_e_aceitar()
