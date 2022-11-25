import pandas as pd
import requests

import sys
sys.path.append('../src/')

class viewMath:

    def __init__(self):
        return None

    def calc_expression(expression):
        sintaxe = "<br><br><h3>Sintaxe das expressões</h3>\
                    <p>Soma: 1 <b>+</b> 1 = 2 <br> \
                    Subtração: 2 <b>-</b> 1 = 1<br> \
                    Multiplicação: 2 <b>*</b> 2 <br> \
                    Divisão: 4 <b>/</b> 2 = 2<br> \
                    Potenciação: 2 <b>^</b> 3 = 8 ou 2<b>**</b>3 = 8<br> \
                    Raiz quadrada: <b>sqrt(</b>90<b>)</b> = 3 (3.0) <br> \
                    Resto de divisão: 3 <b>%</b> 2 = 1 <br></p>"

        if expression != "Invalid Expression Error":
            return f'<strong>{expression}</strong>' + sintaxe
        return "<strong>Expressão <strong>aritmética</strong> inválida!</strong><br><br><em>Tente utilizar a sintaxe padrão:<em>" + sintaxe