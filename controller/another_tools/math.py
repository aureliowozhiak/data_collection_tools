import pandas as pd
import requests

import sys
sys.path.append('../src/')

from model.another_tools.math import modelMath
from view.web.another_tools.math import viewMath

class controllerMath:

    def __init__(self):
        return None

    def main(input_value="2+2", math_type="calc_expression"):
        input_value = input_value.replace("^", "**")

        if math_type == "calc_expression":
            return f"{input_value} = {viewMath.calc_expression(modelMath.calc_expression(input_value))}"
        else:
            return ""

    