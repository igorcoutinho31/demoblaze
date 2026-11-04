"""Page Object do modal de login (botão 'Log in' no menu)."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    BOTAO_MENU = (By.ID, "login2")
    MODAL = (By.ID, "logInModal")
    CAMPO_USUARIO = (By.ID, "loginusername")
    CAMPO_SENHA = (By.ID, "loginpassword")
    BOTAO_ENTRAR = (By.CSS_SELECTOR, "#logInModal button[onclick='logIn()']")
    BOAS_VINDAS = (By.ID, "nameofuser")

    def abrir(self):
        """Acessa o site e abre o modal de login."""
        self.abrir_site()
        self.clicar(self.BOTAO_MENU)
        self.esperar_visivel(self.MODAL)
        return self

    def entrar(self, usuario, senha):
        self.digitar(self.CAMPO_USUARIO, usuario)
        self.digitar(self.CAMPO_SENHA, senha)
        self.clicar(self.BOTAO_ENTRAR)

    def texto_boas_vindas(self, usuario):
        """Espera o menu mostrar 'Welcome <usuario>' e devolve o texto."""
        self.wait.until(
            EC.text_to_be_present_in_element(self.BOAS_VINDAS, f"Welcome {usuario}")
        )
        return self.texto_de(self.BOAS_VINDAS)

    def mensagem_de_erro(self):
        """Login inválido responde com alerta JavaScript; devolve o texto dele."""
        return self.ler_alerta_e_aceitar()
