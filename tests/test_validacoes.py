"""
Validações que um sistema real deveria ter (CT12 a CT14)

Estes testes esperam que o site RECUSE dados inválidos. Se o site aceitar,
o teste falha: é um DEFEITO, que vai para o relatório (seção 4.1) com o print
salvo em evidencias/. Teste que falha não se apaga.

Critérios usados (boas práticas, já que o site não publica regras):
- senha com no mínimo 8 caracteres (recomendação OWASP / NIST);
- número de cartão só com dígitos e mês entre 1 e 12.
"""
import pytest

from pages.carrinho_page import CarrinhoPage
from pages.catalogo_page import CatalogoPage
from pages.compra_page import CompraPage
from pages.signup_page import SignupPage
from tests.dados import usuario_unico

PRODUTO = "Samsung galaxy s6"


def abrir_formulario_de_compra(driver, base_url):
    """Adiciona um produto ao carrinho e abre o formulário de compra."""
    catalogo = CatalogoPage(driver, base_url).abrir()
    catalogo.abrir_produto(PRODUTO)
    catalogo.adicionar_carrinho()
    carrinho = CarrinhoPage(driver, base_url).abrir()
    carrinho.aguardar_itens()
    carrinho.finalizar_compra()
    return CompraPage(driver, base_url).aguardar_modal()


@pytest.mark.validacao
@pytest.mark.cadastro
def test_ct12_cadastro_com_senha_de_7_caracteres_e_recusado(driver, base_url):
    """CT12 — VL: senha com 7 caracteres (um abaixo do mínimo de 8)."""
    # Dado que estou no modal de cadastro
    pagina = SignupPage(driver, base_url).abrir()
    # Quando me cadastro com uma senha de 7 caracteres
    alerta = pagina.cadastrar(usuario_unico(), "Abc@123")
    pagina.salvar_evidencia("CT12_senha_7_caracteres")
    # Então o cadastro deveria ser recusado
    assert alerta != "Sign up successful.", "DEFEITO: o site aceitou uma senha de 7 caracteres."


@pytest.mark.validacao
@pytest.mark.carrinho
def test_ct13_compra_com_cartao_com_letras_e_recusada(driver, base_url):
    """CT13 — PE (classe inválida): número do cartão com letras."""
    # Dado que estou no formulário de compra com um produto no carrinho
    compra = abrir_formulario_de_compra(driver, base_url)
    # Quando informo um cartão com letras
    compra.preencher_dados("Cliente Teste", "Brasil", "Sao Paulo", "abcdefghijklmnop", "11", "2026")
    compra.confirmar()
    resultado, texto = compra.resultado_da_compra()
    compra.salvar_evidencia("CT13_cartao_com_letras")
    # Então a compra deveria ser recusada
    assert resultado == "recusada", f"DEFEITO: compra confirmada com cartão 'abcdefghijklmnop' ({texto!r})."


@pytest.mark.validacao
@pytest.mark.carrinho
def test_ct14_compra_com_mes_13_e_recusada(driver, base_url):
    """CT14 — VL: mês 13 (um acima do maior mês válido, 12)."""
    # Dado que estou no formulário de compra com um produto no carrinho
    compra = abrir_formulario_de_compra(driver, base_url)
    # Quando informo o mês 13
    compra.preencher_dados("Cliente Teste", "Brasil", "Sao Paulo", "1234567890123456", "13", "2026")
    compra.confirmar()
    resultado, texto = compra.resultado_da_compra()
    compra.salvar_evidencia("CT14_mes_13")
    # Então a compra deveria ser recusada
    assert resultado == "recusada", f"DEFEITO: compra confirmada com mês 13 ({texto!r})."
