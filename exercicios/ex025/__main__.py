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


@app.route("/form003", methods=["GET", "POST"])
def form3():
    nome = request.args.get("nome")
    if nome:
        return f"{nome} Cadastro concluido!"
    return render_template("form003.html")

@app.route('/form004', methods=["GET", "POST"])
def form4():
    email = request.args.get("email")
    if email:
        return f"{email} Cadastro concluido!"
    return render_template('form004.html')

@app.route('/form005', methods=["GET", "POST"])
def form5():
    return render_template('form005.html')

@app.route('/form006', methods=["GET", "POST"])
def form6():
    return render_template('form006.html')

@app.route('/form007', methods=["GET", "POST"])
def form7():
    return render_template('form007.html')

@app.route('/form008', methods=["GET", "POST"])
def form8():
    return render_template('form008.html')

@app.route('/form009', methods=["GET", "POST"])
def form9():
    return render_template('form009.html')

@app.route('/form010', methods=["GET", "POST"])
def form10():
    return render_template('form010.html')

if __name__ == "__main__":
    app.run(debug=True)
