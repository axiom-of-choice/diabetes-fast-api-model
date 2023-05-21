import pandas as pd
import numpy as np
from typing import Tuple
from sklearn.model_selection import train_test_split


def get_data_splits(X: pd.DataFrame, y: pd.Series, train_size: float = 0.8) -> Tuple:
    """Generate data splits

    Args:
        X (pd.DataFrame): Input features
        y (pd.Series): Target feature
        train_size (float, optional): Porportion of data to use for training. Defaults to 0.8.

    Returns:
        Tuple: Data splits as arrays
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=train_size, stratify=y
    )
    return X_train, X_test, y_train, y_test
