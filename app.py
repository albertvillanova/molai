from flask import abort, Flask, jsonify, request

import molai.main


app = Flask(__name__)


@app.route("/predict")
def predict():
    smile = request.args.get("smile")
    if not smile:
        abort(400)  # TODO: message="Missing required parameter 'smile'."
    model_id = request.args.get("model")
    prediction = molai.main.predict(smile=smile, model_id=model_id)
    return {
        "smile": smile,
        "prediction": float(prediction),
    }
