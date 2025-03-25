from flask import Flask, render_template

app = Flask(__name__)


@app.route("/conditionals/")
def conditionals():
    company = ""

    return render_template("conditionals_basics.html", company=company)
