from pathlib import Path
import csv

RAW_FILE = Path("simulation/raw/PSSE/NETS-NYPS 68 Bus System.RAW")
OUTPUT_FILE = Path("dataset/bus_data.csv")


def clean_field(value):
    return value.strip().strip("'").strip('"').strip()


def parse_bus_data(lines):
    buses = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("0 /"):
            break

        parts = [clean_field(x) for x in line.split(",")]

        if len(parts) < 9:
            continue

        try:
            bus_number = int(parts[0])
            bus_name = parts[1]
            base_kv = float(parts[2])
            bus_type = int(parts[3])
            vm = float(parts[7])
            va = float(parts[8])

            buses.append({
                "bus_number": bus_number,
                "bus_name": bus_name,
                "base_kv": base_kv,
                "bus_type": bus_type,
                "voltage_magnitude": vm,
                "voltage_angle": va,
            })

        except (ValueError, IndexError):
            continue

    return buses

def main():
    with open(RAW_FILE, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    buses = parse_bus_data(lines)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "bus_number",
                "bus_name",
                "base_kv",
                "bus_type",
                "voltage_magnitude",
                "voltage_angle",
            ],
        )
        writer.writeheader()
        writer.writerows(buses)

    print(f"Parsed {len(buses)} buses")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()