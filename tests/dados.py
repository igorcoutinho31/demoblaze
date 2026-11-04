"""Dados de teste fictícios (nunca usar dados reais)."""
import uuid

SENHA_PADRAO = "Teste@123"


def usuario_unico(prefixo="grupo2"):
    """O Demoblaze recusa nomes repetidos, então cada execução gera um novo."""
    return f"{prefixo}_{uuid.uuid4().hex[:10]}"
