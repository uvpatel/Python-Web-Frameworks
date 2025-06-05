from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    name = "Urvil"
    return render_template("index.html", name=name)

# About route
@app.route("/about")
def about():
    name = "Urvil"
    return render_template("about.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
