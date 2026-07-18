import pandas as pd


def profile_data(df):

    profile = pd.DataFrame({

        "datatype":
            df.dtypes.astype(str),

        "missing_count":
            df.isnull().sum(),

        "unique_values":
            df.nunique(),

        "duplicate_count":
            df.duplicated().sum()

    })


    return profile