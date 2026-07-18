from src.pipeline import run_pipeline


def main():
    print("=" * 50)
    print("HDB Resale ETL Pipeline")
    print("=" * 50)

    try:
        run_pipeline()
        print("\nETL Pipeline completed successfully.")

    except Exception as e:
        print(f"\nPipeline failed: {e}")
        raise


if __name__ == "__main__":
    main()