from flask import Flask, render_template, request, redirect
from calendar import isleap
import pickle

app = Flask(__name__)

try:
    with open("zurnalas.pkl", 'rb') as file:
        zurnalas = pickle.load(file)
except FileNotFoundError:
    zurnalas = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/keliamieji/", methods=['GET', 'POST'])
def keliamieji():
    if request.method == "POST":
        metai = int(request.form['metai'])
        return render_template("rezultatas.html", metai=metai, isleap=isleap)
    return render_template("keliamieji.html")


@app.route("/biudzetas/", methods=["GET", "POST"])
def biudzetas():
    if request.method == "POST":
        suma = int(request.form['suma'])
        zurnalas.append(suma)
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(zurnalas, file)
    balansas = sum(zurnalas)
    return render_template("biudzetas.html", zurnalas=zurnalas, balansas=balansas)

if __name__ == "__main__":
    app.run(debug=True)

