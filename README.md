# Customer Review Classifier

**Customer Review Classifier** is a machine learning project designed to analyze and classify customer reviews into three sentiment categories: Positive, Negative, and Neutral.

The project leverages advanced NLP techniques, including text preprocessing (cleaning, lemmatization, stopword removal) and powerful models like BERT with LoRA fine-tuning as well as classical machine learning models such as SGDClassifier.

Additionally, the project uses a **MySQL database** to store user reviews and the predictions from the models, making it easier to track and analyze sentiment data over time.

Users can input a review and quickly get a sentiment prediction, making it useful for businesses to understand customer feedback, monitor satisfaction, and make data-driven decisions.

## Data

The original data comes from the [Yelp Open Dataset](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset), a rich resource containing millions of reviews.

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