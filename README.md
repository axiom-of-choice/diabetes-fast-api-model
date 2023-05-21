# Diabetes fast api model prediction
Diabetes predictive model built with Fast API and deployed in Heroku

## Virtual Environment
``` bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -e ".[dev]"
pre-commit install
pre-commit autoupdate
```

## Directory
```
diabetes/
├── data_preprocessing.py  - data processing components
├── evaluate.py   - evaluation components
├── main.py       - training/optimization operations
├── predict.py    - inference components
├── train.py      - training components
├── model_arch.py - Define model architecture
└── utils.py      - supplementary utilities
```
## Workflow
```
TO-DO
```
## API
uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload --reload-dir diabetes --reload-dir app  # dev
gunicorn -c app/gunicorn.py -k uvicorn.workers.UvicornWorker app.api:app  # prod
