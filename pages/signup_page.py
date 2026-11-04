"""Page Object do modal de cadastro (botão 'Sign up' no menu)."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):
    BOTAO_MENU = (By.ID, "signin2")
    MODAL = (By.ID, "signInModal")
    CAMPO_USUARIO = (By.ID, "sign-username")
    CAMPO_SENHA = (By.ID, "sign-password")
    BOTAO_CADASTRAR = (By.CSS_SELECTOR, "#signInModal button[onclick='register()']")

    def abrir(self):
        """Acessa o site e abre o modal de cadastro."""
        self.abrir_site()
        self.clicar(self.BOTAO_MENU)
        self.esperar_visivel(self.MODAL)
        return self

    def cadastrar(self, usuario, senha):
        """Preenche o modal, envia e devolve o texto do alerta exibido."""
        self.digitar(self.CAMPO_USUARIO, usuario)
        self.digitar(self.CAMPO_SENHA, senha)
        self.clicar(self.BOTAO_CADASTRAR)
        return self.ler_alerta_e_aceitar()
