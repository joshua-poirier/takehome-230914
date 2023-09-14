from typing import List
from typing import Tuple

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

DATA_PATH: str = "takehome/data/zillow.csv"
DATA_COLS: List[str] = ["Living Space", "Beds", "Baths", "Zip", "Year", "List Price"]


def demo_solution() -> None:
    """A demo problem building a linear regression model on a small dataset."""
    df = _read_data()
    _, scores = _model(df=df)

    print(scores)


def _read_data() -> pd.DataFrame:
    """Read the data from a CSV file into a pandas dataframe."""
    return pd.read_csv(
        filepath_or_buffer=DATA_PATH,
        header=0,
        names=DATA_COLS,
    )


def _model(df: pd.DataFrame) -> Tuple[LinearRegression, List[float]]:
    """Create and evaluate a linear regression model.

    Args:
        df (pd.DataFrame): Dataframe to use for building the model.

    Returns:
        A tuple containing the linear regression model and a list of R-squared
        scores for the different folds of data.
    """
    # split data into predictor (X) and target (y) variables
    X = pd.DataFrame(df[["Living Space", "Beds", "Baths", "Year"]])
    y = pd.DataFrame(df["List Price"])

    # setup the model and k-folds cross validation
    model = LinearRegression()
    scores = []
    kfold = KFold(n_splits=3, shuffle=True, random_state=42)

    # create models over each fold
    for _, (train, test) in enumerate(kfold.split(X, y)):
        model.fit(X.iloc[train, :], y.iloc[train, :])
        score = model.score(X.iloc[test, :], y.iloc[test, :])
        scores.append(score)

    return model, scores
