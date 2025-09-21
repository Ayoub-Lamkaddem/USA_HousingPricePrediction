# USA Housing Price Prediction

**USA Housing Price Prediction** is a machine learning project designed to predict house prices in the United States based on key features such as average area income, house age, number of rooms, number of bedrooms, and area population.

The project leverages regression models like Ridge Regression and SVR, along with data preprocessing (handling missing values, outliers, normalization) to ensure robust predictions.

Additionally, the project integrates a Streamlit interface, allowing users to input housing features and instantly get a price prediction. This makes it useful for individuals, real estate agents, and businesses to better understand housing market trends and make data-driven decisions.

## Data

The original dataset comes from [Kaggle](https://www.kaggle.com/datasets/farhankarim1/usa-house-prices), specifically the USA Housing dataset, which contains 5,000 entries with features such as average area income, house age, number of rooms, number of bedrooms, and area population.

## Installation

### 1- Clone the repository
```bash
git clone https://github.com/Ayoub-Lamkaddem/USA_HousingPricePrediction.git
cd USA_HousingPricePrediction
```

### 2- Install **uv**
Before anything, install uv depending on your OS:

- **For Windows (PowerShell):**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
- **For macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
### 3- Create a virtual environment (recommended) and Install dependencies:
We need two environments: **frontend** and **ml**.

For each folder, run:
- **frontend folder**
```bash
cd frontend
uv init --python 3.12
uv venv
uv sync
cd ..
```
- **ML folder**
```bash
cd ml
uv init --python 3.12
uv venv
uv sync
cd ..
```

### 4- Activate the virtual environment and run the project:
- **Frontend folder**
```bash
cd frontend
# Windows
    ./venv/scripts/activate

# Linux or Mac
    source .venv/bin/activate

# Run the frontend
    streamlit run app.py
```