# -*- coding: utf-8 -*-
"""
@author: Isaac
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
import json

from http import HTTPStatus
from typing import Dict
from datetime import datetime
from functools import wraps
from fastapi import FastAPI, Request

from pathlib import Path
from config import config
from config.config import logger
from diabetes import main, predict
from app.schemas import PredictPayload


# Define application
app = FastAPI(
    title="Diabetes Model Prediction",
    description="Classify machine learning projects.",
    version="0.1",
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# loading the saved model
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))


def construct_response(f):
    """Construct a JSON response for an endpoint."""

    @wraps(f)
    def wrap(request: Request, *args, **kwargs) -> Dict:
        results = f(request, *args, **kwargs)
        response = {
            "message": results["message"],
            "method": request.method,
            "status-code": results["status-code"],
            "timestamp": datetime.now().isoformat(),
            "url": request.url._url,
        }
        if "data" in results:
            response["data"] = results["data"]
        return response

    return wrap


@app.on_event("startup")
def load_artifacts():
    global artifacts
    run_id = open(Path(config.CONFIG_DIR, "run_id.txt")).read()
    # artifacts = main.load_artifacts(model_dir=config.MODEL_DIR)
    logger.info("Ready for inference!")


@app.get("/", tags=["General"])
@construct_response
def _index(request: Request) -> Dict:
    """Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response


@app.get("/performance", tags=["Performance"])
@construct_response
def _performance(request: Request, filter: str = None) -> Dict:
    """Get the performance metrics."""
    performance = artifacts["performance"]
    data = {"performance": performance.get(filter, performance)}
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": data,
    }
    return response


@app.get("/args", tags=["Arguments"])
@construct_response
def _args(request: Request) -> Dict:
    """Get all arguments used for the run."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {
            "args": vars(artifacts["args"]),
        },
    }
    return response


@app.get("/args/{arg}", tags=["Arguments"])
@construct_response
def _arg(request: Request, arg: str) -> Dict:
    """Get a specific parameter's value used for the run."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {
            arg: vars(artifacts["args"]).get(arg, ""),
        },
    }
    return response


@app.post("/predict", tags=["Prediction"])
@construct_response
def _predict(request: Request, payload: PredictPayload) -> Dict:
    """Predict tags for a list of texts."""
    texts = [item.text for item in payload.texts]
    predictions = predict.predict(texts=texts, artifacts=artifacts)
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"predictions": predictions},
    }
    return response


# @app.post('/diabetes_prediction')
# def diabetes_pred(input_parameters : model_input):
#
#     input_data = input_parameters.json()
#     input_dictionary = json.loads(input_data)
#
#     preg = input_dictionary['Pregnancies']
#     glu = input_dictionary['Glucose']
#     bp = input_dictionary['BloodPressure']
#     skin = input_dictionary['SkinThickness']
#     insulin = input_dictionary['Insulin']
#     bmi = input_dictionary['BMI']
#     dpf = input_dictionary['DiabetesPedigreeFunction']
#     age = input_dictionary['Age']
#
#
#     input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
#
#     prediction = diabetes_model.predict([input_list])
#
#     if prediction[0] == 0:
#         return 'The person is not Diabetic'
#
#     else:
#         return 'The person is Diabetic'
