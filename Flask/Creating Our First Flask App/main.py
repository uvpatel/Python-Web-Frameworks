from flask import Flask # import flask 

app = Flask(__name__) # App define

# decorator
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/urvil")
def urvil():
    return "<p>Hello, Urvil!</p>"

app.run(debug=True) # detact change and serve always it is good practice 
 # it is use in eveywhere. 
# for running apps 