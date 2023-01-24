import pandas as pd
import requests
import numexpr as ne

import sys
sys.path.append('../src/')

class modelMath:

    def __init__(self):
        return None

    def calc_expression(expression):
        try:
            return ne.evaluate(expression)
        except:
            return "Invalid Expression Error"
    