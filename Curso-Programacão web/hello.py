from flask import Flask

app = Flask(__name__)


@app.route("/maior/<x>/<y>/<z>")
def Maior(x,y,z):
    x = float(x)
    y = float(y)
    z = float(z)
    if(x + y + z / 3 < 60):
        return "reprovado". format(x,y,z)
    else: 
        return "aprovado".format(x,y,z)