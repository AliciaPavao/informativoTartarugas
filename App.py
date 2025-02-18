import random

from .data import listas_configuracao as listas
from flask import Flask, render_template, request, redirect

# Padrão de criação do app
app = Flask(__name__)


# Aqui irá todas as minhas rotas

# Pag sobre
@app.route("/sobre")
def pag_sobre():
    cor_de_fundo = random.choice(listas.lista_cores)
    return render_template("PagInicial.html", cor_de_fundo_html = cor_de_fundo)

# Pag infos
@app.route("/", methods=["GET"])
def pag_infos():
    cor_de_fundo = random.choice(listas.lista_cores)
    adjetivos_aleatorios = random.choice(listas.lista_adjetivos)
    imagens_aleatorias = random.choice(listas.lista_imagens)
    return render_template("PagAleatorio.html", cor_de_fundo_html = cor_de_fundo, 
                           adjetivos_aleatorios_html = adjetivos_aleatorios, imagens_aleatorias_html = imagens_aleatorias)


# Cor
@app.route("/cores", methods=["GET"])
def pag_cores():
     return render_template("PagCor.html", cores = listas.lista_cores)

@app.route("/post/cadastrarcor", methods=["POST"])
def post_cadastrarcor():
    cor_vinda_do_html = request.form.get("cor")
    listas.lista_cores.append(cor_vinda_do_html)
    return redirect("/cores")

@app.route("/cores/delete/<indice_cor>", methods=["GET"])
def delete_cores(indice_cor):
    # Lembrar de converter o int para inteiro - pois ele vem como string
    indice_cor = int(indice_cor)
    # Excluir a cor da lista através do indice
    listas.lista_cores.pop(indice_cor)
    return redirect("/cores")


# Escrever
@app.route("/escreva", methods=["GET"])
def pag_escreva():
     return render_template("PagEscreva.html", frases = listas.lista_adjetivos)

@app.route("/post/cadastrarfrase", methods=["POST"])
def post_cadastrarfrase():
    frase_vinda_do_html = request.form.get("frase")
    listas.lista_adjetivos.append(frase_vinda_do_html)
    return redirect("/escreva")

# Post - Envia uma informção
# Get - Pega uma informação

app.run(debug=True)