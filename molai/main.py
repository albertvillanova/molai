"""Main module."""

from .models import evaluate_model, load_model, make_prediction, save_model, \
    train_model
from .preprocessing import load_data


def train(model_id="1"):
    """Train the model.

    Parameters
    ----------
    model_id : str

    Returns
    -------
    None
    """
    print("Train the model")
    data = load_data(model_id=model_id)
    model = load_model(model_id=model_id, mode="train")
    train_model(model, data, model_id=model_id)
    save_model(model, model_id=model_id)


def evaluate(model_id="1"):
    """Evaluate the model.

    Parameters
    ----------
    model_id : str

    Returns
    -------
    dict
    """
    print("Evaluate the model")
    data = load_data(model_id=model_id)
    model = load_model(model_id=model_id, mode="evaluate")
    evaluation = evaluate_model(model, data, model_id=model_id)
    return evaluation


def predict(smile, model_id="1"):
    """Predict the property `P1` for a given smile.

    Parameters
    ----------
    smile : str
        Molecule smile.
    model_id : str

    Returns
    -------
    float
        Prediction of the model.
    """
    print(f"Predict property 'P1' for smile '{smile}'")
    model = load_model(model_id=model_id, mode="predict")
    prediction = make_prediction(model, smile, model_id=model_id)
    return prediction
