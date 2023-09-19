import requests
from flask import Flask, jsonify, request
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")


@app.route("/symbol_search", methods=["POST"])
def symbol_search():
    url = "https://symbol-search.tradingview.com/symbol_search/?"
    # symbol = request.form.get("symbol")
    symbol = request.get_json()["symbol"]
    # print(symbol)
    params = {"text": symbol}

    response = requests.get(url, params=params)
    return jsonify(response.text)


if __name__ == "__main__":
    app.run()
