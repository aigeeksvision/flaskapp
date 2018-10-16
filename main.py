# Dependencies
from flask import Flask, render_template

# Flask App
app = Flask(__name__)
# Defalut route
@app.route("/")
def default():
   return render_template("layout.html")

# /first route
@app.route("/first")
def first():
   return render_template("first.html")

# /second route
@app.route("/second")
def second():
   return render_template("second.html")

# /third route
@app.route("/third")
def third():
   return render_template("third.html")

if __name__ == '__main__':
   app.run(debug=True)