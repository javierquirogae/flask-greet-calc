# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)



@app.route('/add')
def adds():
    """adds"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a,b))

@app.route('/sub')
def subtracts():
    """subtracts"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a,b))

@app.route('/mult')
def multiplies():
    """multiplies"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a,b))

@app.route('/div')
def divides():
    """divides"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a,b))

op = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """do all."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(op[oper](a,b))

   