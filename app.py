from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("jinja.html", name="Jeff", template_name="Jinja2")


@app.route("/expressions/")
def expressions():
    # interpolation
    color = "blue"
    animal_one = "wolf"
    animal_two = "eagle"

    # add/subtract
    orange_amount = 111
    apple_amount = 11
    donate_amount = 5

    # string concat
    first_name = "Jeff"
    last_name = "Graham"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name,
    }

    return render_template("expressions.html", **kwargs)
