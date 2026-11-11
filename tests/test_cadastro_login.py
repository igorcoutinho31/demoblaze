"""
Fluxo 1: CADASTRO (Sign up) e LOGIN (Log in)

Modelo de cada teste:
  Dado (pré-condição)  ->  Quando (ação)  ->  Então (assert com o resultado esperado)
"""
import pytest

from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from tests.dados import SENHA_PADRAO, usuario_unico


@pytest.fixture
def usuario_cadastrado(driver, base_url):
    """Pré-condição: cria um usuário novo e devolve (usuario, senha)."""
    usuario = usuario_unico()
    alerta = SignupPage(driver, base_url).abrir().cadastrar(usuario, SENHA_PADRAO)
    assert alerta == "Sign up successful.", f"Pré-condição falhou: {alerta!r}"
    return usuario, SENHA_PADRAO


@pytest.mark.cadastro
def test_ct01_cadastro_usuario_novo_mostra_sucesso(driver, base_url):
    """CT01 — PE (classe válida): usuário inexistente + senha preenchida."""
    usuario = usuario_unico()
    # Dado que estou no modal de cadastro
    pagina = SignupPage(driver, base_url).abrir()
    # Quando me cadastro com um usuário que ainda não existe
    alerta = pagina.cadastrar(usuario, SENHA_PADRAO)
    pagina.salvar_evidencia("CT01_apos_cadastro")
    # Então vejo o alerta de sucesso
    assert alerta == "Sign up successful.", f"Usuário {usuario!r}: alerta {alerta!r}"


@pytest.mark.cadastro
def test_ct02_cadastro_usuario_existente_recusado(driver, base_url, usuario_cadastrado):
    """CT02 — PE (classe inválida): nome de usuário que já existe."""
    usuario, senha = usuario_cadastrado
    # Dado que o usuário já existe e abro o modal de cadastro de novo
    pagina = SignupPage(driver, base_url).abrir()
    # Quando tento me cadastrar com o mesmo nome
    alerta = pagina.cadastrar(usuario, senha)
    pagina.salvar_evidencia("CT02_usuario_existente")
    # Então o cadastro é recusado
    assert alerta == "This user already exist.", f"Usuário {usuario!r}: alerta {alerta!r}"


@pytest.mark.login
def test_ct03_login_valido_mostra_boas_vindas(driver, base_url, usuario_cadastrado):
    """CT03 — PE (classe válida): usuário e senha corretos."""
    usuario, senha = usuario_cadastrado
    # Dado que tenho um usuário cadastrado e abro o modal de login
    pagina = LoginPage(driver, base_url).abrir()
    # Quando entro com usuário e senha corretos
    pagina.entrar(usuario, senha)
    # Então o menu mostra "Welcome <usuário>"
    texto = pagina.texto_boas_vindas(usuario)
    pagina.salvar_evidencia("CT03_login_valido")
    assert texto == f"Welcome {usuario}"


@pytest.mark.login
def test_ct04_login_senha_errada_mostra_erro(driver, base_url, usuario_cadastrado):
    """CT04 — PE (classe inválida): usuário existente + senha errada."""
    usuario, _ = usuario_cadastrado
    # Dado que tenho um usuário cadastrado e abro o modal de login
    pagina = LoginPage(driver, base_url).abrir()
    # Quando entro com a senha errada
    pagina.entrar(usuario, "SenhaErrada#999")
    # Então vejo o alerta de erro
    alerta = pagina.mensagem_de_erro()
    pagina.salvar_evidencia("CT04_senha_errada")
    assert alerta == "Wrong password.", f"Alerta inesperado: {alerta!r}"
