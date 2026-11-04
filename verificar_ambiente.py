"""
Verificacao do ambiente do laboratorio para o A3 (Selenium + pytest).

Como usar (em cada computador):
    pip install selenium pytest
    python verificar_ambiente.py

Resultado esperado: o Chrome abre, acessa o Demoblaze e aparece "AMBIENTE OK".
"""
import sys


def main():
    print(f"Python {sys.version.split()[0]}")
    if sys.version_info < (3, 10):
        print("ATENCAO: use Python 3.10 ou superior.")

    try:
        import selenium
        import pytest  # noqa: F401
    except ImportError as erro:
        print(f"FALHOU: pacote nao instalado ({erro.name}). Rode: pip install selenium pytest")
        return 1
    print(f"Selenium {selenium.__version__}")

    from selenium import webdriver

    try:
        navegador = webdriver.Chrome()  # o Selenium Manager baixa o driver sozinho
    except Exception as erro:
        print("FALHOU ao abrir o Chrome.")
        print("Verifique se o Google Chrome esta instalado e se a rede libera")
        print("googlechromelabs.github.io e storage.googleapis.com.")
        print(f"Detalhe: {erro}")
        return 1

    try:
        navegador.get("https://www.demoblaze.com")
        titulo = navegador.title
    finally:
        navegador.quit()

    if titulo == "STORE":
        print("AMBIENTE OK")
        return 0
    print(f"FALHOU: o site abriu com titulo inesperado ({titulo!r}). Verifique o acesso a www.demoblaze.com.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
