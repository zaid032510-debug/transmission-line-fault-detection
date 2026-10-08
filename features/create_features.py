from pathlib import Path
import pandas as pd


INPUT_FILE = Path("dataset/bus_data.csv")
OUTPUT_FILE = Path("dataset/features.csv")


def main():
    print("Loading bus data...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Loaded {len(df)} bus records")

    # Select numerical features for machine learning
    features = df[
        [
            "bus_number",
            "base_kv",
            "bus_type",
            "voltage_magnitude",
            "voltage_angle",
        ]
    ].copy()

    # Remove rows where voltage data is missing
    features = features.dropna()

    # Save feature dataset
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    features.to_csv(OUTPUT_FILE, index=False)

    print(f"Created {len(features)} feature records")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()