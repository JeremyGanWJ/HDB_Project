from pathlib import Path
import pandas as pd


def extract_raw_data(path):
    """
    Read all CSV files from raw folder
    """

    files = list(Path(path).glob("*.csv"))

    if not files:
        raise Exception("No CSV files found")


    dataframe_list = []

    for file in files:
        print(f"Loading {file.name}")

        df = pd.read_csv(file)
        dataframe_list.append(df)


    master_df = pd.concat(
        dataframe_list,
        ignore_index=True,
        sort=False
    )


    return master_df