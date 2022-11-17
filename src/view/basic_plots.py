import matplotlib.pyplot as plt
#%matplotlib inline

class BasicPlots:

    def __init__(self):
        return None

    def xy_graph(X, y, ylabel = "", xlabel = ""):
        plt.plot(X, y)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.show()

    