from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("jinja.html", name="Jeff", template_name="Jinja2")
