from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("plot.html")

if __name__ == "__main__":
    app.run(debug=True)
    