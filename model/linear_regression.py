from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ModelLinearRegressionForecast():

    def __init__(self, df, periods = 3, column_of_date = 'date', column_to_predict = 'demand'):
        self.df = df
        self.column_to_predict = column_to_predict
        self.column_of_date = column_of_date
        self.periods = periods

    def predict(self):
        self.df[self.column_of_date] = pd.to_datetime(self.df[self.column_of_date])
        self.df.set_index(self.column_of_date, inplace=True)

        # Criação do modelo de previsão
        X = np.array(list(range(len(self.df)))).reshape(-1, 1)
        y = self.df[self.column_to_predict].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        self.X_train = X_train
        self.y_train = y_train

        self.X_test = X_test
        self.y_test = y_test

        self.reg = LinearRegression().fit(X_train, y_train)
        # Previsão dos próximos períodos
        X_forecast = np.array(list(range(len(self.df),len(self.df)+self.periods))).reshape(-1, 1)
        forecast = self.reg.predict(X_forecast)
        return forecast, self.X_train, self.y_train, self.reg

