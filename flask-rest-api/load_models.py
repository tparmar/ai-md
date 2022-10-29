from typing import final
from unicodedata import name
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
import glob


#import models
model_dt = pickle.load(open("models/Decision_Tree_Model.sav", 'rb'))
model_et = pickle.load(open("models/Extra_Tree_Model.sav", 'rb'))
model_knn = pickle.load(open("models/KNeighbors_Model.sav", 'rb'))
model_rf = pickle.load(open("models/Random_Forest_Model.sav", 'rb'))

#import data to create disease dictionary
DATA_PATH = "input/Training.csv"
files = os.path.join("input", "*.csv")
files = glob.glob(files)

data = pd.concat(map(pd.read_csv, files), ignore_index=True).dropna(axis=1)
# data = pd.read_csv(DATA_PATH).dropna(axis = 1)
encoder = LabelEncoder()
encoder.fit(data["prognosis"])
data["prognosis"] = encoder.transform(data["prognosis"])

X = data
y = data.pop("prognosis")


symptoms = X.columns.values

# Creating a symptom index dictionary to encode the
# input symptoms into numerical form
symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

data_dict = {"symptom_index":symptom_index,"predictions_classes":encoder.classes_}

def symptoms_index():
    return symptom_index
#predict disease function using all models
def predictDisease(symptoms):
    symptoms = symptoms.split(",")
# creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        print(symptoms)
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1
    for i in range(len(input_data)):
        if input_data[i] > 0:
            print(X.columns[i])
# reshaping the input data and converting it
# into suitable format for model predictions
    input_data = np.array(input_data).reshape(1,-1)
    predictions_rf = model_rf.predict_proba(input_data)
    predictions_knn = model_knn.predict_proba(input_data)
    predictions_et = model_et.predict_proba(input_data)
    predictions_dt = model_dt.predict_proba(input_data)
    
    final_preds_rf = []
    final_preds_knn = []
    final_preds_et = []
    final_preds_dt = []

    final_dict = {}
    
    #Random Forest Predictions
    for i in range(len(predictions_rf)):
        for n in range(len(predictions_rf[0])):
            if predictions_rf[i][n] > 0:
                final_preds_rf.append([data_dict["predictions_classes"][n], predictions_rf[i][n]])
                new_disease = Disease(data_dict["predictions_classes"][n], predictions_rf[i][n])
                final_dict[new_disease.getName()] = new_disease.getProba()
        
    #KNN Predictions    
    for i in range(len(predictions_knn)):
        for n in range(len(predictions_knn[0])):
            if predictions_rf[i][n] > 0:
                final_preds_knn.append([data_dict["predictions_classes"][n], predictions_knn[i][n]])

    
    #Extra Tree Predictions
    for i in range(len(predictions_et)):
        for n in range(len(predictions_et[0])):
            if predictions_et[i][n] > 0:
                final_preds_et.append([data_dict["predictions_classes"][n], predictions_et[i][n]])
    
    #Decision Tree Predictions
    for i in range(len(predictions_dt)):
        for n in range(len(predictions_dt[0])):
            if predictions_dt[i][n] > 0:
                final_preds_dt.append([data_dict["predictions_classes"][n], predictions_dt[i][n]])

    final_preds_rf = sorted(final_preds_rf, key=lambda x: x[1], reverse=True)
    final_preds_knn = sorted(final_preds_knn, key=lambda x: x[1], reverse=True)
    final_preds_dt = sorted(final_preds_dt, key=lambda x: x[1], reverse=True)
    final_preds_et = sorted(final_preds_et, key=lambda x: x[1], reverse=True)

    # print(final_preds_rf)
    # print(final_preds_knn)
    # print(final_preds_dt)
    # print(final_preds_et)
    # return [final_preds_rf, final_preds_knn, final_preds_dt, final_preds_et]
    # final_dict = {}
    # for i in range(len(final_preds_rf)):
    #     for n in range(len(final_preds_rf[i])):
    #         final_dict[final_preds_rf[i][n][0]] = final_preds_rf[i][n][1]
    # print(final_dict)

    sorted_dict = {}
    sorted_values = sorted(final_dict.values(), reverse=True)

    for i in sorted_values:
        for k in final_dict.keys():
            if final_dict[k] == i:
                sorted_dict[k] = final_dict[k]
                break

    #return final_dict
    return sorted_dict

class Disease:
    def __init__(self, name: str, proba):
        self.name = name
        self.proba = proba
    
    def getName(self):
        return self.name

    def getProba(self):
        return self.proba


# predictDisease("Chills,Vomiting,Headache,Nausea,Muscle Weakness")


