"""Data preprocessing module."""

from types import SimpleNamespace

import pandas as pd
from sklearn.model_selection import train_test_split

from .feature_extractor import fingerprint_features
from .io import read_data

RANDOM_STATE = 0


def load_data(model_id: str) -> SimpleNamespace:
    """Read and preprocess data from file.

    Parameters
    ----------
    model_id : str

    Returns
    -------
    SimpleNamespace
    """
    if model_id in ["1", "2"]:
        dataset = "single"
    elif model_id == "3":
        dataset = "multi"
    df = read_data(dataset)
    data = preprocess_data(df, model_id=model_id)
    return data


def preprocess_data(df: pd.DataFrame,
                    model_id: str = "1"
                    ) -> SimpleNamespace:
    """Preprocess data frame.

    Parameters
    ----------
    df : pd.DataFrame
    model_id : str

    Returns
    -------
    SimpleNamespace
    """
    df = extract_features(df, model_id=model_id)
    df = subsample_data(df)
    data = split_data(df)
    return data


def extract_features(df: pd.DataFrame,
                     model_id: str = "1"
                     ) -> pd.DataFrame:
    """Extract features from data frame.

    Parameters
    ----------
    df : pd.DataFrame
    model_id : str

    Returns
    -------
    pd.DataFrame
    """
    if model_id == "1":
        d = pd.DataFrame(
            df["smiles"].map(lambda x:
                             list(fingerprint_features(x))).to_list(),
            index=df.index).rename(columns=lambda c: f"bit_{c}")
        d = d.join(df["P1"])
    return d


def to_features(smile, model_id="1"):
    if model_id == "1":
        features = list(fingerprint_features(smile))
    return features


def subsample_data(df: pd.DataFrame,
                   random_state: int = RANDOM_STATE
                   ) -> pd.DataFrame:
    """Subsample data because of class imbalance.

    Parameters
    ----------
    df : pd.DataFrame
    random_state : int

    Returns
    -------
    pd.DataFrame
    """
    d = df[df["P1"] == 1].sample(n=1000, random_state=random_state).append(
        df[df["P1"] == 0])
    return d


def split_data(df: pd.DataFrame,
               test_size: float = 0.1,
               val_size: float = 0.1,
               random_state: int = RANDOM_STATE
               ) -> SimpleNamespace:
    """Split data into train/val/test sets and pop target from features.

    Parameters
    ----------
    df : pd.DataFrame
    test_size : float
    val_size : float
    random_state : int

    Returns
    -------
    SimpleNamespace
    """
    d_train, d_test = train_test_split(df, test_size=test_size,
                                       stratify=df["P1"],
                                       random_state=random_state)
    d_train, d_val = train_test_split(d_train,
                                      test_size=val_size/(1 - test_size),
                                      stratify=d_train["P1"],
                                      random_state=random_state)
    x_train, y_train = pop_target(d_train)
    x_val, y_val = pop_target(d_val)
    x_test, y_test = pop_target(d_test)
    return SimpleNamespace(train=SimpleNamespace(x=x_train, y=y_train),
                           val=SimpleNamespace(x=x_val, y=y_val),
                           test=SimpleNamespace(x=x_test, y=y_test)
                           )


def pop_target(df, target="P1"):
    """Pop target from data frame.

    Parameters
    ----------
    df : pd.DataFrame
        Data frame.
    target : str
        Target column name.

    Returns
    -------
    x : pd.DataFrame
    y : pd.Series
    """
    x = df.copy()
    y = x.pop(target)
    return x, y
