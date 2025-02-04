import random

from flask import Flask, render_template

# Padrão de criação do app
app = Flask(__name__)

# Lista de cores para alterar o fundo do site
lista_cores = [
    "#9ff5d1",
    "#96ffea",
    "#6cd9c5",
    "#60d1b3",
    "#b5ffd9"]

# Lista de adjetivos para o site
lista_adjetivos = [
    "Inteligentes.",
    "Bonitas.",
    "Velozes.",
    "Animais marinhos.",
    "Verdes.",
    "Amigaveis.",
    "Importantes para o meio ambiente."]

# Lista de imagens
lista_imagens = [
    "01.jpg",
    "02.jpg",
    "03.jpg",
    "04.jpg",
    "05.jpg"]

# Aqui irá todas as minhas rotas
@app.route("/sobre")
def pag_sobre():
    cor_de_fundo = random.choice(lista_cores)
    return render_template("PagInicial.html", cor_de_fundo_html = cor_de_fundo)

@app.route("/infos")
def pag_infos():
    cor_de_fundo = random.choice(lista_cores)
    adjetivos_aleatorios = random.choice(lista_adjetivos)
    imagens_aleatorias = random.choice(lista_imagens)
    return render_template("PagAleatorio.html", cor_de_fundo_html = cor_de_fundo, 
                           adjetivos_aleatorios_html = adjetivos_aleatorios, imagens_aleatorias_html = imagens_aleatorias)

app.run(debug=True)