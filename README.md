# transmission-line-fault-detection

## Project Description

Machine Learning-Based Transmission Line Fault Detection Using the IEEE 68-Bus System

This project focuses on developing an automated transmission-line fault detection system using machine learning. The IEEE 68-bus test system is used as the power-system model, with bus and transmission-line information obtained from the available PSS/E .RAW and .DYR files.

Since PSS/E is not installed, the project uses the open-source ANDES power-system simulation tool to load and simulate the IEEE 68-bus system. The simulation data is used to generate normal operating conditions and transmission-line fault conditions.

The project follows a complete pipeline:

IEEE 68-Bus System → Power-System Simulation → Data Extraction → Feature Engineering → Fault Labeling → Machine Learning → Fault Detection

The extracted electrical parameters, such as bus voltage magnitude, voltage angle, and other relevant system measurements, are processed into a machine-learning dataset. Fault cases will then be labeled according to their operating condition.

## Planned Models

- Decision Tree
- Random Forest

## Main Objective

The main objective is to develop a data-driven transmission-line fault detection system that can analyze electrical-system measurements and automatically detect abnormal or fault conditions, reducing the dependence on manual analysis and providing a foundation for faster power-system protection and monitoring.

## Current Status

The initial data-processing pipeline is already working:

- IEEE 68-bus RAW data → 68 bus records
- Feature generation → 68 feature records
- ML dataset generation → 68 records
- ANDES 2.0.0 installed successfully
- The next step is to simulate the IEEE 68-bus system and generate actual normal and fault-condition data

> Important: the current `fault = 0` assignment is a temporary placeholder and will be replaced with genuine fault labels after simulation data is generated.

## Repository Structure

- `dashboard/` – dashboard application and visuals
- `dataset/` – raw and processed dataset files
- `documentation/` – project documentation and report files
- `features/` – feature engineering scripts
- `machine_learning/` – model training and evaluation code
- `simulation/` – IEEE 68-bus simulation inputs and cases
- `reports/` – project reports and summaries
- `results/` – output files and generated predictions

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Run the preprocessing and model scripts

Example:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
```

## GitHub Upload / Push

```bash
git add .
git commit -m "Initial project upload"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

## License

This project is currently without a formal license. Add a license if you plan to publish the project publicly.

## Notes

This repository is structured to support the simulation pipeline, feature extraction, model training, and dashboard presentation for transmission-line fault detection.

