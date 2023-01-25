import matplotlib.pyplot as plt
#%matplotlib inline

import uuid
import os

class BasicPlots:

    def __init__(self):
        return None

    def line_graph(X, y, xlabel = "", ylabel = ""):
        plt.plot(X, y)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.show()

    def bar_graph(X, y, xlabel = "", ylabel = ""):
        plt.bar(X, y)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        return plt

    
    def generate_image(plot_image : plt):
        imagem_format = "svg"
        file_name = uuid.uuid4()
        file_path = f"../src/view/web/tmp_files/{file_name}.{imagem_format}"
        
        plot_image.savefig(file_path, format=imagem_format)

        return file_path

    