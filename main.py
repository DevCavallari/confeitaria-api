import os

from flask import Flask
from cardapio import buscar_cardapio, buscar_cardapio_id



app = Flask(__name__)

@app.route("/")
def hello_world():
  """Example Hello World route."""
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"

@app.route("/cardapio")
def mostrar_cardapio():
    return buscar_cardapio()

@app.route("/cardapio/<int:item_id>")
def mostrar_cardapio_id(item_id):
    return buscar_cardapio_id(item_id)

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))