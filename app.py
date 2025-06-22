from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Letras maiúsculas e minúsculas (A-Z, a-z)
letras_maiusculas = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
letras_minusculas = [chr(i) for i in range(ord('a'), ord('z') + 1)]
letras = letras_maiusculas + letras_minusculas

# Agrupamento das letras: 13 por página
letras_por_pagina = 13
letras_paginas = [letras[i:i + letras_por_pagina] for i in range(0, len(letras), letras_por_pagina)]

# Números de 0 a 100
numeros = [str(i) for i in range(101)]

# Primeiro grupo: 0 a 10 (11 números), depois de 10 em 10
numeros_paginas = [numeros[0:11]] + [numeros[i:i + 10] for i in range(11, 101, 10)]

# Total de páginas
total_paginas_letras = len(letras_paginas)
total_paginas_numeros = len(numeros_paginas)
total_paginas = total_paginas_letras + total_paginas_numeros

@app.route("/")
def index():
    """
    Rota principal da aplicação.
    Renderiza a página com o grupo de letras ou números correspondente à página atual.
    """
    pagina = int(request.args.get("pagina", 1))

    # Corrige páginas inválidas
    if pagina < 1 or pagina > total_paginas:
        pagina = 1

    if pagina <= total_paginas_letras:
        grupo = letras_paginas[pagina - 1]
        tipo = "Letras"
        pagina_atual = pagina
        paginas_total = total_paginas_letras
    else:
        idx = pagina - total_paginas_letras - 1
        grupo = numeros_paginas[idx]
        tipo = "Números"
        pagina_atual = idx + 1
        paginas_total = total_paginas_numeros

    return render_template(
        "index.html",
        grupo=grupo,
        pagina=pagina,
        total=total_paginas,
        tipo=tipo,
        pagina_atual=pagina_atual,
        paginas_total=paginas_total
    )

if __name__ == "__main__":
    app.run(debug=True)
