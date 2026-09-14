from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form001", methods=["GET", "POST"])
def form1():
    if request.method == "POST":
        nome = request.form["nome"]
        return f"{nome} Cadastro concluido!"
    return render_template("form001.html")


@app.route("/form002", methods=["GET", "POST"])
def form2():
    if request.method == "POST":
        nome = request.form["Usu"]
        return f"{nome} Cadastro concluido!"
    return render_template("form002.html")


@app.route("/form003")
def form3():
    nome = request.args.get("nome")
    if nome:
        return f"{nome} Cadastro concluido!"
    return render_template("form003.html")


if __name__ == "__main__":
    app.run(debug=True)
