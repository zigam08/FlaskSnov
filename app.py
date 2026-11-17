from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/o-meni")
def about():
    return render_template("about.html")

# met kocke... random(1-6)
@app.route("/kocka")
def dice():
    return render_template("dice.html", kocka = random.randint(1,6))

# met kocke... random(1-N)
@app.route("/kocka/<N>")
def dice2(N):
    return render_template("dice.html", kocka = random.randint(6,int(N)))


@app.route("/ljubezen")
def love():
    return render_template("love.html", izracun = random.randint(6,int()))

app.run(debug = True)


sez = [1,2,4]
print(random.choice(sez))