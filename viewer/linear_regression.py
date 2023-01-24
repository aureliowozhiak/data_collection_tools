import matplotlib.pyplot as plt
import streamlit as st

class ViewerLinearRegressionForecast():
    
    def __init__(self):
        pass

    def plot(self, X_train, y_train, reg):
            
        fig, ax = plt.subplots()
        ax.scatter([1, 2, 3], [1, 2, 3])

        ax.scatter(X_train, y_train, color = 'blue')
        plt.plot(X_train, reg.predict(X_train), color = 'red')
        plt.title('Linear Regression - Train')
        plt.xlabel('X')
        plt.ylabel('Y')

        st.pyplot(fig)