from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

full_accounts = {
    'azr-fullservice-accounts': ["azr-008", "azr-acc"]
}

@app.route("/", methods=["GET"])
def accountget():
    return full_accounts

@app.route("/<accountname>", methods=["POST"])
def accountcheck(accountname):
    if accountname in full_accounts["azr-fullservice-accounts"]:
        return "True"
    else:
        return "False"


if __name__ == "__main__":
    app.run(debug=True)