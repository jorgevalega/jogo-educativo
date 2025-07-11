"""
Modulo principal da aplicação.
"""

from flask import Flask, render_template, request

from services.page_service import get_pagina_info
from setup import config


app = Flask(__name__)

@app.route("/")
def index():
    """
    Rota principal da aplicação.
    Renderiza a página com o grupo de letras ou números correspondente à página atual.
    """
    pagina = int(request.args.get("pagina", 1))
    pagina_info = get_pagina_info(pagina, config)

    return render_template(
        "index.html",
        **pagina_info
    )

if __name__ == "__main__":
    app.run(debug=True)
