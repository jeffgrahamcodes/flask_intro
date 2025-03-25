from flask import Flask, render_template

app = Flask(__name__)


@app.route("/for-loop/conditionals/")
def render_conditional_for_loops():
    user_os = {
        "Jeff": "MacOS",
        "Mekhi": "Windows",
        "Jeffery": "Linux",
        "Aniyah": "Windows",
    }

    return render_template("loops_and_conditionals.html", user_os=user_os)
