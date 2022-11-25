import pandas as pd
import requests

import sys
sys.path.append('../src/')

from model.another_tools.math import modelMath
from view.web.another_tools.math import viewMath

class controllerMath:

    def __init__(self):
        return None

    def calc_expression(input_value, scraper_type):
        return f"{input_value} = {viewMath.calc_expression(modelMath.calc_expression(input_value))}"

    