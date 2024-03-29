from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('./home.html')

@app.route("/risks")
def risks():
    return render_template('./risks.html')

@app.route("/solutions")
def solutions():
    return render_template('./solutions.html')

@app.route("/solutions/egua")
def solutionsegua():
    return render_template('./solutionsegua.html')

@app.route("/solutions/elefante")
def solutionselefante():
    return render_template('./solutionselefante.html')

app.run(host='localhost',port=3000,debug=True)
