from pathlib import Path
import pandas as pd


INPUT_FILE = Path("dataset/features.csv")
OUTPUT_FILE = Path("dataset/ml_data.csv")


def main():
    print("Loading feature data...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Loaded {len(df)} records")

    # For now, create a basic target column.
    # 0 = normal operating condition
    # 1 = abnormal condition
    #
    # We will replace this with actual fault labels
    # when the fault simulation data is prepared.

    df["fault"] = 0

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Created ML dataset with {len(df)} records")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()