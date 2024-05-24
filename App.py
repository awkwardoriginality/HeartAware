from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize
import sklearn

app = Flask(__name__)
model1 = joblib.load('model_professional.pkl')
model2 = joblib.load('model_casual.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/model1', methods=['GET', 'POST'])
def model1_prediction():
    prediction = ""
    description = ""  # Initialize description outside of the POST block
    if request.method == 'POST':
        # Numeric features
        age = float(request.form['age'])
        resting_bp_s = float(request.form['resting bp s'])
        cholesterol = float(request.form['cholesterol'])
        fasting_blood_sugar = float(request.form['fasting blood sugar'])
        max_heart_rate = float(request.form['max heart rate'])

        # One-hot encoded features for sex, chest pain type and exercise angina
        sex = [1, 0] if request.form['sex'] == '1' else [0, 1]
        chest_pain_type = [0, 0, 0, 0]
        chest_pain_type[int(request.form['chest pain type']) - 1] = 1
        exercise_angina = [1, 0] if request.form['exercise angina'] == '1' else [0, 1]

        # Assemble all features in the order expected by the model
        features = [
            age, resting_bp_s, cholesterol, fasting_blood_sugar,
            max_heart_rate
        ] + sex + chest_pain_type + exercise_angina
        
        # Make a prediction
        prediction = model1.predict([features])[0]
        print("Predicion for model1 : " + str(prediction))
        # Assign descriptions based on prediction
        if prediction == 1:
            description = "You're probably gonna die"
        elif prediction == 0:
            description = "You're probably fine"
        else:
            description = "This is a general paragraph for other predictions."
            
    return render_template('model1.html', prediction=prediction, description=description)

@app.route('/model2', methods=['GET', 'POST'])
def model2_prediction():
    prediction = ""
    description = ""
    form_data = request.form  # Capture form data to repopulate form after submission

    if request.method == 'POST':
        try:
            age = float(request.form.get('age', 0))
            cigs_per_day = float(request.form.get('cigsPerDay', 0))
            height = float(request.form.get('Height', 0))
            weight = float(request.form.get('Weight', 0))
            bmi = weight / (height / 100) ** 2
            heart_rate = float(request.form.get('heartRate', 0))

            # One-hot or binary features
            current_smoker = 1 if request.form.get('currentSmoker', 'No') == 'Yes' else 0
            bp_meds = 1 if request.form.get('BPMeds', 'No') == 'Yes' else 0
            prevalent_hyp = 1 if request.form.get('prevalentHyp', 'No') == 'Yes' else 0
            diabetes = 1 if request.form.get('diabetes', 'No') == 'Yes' else 0
            gender = [1, 0] if request.form.get('Gender', 'Female') == 'Female' else [0, 1]
            prevalent_stroke = [1, 0] if request.form.get('prevalentStroke', 'No') == 'Yes' else [0, 1]

            # Combine all features in the correct order
            features = [
                age, current_smoker, cigs_per_day, bp_meds, prevalent_hyp, diabetes,
                bmi, heart_rate, gender[0], gender[1], prevalent_stroke[0], prevalent_stroke[1]
            ]
            column_names = ['age', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentHyp',
                            'diabetes', 'BMI', 'heartRate', 'Gender_Female',
                            'Gender_Male', 'prevalentStroke_no', 'prevalentStroke_yes']

            data_for_prediction = pd.DataFrame([features], columns=column_names)
            columns_to_normalise = ['age', 'cigsPerDay', 'BMI', 'heartRate']
            data_for_prediction_normalized = normalize(data_for_prediction[columns_to_normalise], axis=0)
            data_for_prediction[columns_to_normalise] = data_for_prediction_normalized

            prediction = model2.predict(data_for_prediction)[0]
            description = "High risk of heart disease." if prediction == 'yes' else "Low risk of heart disease."

        except Exception as e:
            description = "Error: " + str(e)

    return render_template('model2.html', prediction=prediction, description=description, form_data=form_data)

if __name__ == "__main__":
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)

