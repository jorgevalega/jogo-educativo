"""
Serviço responsável por fornecer informações sobre as páginas do jogo.
"""

from setup import Config


def get_pagina_info(pagina: int, config: Config):
    """
    Recebe o número da página e a configuração, e retorna os dados necessários para renderizar a página.
    
    Args:
        pagina (int): O número da página a ser exibida.
        config (Config): A configuração do jogo.
    
    Returns:
        dict: Dicionário com as informações da página.

    Exemplo de retorno:
    {
        "grupo": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", ...],
        "pagina": 1,
        "total": 100,
        "tipo": "Letras",
        "pagina_atual": 1,
        "paginas_total": 100
    }
    """
    # Corrige páginas inválidas
    if pagina < 1 or pagina > config.total_paginas:
        pagina = 1

    if pagina <= config.total_paginas_letras:
        grupo = config.get_letras_paginas()[pagina - 1]
        tipo = "Letras"
        pagina_atual = pagina
        paginas_total = config.total_paginas_letras
    else:
        idx = pagina - config.total_paginas_letras - 1
        grupo = config.get_numeros_paginas()[idx]
        tipo = "Números"
        pagina_atual = idx + 1
        paginas_total = config.total_paginas_numeros

    return {
        "grupo": grupo,
        "pagina": pagina,
        "total": config.total_paginas,
        "tipo": tipo,
        "pagina_atual": pagina_atual,
        "paginas_total": paginas_total
    }
