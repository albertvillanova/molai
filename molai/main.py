"""Main module."""


def train():
    """Train the model.

    Returns
    -------
    None
    """
    print("Train the model")


def evaluate():
    """Evaluate the model.

    Returns
    -------
    None
    """
    print("Evaluate the model")


def predict(smile: str):
    """Predict the property `P1` for a given smile.

    Parameters
    ----------
    smile : str
        Molecule smile.

    Returns
    -------
    str
        Prediction of the model.
    """
    print(f"Predict property 'P1' for smile '{smile}'")
    prediction = smile
    return prediction
