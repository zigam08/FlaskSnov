from flask import Flask, render_template, request
import random as r

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ljubezen", methods = ["POST"])
def love_calc():
    print(request.form)
    i1 = request.form["ime1"]
    i2 = request.form["ime2"]
    p = 0
    k = ""
    if i1.strip().lower() == "žiga" or i2.strip().lower() == "žiga":
        p = r.randint(90,100)
    elif i1.strip().lower() == "anže" or i2.strip().lower() == "anže":
        p = r.randint(0,10)
    else:
        p = r.randint(0,100)

    if i1.strip().lower() == i2.strip().lower():
        p = 100
        k = "Samoljubje!"

    if "x" in i1.strip().lower() or "x" in i2.strip().lower():
        p = r.randint(0,100) * 2
        if p > 100:
            p = 100


    zdruzenje = i1[:len(i1)//2] + i2[len(i2)//2:]


    if p < 50:
        k = "Pozabi"
    elif p < 85:
        k = "Morda"
    elif p > 85:
        k = "Poroka!"
    print(k)


    if i1.strip().lower() == "luka" or i2.strip().lower() == "luka":
        p = 404
        k = "Ljubezen ni najdena!"

    nasveti = [
    "Pojdita na kebab",
    "Skupaj igrata Minecraft",
    "Pojdita na sprehod",
    "Igrajta družabne igre",
    "Pojdita na sladoled",
    "Skupaj glejta film",
    "Pojdita na bowling",
    "Naredita si piknik",
    "Skupaj specita pico",
    "Igrajta videoigre"
]

    nasvet = r.choice(nasveti)

    

    return render_template("index.html", ime1 = i1, ime2 = i2, procent = p, k = k, zdruzenje = zdruzenje, nasvet = nasvet)


app.run(debug=True)