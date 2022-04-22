import pandas as pd


def find_groups_with_value(df: pd.DataFrame, b_val: str) -> pd.DataFrame:

    return df[df["b"] == int(b_val)]
