# Machine Learning-Based Transmission Line Fault Detection Using the IEEE 68-Bus System

This project develops a machine-learning-based transmission line fault detection system for the IEEE 68-bus test system. The workflow starts from the IEEE 68-bus power network, advances through simulation and feature extraction, and ends with fault classification using machine learning models.

## Project Overview

The project follows this pipeline:

IEEE 68-Bus System → Power-System Simulation → Data Extraction → Feature Engineering → Fault Labeling → Machine Learning → Fault Detection

The dataset is built from electrical measurements such as bus voltage magnitude, voltage angle, and other system parameters. Fault cases are labeled according to operating conditions and used to train classification models.

## Planned Models

- Decision Tree
- Random Forest

## Current Status

The initial data-processing pipeline is working:

- IEEE 68-bus RAW data → 68 bus records
- Feature generation → 68 feature records
- ML dataset generation → 68 records
- ANDES 2.0.0 installed successfully

The next stage is to simulate the IEEE 68-bus system and generate real normal and fault-condition datasets.

> Note: the current `fault = 0` assignment is a placeholder and will be replaced with real fault labels once the simulation data is available.

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
3. Install the required Python packages
4. Run the preprocessing and model scripts

Example:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## GitHub Upload Checklist

- Create a GitHub repository
- Initialize Git locally
- Add the project files
- Commit the changes
- Push to GitHub

Example:

```bash
git init
git add .
git commit -m "Initial project upload"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

## License

This project is currently without a formal license. Add a license file if you plan to publish it publicly on GitHub.

## Notes

This repository is structured to support further development of the simulation pipeline, feature extraction, model training, and dashboard presentation.
