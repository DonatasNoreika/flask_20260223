from flask import Flask, render_template, request
from calendar import isleap

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/keliamieji/", methods=['GET', 'POST'])
def keliamieji():
    if request.method == "POST":
        metai = int(request.form['metai'])
        return render_template("rezultatas.html", metai=metai, isleap=isleap)
    return render_template("keliamieji.html")

if __name__ == "__main__":
    app.run(debug=True)

