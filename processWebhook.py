import flask
import os
from flask import send_from_directory, jsonify
from urllib.request import urlopen  # Use to call APIs
import json 

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)




app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')


@app.route('/<name>')
def home(name):
    url = ("https://financialmodelingprep.com/api/v3/income-statement/"+name+"?apikey=68cea4d99d13d60f59e7a1df544f632a")
    data = get_jsonparsed_data(url)
    return jsonify(data)

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()