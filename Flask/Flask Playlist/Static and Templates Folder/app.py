from flask import Flask, render_template

app = Flask(__name__)  # App define

# Home page
@app.route("/")
def home():
    return render_template('index.html')

# About page
@app.route("/about")
def about():
    name = "Urvil"  # Passing Variable
    return render_template('about.html', name=name)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
