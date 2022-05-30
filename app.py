from flask import Flask, render_template, request
from werkzeug import exceptions
from url_shortener import shorten_link

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        URL = request.form['url_input']
        print(URL)
        data = shorten_link(URL)
        short_link = data["url"]["shortLink"]
        return render_template("url_result.html", data=short_link)
    else:
         return render_template('index.html')


@app.errorhandler(exceptions.NotFound)
def page_not_found(err):
    return render_template("404.html", error=err), 404

if __name__ =="__main__":
    app.run(debug=True)

app.run()
