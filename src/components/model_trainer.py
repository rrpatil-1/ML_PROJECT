import sys
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import evaluate_model, save_object
from dataclasses import dataclass
import os

@dataclass
class ModelTrainerConfig:
    train_model_file_path = os.path.join('artifact','model.pkl')
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        
    def initiate_model_trainer(self,train_arry,test_arry):
        try:
            logging.info('spliting tarining and test input data')
            X_train,Y_train,X_test,Y_test=(
                train_arry[:,:-1],
                train_arry[:,-1],
                test_arry[:,:-1],
                test_arry[:,-1]
                )
            models ={
                    "Linear Regression":LinearRegression(),
                    "K-Neighbors Regression":KNeighborsRegressor(),
                    "Decision Tree":DecisionTreeRegressor(),
                    "Random Forest":RandomForestRegressor(),
                    "XGBRegressor":XGBRegressor(),
                    "CatBoostRegressor":CatBoostRegressor(verbose=False),
                    "AdaBoostRegressor":AdaBoostRegressor(),
                    "GradientBoostTrgressor":GradientBoostingRegressor()}
            
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "GradientBoostTrgressor":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "K-Neighbors Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoostRegressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoostRegressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }
            
            model_report:dict=evaluate_model(X_train,Y_train,X_test,Y_test,models,params)
            
            #To get best model score
            best_model_score = max(model_report.values())
            
            #To get best model name from  dict
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            
            best_model = models[best_model_name]
            
            if best_model_score<0.6:
                raise CustomException('No best model found',sys)
            
            logging.info('best model found on training and testing dataset')
            
            save_object(file_path=self.model_trainer_config.train_model_file_path,
                        obj=best_model)
            
            Y_predict = best_model.predict(X_test)
            r2score = r2_score(Y_test,Y_predict)
            
            return r2score
            
            
            
        except Exception as e:
            raise CustomException(e,sys)