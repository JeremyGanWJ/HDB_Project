def clean_text(df):

    text_columns = [
        "town",
        "flat_type",
        "flat_model"
    ]


    for col in text_columns:

        df[col] = (
            df[col]
            .str.strip()
            .str.upper()
        )


    return df

def remove_duplicates(df):

    key_columns = [
        col
        for col in df.columns
        if col != "resale_price"
    ]


    df = df.sort_values(
        "resale_price",
        ascending=False
    )


    duplicate_records = df[
        df.duplicated(
            key_columns,
            keep="first"
        )
    ]


    cleaned_df = df.drop_duplicates(
        key_columns,
        keep="first"
    )


    return cleaned_df, duplicate_records