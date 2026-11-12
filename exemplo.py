"""Simulação didática. Não compra anúncios nem os publica."""

AUTORIZADOS = {
    "candidato", "partido", "federacao",
    "coligacao", "administrador_financeiro",
}


def avaliar_contratante(contratante):
    if contratante not in AUTORIZADOS:
        return "BLOQUEAR a contratação"
    return "PENDENTE: revisar peça, provedor, identificação e período"


if __name__ == "__main__":
    print(avaliar_contratante("empresa_privada"))
    assert avaliar_contratante("empresa_privada").startswith("BLOQUEAR")
    assert avaliar_contratante("partido").startswith("PENDENTE")
