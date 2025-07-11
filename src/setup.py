"""
Modulo que contem as configurações do aplicativo
"""

from typing import List
import string


class Config:
    """
    Classe de configuração central do aplicativo educativo.

    Responsável por gerar e agrupar letras e números para o jogo, além de fornecer totais de páginas.

    Exemplo de uso:
        config = Config()
        letras_paginas = config.get_letras_paginas()
        numeros_paginas = config.get_numeros_paginas()
        total = config.total_paginas
    """

    def __init__(self) -> None:
        """
        Inicializa a configuração, gerando listas de letras e números.
        Letras são agrupadas em maiúsculas e minúsculas, e números de 0 a 100.
        """
        self.ALFABETO_COMPLETO = list(string.ascii_uppercase) + list(string.ascii_lowercase)
        self.NUMEROS = [str(i) for i in range(101)]
        self.LETRAS_POR_PAGINA = 13

    @staticmethod
    def agrupar_em_paginas(lista: list, tamanho_pagina: int) -> List[List[str]]:
        """
        Agrupa uma lista em sublistas de tamanho definido.

        Args:
            lista (list): Lista a ser agrupada.
            tamanho_pagina (int): Tamanho de cada grupo/página.
        Returns:
            List[List[str]]: Lista de listas agrupadas.
        Exemplo:
            agrupar_em_paginas([1,2,3,4,5], 2) => [[1,2],[3,4],[5]]
        """
        return [lista[i:i + tamanho_pagina] for i in range(0, len(lista), tamanho_pagina)]

    def get_letras_paginas(self) -> List[List[str]]:
        """
        Retorna as letras agrupadas em páginas.
        Returns:
            List[List[str]]: Lista de listas, cada uma representando uma página de letras.
        """
        return Config.agrupar_em_paginas(self.ALFABETO_COMPLETO, self.LETRAS_POR_PAGINA)

    def get_numeros_paginas(self) -> List[List[str]]:
        """
        Retorna os números agrupados em páginas.
        O primeiro grupo vai de 0 a 10 (11 números), os demais de 10 em 10.
        Returns:
            List[List[str]]: Lista de listas, cada uma representando uma página de números.
        """
        return [self.NUMEROS[0:11]] + Config.agrupar_em_paginas(self.NUMEROS[11:], 10)

    @property
    def total_paginas_letras(self) -> int:
        """
        Retorna o total de páginas de letras.
        Returns:
            int: Número de páginas de letras.
        """
        return len(self.get_letras_paginas())

    @property
    def total_paginas_numeros(self) -> int:
        """
        Retorna o total de páginas de números.
        Returns:
            int: Número de páginas de números.
        """
        return len(self.get_numeros_paginas())

    @property
    def total_paginas(self) -> int:
        """
        Retorna o total de páginas do jogo (letras + números).
        Returns:
            int: Total de páginas.
        """
        return self.total_paginas_letras + self.total_paginas_numeros


# Instancia a configuração
config = Config()
