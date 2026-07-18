import hashlib


def hash_identifier(df):


    df["hashed_identifier"] = (
        df["resale_identifier"]
        .apply(
            lambda x:
            hashlib.sha256(
                x.encode()
            ).hexdigest()
        )
    )


    return df