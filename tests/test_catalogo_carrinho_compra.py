"""
Fluxos 2 e 3: CATÁLOGO, CARRINHO E COMPRA (CT05 a CT08)

Modelo de cada teste:
  Dado (pré-condição)  ->  Quando (ação)  ->  Então (assert com o resultado esperado)
"""
import pytest

from pages.carrinho_page import CarrinhoPage
from pages.catalogo_page import CatalogoPage
from pages.compra_page import CompraPage

PRODUTO = "Samsung galaxy s6"
PRODUTOS_CT06 = ["Samsung galaxy s6", "Nokia lumia 1520"]
MONITORES = {"Apple monitor 24", "ASUS Full HD"}

DADOS_COMPRA = {
    "nome": "Cliente Teste",
    "pais": "Brasil",
    "cidade": "Sao Paulo",
    "cartao": "1234567890123456",  # número fictício
    "mes": "11",
    "ano": "2026",
}


def adicionar_ao_carrinho(driver, base_url, nome):
    """Abre o produto pela Home, adiciona ao carrinho e devolve o preço dele."""
    catalogo = CatalogoPage(driver, base_url).abrir()
    catalogo.abrir_produto(nome)
    preco = catalogo.preco_produto()
    alerta = catalogo.adicionar_carrinho()
    assert alerta == "Product added.", f"Alerta inesperado ao adicionar {nome!r}: {alerta!r}"
    return preco


@pytest.mark.catalogo
def test_ct05_filtro_categoria_mostra_so_monitores(driver, base_url):
    """CT05 — PE: categoria Monitors deve mostrar somente monitores."""
    # Dado que estou na página inicial
    pagina = CatalogoPage(driver, base_url).abrir()
    # Quando seleciono a categoria Monitors
    pagina.selecionar_categoria("Monitors")
    produtos = pagina.nomes_produtos()
    pagina.salvar_evidencia("CT05_filtro_monitors")
    # Então só aparecem monitores
    assert set(produtos) == MONITORES, f"Produtos exibidos: {produtos}"


@pytest.mark.carrinho
def test_ct06_total_do_carrinho_e_a_soma_dos_precos(driver, base_url):
    """CT06 — 2 produtos no carrinho; o total deve ser a soma dos preços."""
    # Dado que adicionei dois produtos ao carrinho
    precos = [adicionar_ao_carrinho(driver, base_url, nome) for nome in PRODUTOS_CT06]
    # Quando abro o carrinho
    carrinho = CarrinhoPage(driver, base_url).abrir()
    carrinho.aguardar_itens(quantidade=len(PRODUTOS_CT06))
    nomes = carrinho.nomes_produtos()
    total = carrinho.total()
    carrinho.salvar_evidencia("CT06_carrinho_total")
    # Então os dois produtos aparecem e o total é a soma dos preços
    assert sorted(nomes) == sorted(PRODUTOS_CT06), f"Itens no carrinho: {nomes}"
    assert total == sum(precos), f"Total {total} ≠ soma dos preços {precos} = {sum(precos)}"


@pytest.mark.carrinho
def test_ct07_compra_com_nome_e_cartao_vazios_e_recusada(driver, base_url):
    """CT07 — VL (0 caractere) em Name e Credit card."""
    # Dado que existe um produto no carrinho
    adicionar_ao_carrinho(driver, base_url, PRODUTO)
    carrinho = CarrinhoPage(driver, base_url).abrir()
    carrinho.aguardar_itens()
    carrinho.finalizar_compra()
    compra = CompraPage(driver, base_url).aguardar_modal()
    # Quando tento comprar sem preencher os dados
    alerta = compra.comprar_sem_dados()
    compra.salvar_evidencia("CT07_compra_campos_vazios")
    # Então a compra é recusada
    assert alerta == "Please fill out Name and Creditcard.", f"Alerta inesperado: {alerta!r}"


@pytest.mark.carrinho
def test_ct08_compra_completa_mostra_confirmacao(driver, base_url):
    """CT08 — compra com todos os dados preenchidos (fictícios)."""
    # Dado que existe um produto no carrinho
    adicionar_ao_carrinho(driver, base_url, PRODUTO)
    carrinho = CarrinhoPage(driver, base_url).abrir()
    carrinho.aguardar_itens()
    carrinho.finalizar_compra()
    compra = CompraPage(driver, base_url).aguardar_modal()
    # Quando preencho os dados e confirmo a compra
    compra.preencher_dados(**DADOS_COMPRA)
    compra.confirmar()
    # Então aparece a confirmação
    mensagem = compra.texto_confirmacao()
    compra.salvar_evidencia("CT08_compra_confirmada")
    assert mensagem == "Thank you for your purchase!"
    compra.fechar_confirmacao()
