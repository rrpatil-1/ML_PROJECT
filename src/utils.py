import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(X_train,Y_train,X_test,Y_test,models,param):
    try:
        report= {}
        
        for StrModel in models:
            model = models[StrModel]
            para=param[StrModel]
            
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,Y_train)
            
            model.set_params(**gs.best_params_)
            
            model.fit(X_train,Y_train)
            
            y_train_predict = model.predict(X_train)
            y_test_predict = model.predict(X_test)
            
            train_score = r2_score(Y_train,y_train_predict)
            test_score = r2_score(Y_test,y_test_predict)
            
            report[StrModel]=test_score
        return report
    
    except Exception as e:
        raise CustomException(e,sys)
        
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)