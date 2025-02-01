import joblib
import numpy as np
import sklearn
from pathlib import Path

def loadModel():
    model5 = joblib.load(Path("C:/Users/User/Desktop/PythonAICourse/Modul2/SleepHealthLifestyle/trained_model.pkl")) 
    polynom_conv = joblib.load(Path("C:/Users/User/Desktop/PythonAICourse/Modul2/SleepHealthLifestyle/poly_transform.pkl"))
    return model5, polynom_conv

def calculateHealth(age, sleep_duration, quality_of_sleep, physical_activity, stress_level, heart_rate):
    model5, polynom_conv = loadModel()

    try:
        user_data = np.array([[age, sleep_duration, quality_of_sleep, physical_activity, stress_level, heart_rate]])

        user_data_poly = polynom_conv.transform(user_data)

        prediction = model5.predict(user_data_poly)

        if prediction[0] < 0.5:
            return 0
        elif prediction[0] > 0.5 and prediction[0] < 1.5:
            return 1
        elif prediction[0] >= 1.5:
            return 2

    except ValueError:
        print("Invalid input. Please enter numeric values.")

