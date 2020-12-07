from flask import abort, Flask, jsonify, request

import molai.main


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/predict")
def predict():
    smile = request.args.get("smile")
    if not smile:
        abort(400)  # TODO: message="Missing required parameter 'smile'."
    print(f"smile: {smile}")
    prediction = molai.main.predict(smile=smile)
    return {
        "prediction": prediction,
    }
