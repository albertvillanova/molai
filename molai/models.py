"""Models module."""

import tensorflow as tf

from .io import read_model, write_model
from .preprocessing import to_features

# Metrics for imbalanced data, better than accuracy
METRICS = [
    tf.keras.metrics.Precision(name='precision'),
    tf.keras.metrics.Recall(name='recall'),
    tf.keras.metrics.AUC(name='auc'),
]


def load_model(model_id="1", mode="train"):
    """Load model and prepare it for train/evaluate/predict.

    Parameters
    ----------
    model_id : str
    mode : {'train', 'evaluate', 'predict'}
        Mode the model will be used in.

    Returns
    -------
    tf.keras.Model
    """
    model = create_model(model_id=model_id)
    if mode in ["evaluate", "predict"]:
        read_model(model, f"model-{model_id}")
    return model


def create_model(model_id="1") -> tf.keras.Model:
    """Create model instance and compile it.

    Parameters
    ----------
    model_id : str

    Returns
    -------
    tf.keras.Model
    """
    if model_id == "1":
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(2, activation='relu'),
            # tf.keras.layers.Dropout(0.2),
            # tf.keras.layers.Dense(2, activation='relu'),
            # tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(1, activation="sigmoid")
        ])
        model.compile(optimizer='adam',
                      loss=tf.keras.losses.BinaryCrossentropy(
                          from_logits=False),  # from_logits=True
                      metrics=METRICS)  # ["accuracy]
        # TODO: fix TensorFlow: METRICS (differently from "accuracy") do not
        # work with logits (need sigmoid activation function)
    return model


def train_model(model, data, model_id="1"):
    """Train the model with data.

    Parameters
    ----------
    model : tf.keras.Model
    data : SimpleNamespace
    model_id : str

    Returns
    -------
    tf.keras.Model
    """
    if model_id == "1":
        model.fit(data.train.x, data.train.y,
                  validation_data=(data.val.x, data.val.y),
                  batch_size=128, epochs=50)
        return model  # history,


def save_model(model, model_id="1"):
    write_model(model, f"model-{model_id}")


def evaluate_model(model, data, model_id="1"):
    """Evaluate the model with data.

    Parameters
    ----------
    model : tf.keras.Model
    data : SimpleNamespace
    model_id : str

    Returns
    -------
    dict
    """
    if model_id == "1":
        evaluation = model.evaluate(data.test.x, data.test.y, return_dict=True)
        print(evaluation)
    return evaluation


def make_prediction(model, smile, model_id="1"):
    """Make prediction for a given smile.

    Parameters
    ----------
    model : tf.keras.Model
    smile : str
    model_id : str

    Returns
    -------
    float
    """
    if model_id == "1":
        features = to_features(smile, model_id=model_id)
    prediction = model.predict([features])[0][0]
    print(f"Prediction of the model: {prediction}")
    return prediction
