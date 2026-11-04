"""
Fluxo 1: CADASTRO (Sign up) e LOGIN (Log in)

Modelo de cada teste:
  Dado (pré-condição)  ->  Quando (ação)  ->  Então (assert com o resultado esperado)
"""
import pytest

from pages.signup_page import SignupPage
from tests.dados import SENHA_PADRAO, usuario_unico


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
def test_ct02_cadastro_usuario_existente_recusado(driver, base_url):
    # TODO (grupo): cadastre um usuário, tente cadastrar o MESMO nome de novo
    # e verifique o alerta "This user already exist."
    pytest.skip("A fazer pelo grupo")
