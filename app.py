from flask import Flask, render_template

app = Flask(__name__)


class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


@app.route("/data_structures/")
def render_data_structures():
    movies = ["The Wiz", "Cooley High", "Training Day"]

    car = {
        "brand": "Cadillac",
        "model": "El Dorado",
        "year": 1973,
    }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    kwargs = {"movies": movies, "car": car, "moons": moons}

    return render_template("data_structures.html", **kwargs)
