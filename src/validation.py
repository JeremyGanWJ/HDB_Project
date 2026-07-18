import pandas as pd


def validate_data(df):

    failed_records = []


    # Date validation

    date_check = pd.to_datetime(
        df["month"],
        format="%Y-%m",
        errors="coerce"
    )


    invalid_date = df[
        date_check.isna()
    ]

    failed_records.append(
        invalid_date
    )


    # Town validation

    valid_towns = set(
        df["town"]
        .dropna()
        .unique()
    )


    invalid_town = df[
        ~df["town"].isin(valid_towns)
    ]


    failed_records.append(
        invalid_town
    )


    failed_df = pd.concat(
        failed_records
    ).drop_duplicates()


    clean_df = df.drop(
        failed_df.index
    )


    return clean_df, failed_df