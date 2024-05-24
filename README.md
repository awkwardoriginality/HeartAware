# HeartAware

This repository contains a Flask-based web application for predicting heart disease risk using two different models. The first model is a model used for professionals doctors to assist with diagnosing. The second model is used for individuals at home to assist with self diagnosis.

## Installation

1. **Clone the repository:**

2. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
## Usage

1. **Run the Flask application:**
    ```sh
    python3 App.py
    ```

2. **Open your web browser and navigate to by following the link in the terimal:**
    ```
    http://127.0.0.1:5000
    ```

3. **Use the web interface to input patient data and get predictions from the two models.**

## Endpoints

### Home

- **Route:** `/`
- **Method:** `GET`
- **Description:** Displays the home page with links to the prediction models.

### Model 1 Prediction

- **Route:** `/model1`
- **Method:** `GET`, `POST`
- **Description:** Accepts patient data and uses `model_professional.pkl` to predict the risk of coronary heart disease.
- **Input Fields:**
    - Age
    - Resting Blood Pressure
    - Cholesterol
    - Fasting Blood Sugar
    - Max Heart Rate
    - Sex (1 for male, 0 for female)
    - Chest Pain Type (1-4)
    - Exercise Angina (1 for yes, 0 for no)
- **Output:** Risk prediction and a brief description.

### Model 2 Prediction

- **Route:** `/model2`
- **Method:** `GET`, `POST`
- **Description:** Accepts patient data and uses `model_casual.pkl` to predict the risk of coronary heart disease.
- **Input Fields:**
    - Age
    - Cigarettes per Day
    - Height
    - Weight
    - Heart Rate
    - Current Smoker (Yes/No)
    - BP Meds (Yes/No)
    - Prevalent Hypertension (Yes/No)
    - Diabetes (Yes/No)
    - Gender (Female/Male)
    - Prevalent Stroke (Yes/No)
- **Output:** Risk prediction and a brief description.

## Files

- `app.py`: Main Flask application.
- `model_professional.pkl`: Model used in the `/model1` endpoint.
- `model_casual.pkl`: Model used in the `/model2` endpoint.
- `templates/home.html`: HTML template for the home page.
- `templates/model1.html`: HTML template for the Model 1 prediction page.
- `templates/model2.html`: HTML template for the Model 2 prediction page.
- `requirements.txt`: List of Python dependencies.