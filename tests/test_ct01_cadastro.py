"""CT01 — Cadastro com usuário novo mostra alerta de sucesso.

Técnica: Partição de Equivalência (classe válida: usuário inexistente + senha preenchida).

Passos:
  1. Acessar https://www.demoblaze.com
  2. Clicar em "Sign up"
  3. Preencher Username com um nome único e Password com uma senha fictícia
  4. Clicar no botão "Sign up" do modal
Resultado esperado: alerta do navegador com o texto "Sign up successful."
"""
import pytest

from conftest import EVIDENCIAS_DIR
from pages.signup_page import SignupPage
from tests.dados import SENHA_PADRAO, usuario_unico


@pytest.mark.cadastro
def test_ct01_cadastro_usuario_novo(driver):
    usuario = usuario_unico()

    pagina = SignupPage(driver).abrir()
    texto_alerta = pagina.cadastrar(usuario, SENHA_PADRAO)
    pagina.screenshot(EVIDENCIAS_DIR / "CT01_apos_cadastro.png")

    assert texto_alerta == "Sign up successful.", (
        f"Alerta inesperado para o usuário {usuario!r}: {texto_alerta!r}"
    )
