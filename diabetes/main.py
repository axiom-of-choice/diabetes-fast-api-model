import typer

app = typer.Typer()


@app.command()
def elt_data():
    ...


@app.command()
def train_model(
    args_fp: str = "config/args.json",
    experiment_name: str = "baselines",
    run_name: str = "sgd",
    test_run: bool = False,
) -> None:
    ...


@app.command()
def optimize(
    args_fp: str = "config/args.json",
    study_name: str = "optimization",
    num_trials: int = 20,
) -> None:
    ...


@app.command()
def predict(text: str = "", run_id: str = None) -> None:
    ...
