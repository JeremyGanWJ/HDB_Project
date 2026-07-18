from dateutil.relativedelta import relativedelta
import pandas as pd


def calculate_remaining_lease(df):


    today = pd.Timestamp.today()


    df["lease_expiry"] = (
        pd.to_datetime(
            df["lease_commence_date"],
            format="%Y"
        )
        +
        pd.DateOffset(years=99)
    )


    remaining = []


    for date in df["lease_expiry"]:

        diff = relativedelta(
            date,
            today
        )


        remaining.append(
            f"{max(diff.years,0)} Years "
            f"{max(diff.months,0)} Months"
        )


    df["remaining_lease"] = remaining


    return df

import re


def create_identifier(df):


    avg_price = (
        df
        .groupby(
            [
                "month",
                "town",
                "flat_type"
            ]
        )
        ["resale_price"]
        .mean()
        .reset_index()
    )


    avg_price["price_code"] = (
        avg_price["resale_price"]
        .astype(int)
        .astype(str)
        .str[:2]
    )


    df = df.merge(
        avg_price[
            [
                "month",
                "town",
                "flat_type",
                "price_code"
            ]
        ],
        on=[
            "month",
            "town",
            "flat_type"
        ],
        how="left"
    )


    def block_code(block):

        digits = re.sub(
            r"\D",
            "",
            str(block)
        )

        return digits.zfill(3)[:3]


    df["resale_identifier"] = (
        "S"
        +
        df["block"].apply(block_code)
        +
        df["price_code"]
        +
        df["month"].str[-2:]
        +
        df["town"].str[0].str.upper()
    )


    return df