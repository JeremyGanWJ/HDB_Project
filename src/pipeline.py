from src.extract import extract_raw_data
from src.cleaning import clean_text, remove_duplicates
from src.validation import validate_data
from src.transformation import (
    calculate_remaining_lease,
    create_identifier,
)
from src.hashing import hash_identifier


def run_pipeline():


    df = extract_raw_data(
        "data/raw"
    )


    df = clean_text(df)


    clean, failed = validate_data(df)


    clean, duplicate_failed = remove_duplicates(clean)


    failed = failed.append(
        duplicate_failed
    )


    clean = calculate_remaining_lease(clean)


    transformed = create_identifier(clean)


    hashed = hash_identifier(transformed)


    clean.to_csv(
        "data/cleaned/clean.csv",
        index=False
    )


    failed.to_csv(
        "data/failed/failed.csv",
        index=False
    )


    transformed.to_csv(
        "data/transformed/transformed.csv",
        index=False
    )


    hashed.to_csv(
        "data/hashed/hashed.csv",
        index=False
    )