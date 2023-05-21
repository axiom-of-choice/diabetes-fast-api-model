import pandas as pd
import mlflow
from config.config import logger
from diabetes import evaluate, predict, data_preprocessing
from argparse import Namespace
from typing import Dict
from utils import set_seeds
from model_arch import classifier
from sklearn.metrics import log_loss


def train(args: Namespace, df: pd.DataFrame) -> Dict:
    """Train model on data

    Args:
        args (Namespace): Arguments to use for training
        df (pd.DataFrame): Data for training

    Returns:
        Dict: Artifacts from the run
    """
    ##Setup seeds
    set_seeds()
    ##Preprocess data
    # All the data is very clean so we skip this step

    ## Split data

    X_train, X_test, y_train, y_test = data_preprocessing.split_data(df)

    ##Train model
    for epoch in range(args.num_epochs):
        classifier.fit(X_train, y_train)
        train_loss = log_loss(y_train, classifier.predict_proba(X_train))
        if not epoch % 10:
            logger.info(f"Epoch: {epoch:02d} | " f"train_loss: {train_loss:.5f}, ")
        mlflow.log_metrics({"train_loss": train_loss, "val_loss": val_loss}, step=epoch)
