"""I/O module."""

from pathlib import Path

import pandas as pd
import tensorflow as tf

DATA_DIR = Path("data")
MODELS_DIR = Path("models")


def read_data(dataset="single") -> pd.DataFrame:
    """Read data from file.

    Parameters
    ----------
    dataset : {'single', 'multi'}
        Dataset name.

    Returns
    -------
    pd.DataFrame
    """
    if dataset == "single":
        path = DATA_DIR / "dataset_single.csv"
    elif dataset == "multi":
        path = DATA_DIR / "dataset_multi.csv"
    df = pd.read_csv(path, index_col="mol_id").reset_index(drop=True)
    return df


def write_model(model: tf.keras.Model,
                filename: str
                ) -> None:
    """Write model to file.

    Parameters
    ----------
    model : tf.keras.Model
    filename : str

    Returns
    -------
    None
    """
    path = MODELS_DIR / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    model.save_weights(path)


def read_model(model: tf.keras.Model,
               filename: str
               ) -> tf.keras.Model:
    """Read model file.

    Parameters
    ----------
    model : tf.keras.Model
    filename : str

    Returns
    -------
    tf.keras.Model
    """
    path = MODELS_DIR / filename
    model.load_weights(path)
