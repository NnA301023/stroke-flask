import pickle
import flask 
from flask import Flask, render_template, url_for, request
from numpy.random import randint, choice
import pandas as pd
import numpy as np
import os

#load saved model
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
model_url = os.path.join(SITE_ROOT, 'model.pkl')
def load_pkl(fname):
    with open(fname, 'rb') as f:
        obj = pickle.load(f)
    return obj
#model = load_pkl(model_url)

result = {'PHASE 1': ['Breathing Exercise',
  'Breathing Exercise',
  'Breathing Exercise',
  'Breathing Exercise',
  'Breathing Exercise'],
 'PHASE 2': ['Light Exercise',
  'Light Exercise',
  'Light Exercise',
  'Light Exercise',
  'Light Exercise'],
 'PHASE 3': ['Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities'],
 'PHASE 4': ['Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities'],
 'PHASE 5': ['Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities'],
 'PHASE 6': ['Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities'],
 'PHASE 7': ['Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities'],
 'PHASE 8': ['Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities'],
 'PHASE 9': ['Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities'],
 'PHASE 10': ['Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities',
  'Everyday Activities'],
 'PHASE 11': ['Standing Walking',
  'Standing Walking',
  'Standing Walking',
  'Standing Walking',
  'Standing Walking'],
 'PHASE 12': ['Standing Walking',
  'Standing Walking',
  'Standing Walking',
  'Standing Walking',
  'Standing Walking'],
 'PHASE 13': ['Standing Walking',
  'Standing Walking',
  'Standing Walking',
  'Standing Walking',
  'Standing Walking'],
 'PHASE 14': ['Strength Control',
  'Standing Walking',
  'Strength Control',
  'Strength Control',
  'Standing Walking'],
 'PHASE 15': ['Strength Control',
  'Strength Control',
  'Strength Control',
  'Strength Control',
  'Strength Control'],
 'PHASE 16': ['Strength Control',
  'Strength Control',
  'Strength Control',
  'Strength Control',
  'Strength Control'],
 'PHASE 17': ['Strength Control',
  'Strength Control',
  'Strength Control',
  'Strength Control',
  'Strength Control'],
 'PHASE 18': ['Strength Control',
  'Strength Control',
  'Strength Control',
  'Strength Control',
  'Strength Control'],
 'PHASE 19': ['Facial Exercise',
  'Strength Control',
  'Facial Exercise',
  'Facial Exercise',
  'Strength Control'],
 'PHASE 20': ['Speech Training',
  'Facial Exercise',
  'Speech Training',
  'Speech Training',
  'Facial Exercise'],
 'PHASE 21': ['Return to',
  'Speech Training',
  'Return to',
  'Return to',
  'Speech Training'],
 'PHASE 22': ['Rest', 'Return to', 'Rest', 'Rest', 'Return to']}

disease = []
num_disease = []
app = Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html", judul="Home")

@app.route("/predict", methods=["POST"])
def predict():
    smoke = request.form["smoke"]
    if smoke == "smokes":
        disease.append("SMOKER")
        num_disease.append(0)
        
    obey = int(request.form["bmi"])
    if obey > 30 and obey < 35:
        disease.append("OBESITY I")
        num_disease.append(1)
    elif obey > 35 and obey < 40:
        disease.append("OBESITY II")
        num_disease.append(1)
    elif obey > 40:
        disease.append("OBESITY III")
        num_disease.append(1)
        
    heart = request.form["heart"]
    if heart == 'yes':
        disease.append('HEART DISEASE')  
        num_disease.append(2)
        
    hyper = request.form["hypertension"]
    if hyper == "yes":
        disease.append("HYPERTENSION")
        num_disease.append(3)
        
    diabetes = int(request.form["glucose"])
    if diabetes > 199:
        disease.append("DIABETES")
        num_disease.append(4)

    pred = 1#randint(0,2)
    return render_template('index.html',prediction_text=pred, dis=",".join(disease))

@app.route("/expert")
def expert():
    return render_template("expert-review.html", judul="Expert Review")

@app.route("/expert_review", methods=["POST"])
def expert_review():
    PHASE,HEALTH,EXERCISE = "","",""
    FASE = request.form["phase"]
    PROGRESS =  int(request.form.get("proses", False))
    if PROGRESS > 70 :
        PHASE = FASE.split(' ')[0] +" "+str(int(FASE.split(" ")[1])+1)
    else:
        PHASE = FASE
    HEALTH = choice([str(x)+"%" for x in range(30,90,10)])
    EXERCISE = result[PHASE][0]
    return render_template("expert-review.html", judul="Expert Review", ph=PHASE, health=HEALTH, exe=EXERCISE)

@app.route("/exercise")
def exercise():
    return render_template("Exercise.html", judul="Exercise")
    
@app.route("/health")
def health():
    return render_template("Health.html", judul="Health")
    
@app.route("/module")
def module():
    return render_template("Module.html", judul="Module")
    
if __name__ == '__main__':
	app.run(debug=True, use_reloader=False)
