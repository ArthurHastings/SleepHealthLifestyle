import joblib
import numpy as np
import sklearn
import os
from pathlib import Path

def loadModel(*args): # model_nr, age, sleep_duration, quality_of_sleep, physical_activity, stress_level, heart_rate
    user_data = []
    cont = 0
    for param in args[1]:
        if cont == 0:
            model_nr = int(param)
        else:
            user_data.append(param)
        cont += 1

    model_type = {1: ["trained_model.pkl", "poly_transform.pkl"],
                2: ["trained_model_log.pkl", "scaler.pkl"]}
    
    base_path = Path(__file__).parent
    base_path[0] = "C"
    print(os.path.join(base_path, model_type[1][0]))
    model_path = os.path.join(base_path, model_type[model_nr][0])
    print("ZAZAAAAAAAAAAA", model_path)
    transform_path = os.path.join(base_path, model_type[model_nr][1])


    model = joblib.load(model_path)
    transform_conv = joblib.load(transform_path)
    if model_nr == 1:
        return calculateHealth_model_1(model, transform_conv, user_data)
    elif model_nr == 2:
        return calculateHealth_model_2(model, transform_conv, user_data)


def calculateHealth_model_1(*args): # model, transform, age, sleep_duration, quality_of_sleep, physical_activity, stress_level, heart_rate
    model5 = args[0]
    poly_transform = args[1]
    

    try:
        user_data = []
        for i in range(2, len(args)):
            user_data.append(args[i])

        user_data_poly = poly_transform.transform(user_data)

        prediction = model5.predict(user_data_poly)

        if prediction[0] < 0.5:
            return 0
        elif prediction[0] > 0.5 and prediction[0] < 1.5:
            return 1
        elif prediction[0] >= 1.5:
            return 2

    except ValueError:
        print("Invalid input. Please enter numeric values.")

def calculateHealth_model_2(*args): # model, transform, age, sleep_duration, quality_of_sleep, physical_activity, stress_level, heart_rate
    model6 = args[0]
    scaler = args[1]
    try:
        user_data = []
        for i in range(2, len(args)):
            user_data.append(args[i])

        user_data_scaled = scaler.transform(user_data)

        prediction = model6.predict(user_data_scaled)

        return prediction[0]

    except ValueError:
        print("Invalid input. Please enter numeric values.")