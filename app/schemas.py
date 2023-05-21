from typing import List
from fastapi import Query
from pydantic import BaseModel, validator


class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


class PredictPayload(BaseModel):
    inputs: List[model_input]

    @validator("inputs")
    def list_must_not_be_empty(cls, value):
        if not len(value):
            raise ValueError("List of inputs to classify cannot be empty.")
        return value

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Pregnancies": "1",
                        "Glucose": "85",
                        "BloodPressure": "66",
                        "SkinThickness": "29",
                        "Insulin": "0",
                        "BMI": "26.6",
                        "DiabetesPedigreeFunction": "0.351",
                        "Age": "31",
                    },
                    {
                        "Pregnancies": "2",
                        "Glucose": "90",
                        "BloodPressure": "66",
                        "SkinThickness": "29",
                        "Insulin": "0",
                        "BMI": "26.6",
                        "DiabetesPedigreeFunction": "0.351",
                        "Age": "32",
                    },
                ]
            }
        }
