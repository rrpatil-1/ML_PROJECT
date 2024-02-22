from flask import Flask, request,render_template,jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
from src.logger import logging

application=Flask(__name__)
app=application
#home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
        
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(pred_df)
        return render_template('home.html',results=pred[0])
    

@app.route('/predictscore',methods=['POST'])
def predictscore():
    
    body=request.get_json()
    logging.info(f"request received:{body}")
    # print(body)
    
    data = CustomData(
            gender=body['gender'],
            race_ethnicaity=body['race_ethnicaity'],
            parental_level_of_education=body['parental_level_of_education'],
            lunch=body['lunch'],
            test_preparation_course=body['test_preparation_course'],
            reading_score=float(body['reading_score']),
            writing_score=float(body['writing_score'])
        )
        
    pred_df = data.get_data_as_data_frame()
    logging.info(pred_df)
        
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(pred_df)
    return {'results':pred[0]}
    
@app.errorhandler(500)
def server_error(error):
    logging.info(error)
    return 'Internal Server Error', 500
    

if __name__ =="__main__":
    app.run(host="0.0.0.0",debug=False)