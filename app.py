from flask import Flask, render_template
from werkzeug import exceptions

app = Flask(__name__)

@app.route("/")
def index():
 return render_template("index.html")

@app.errorhandler(exceptions.NotFound)
def page_not_found(err):
    return render_template("404.html", error=err), 404

if __name__ =="__main__":
    app.run(debug=True)

app.run()
