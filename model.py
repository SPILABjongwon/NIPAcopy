import pandas as pd
import numpy as np

def result_rect(data):
    return data



# 임시로 넣어 
data_rect_regression=[{'rectifierId':"1",  'time':1602130231000, 'output_v':-0.00087, 'output_a':0.003856, 'input_v':0.94324, 'in_temp':0.32163, 'ex_temp':0.6213, 'ex_hum':0.97689},
            {'rectifierId':"1",  'time':1602130232000, 'output_v':-0.00088, 'output_a':0.003895, 'input_v':0.94321, 'in_temp':0.32143, 'ex_temp':0.6213, 'ex_hum':0.95089}, 
            {'rectifierId':"1",  'time':1602130233000, 'output_v':-0.00086, 'output_a':0.003845, 'input_v':0.94322, 'in_temp':0.32343, 'ex_temp':0.6213, 'ex_hum':0.95089},
            {'rectifierId':"1",  'time':1602130234000, 'output_v':-0.00082, 'output_a':0.003835, 'input_v':0.94323, 'in_temp':0.32443, 'ex_temp':0.6333, 'ex_hum':0.95289},
            {'rectifierId':"1",  'time':1602130235000, 'output_v':-0.00084, 'output_a':0.003765, 'input_v':0.94324, 'in_temp':0.32163, 'ex_temp':0.6213, 'ex_hum':0.95389},
            {'rectifierId':"1",  'time':1602130236000, 'output_v':-0.00086, 'output_a':0.003883, 'input_v':0.94325, 'in_temp':0.42123, 'ex_temp':0.6243, 'ex_hum':0.95589},
            {'rectifierId':"1",  'time':1602130237000, 'output_v':-0.00087, 'output_a':0.003881, 'input_v':0.94325, 'in_temp':0.52143, 'ex_temp':0.6213, 'ex_hum':0.95689},
            {'rectifierId':"1",  'time':1602130238000, 'output_v':-0.00085, 'output_a':0.003880, 'input_v':0.94327, 'in_temp':0.32143, 'ex_temp':0.6213, 'ex_hum':0.95789}, 
            {'rectifierId':"1",  'time':1602130239000, 'output_v':-0.00086, 'output_a':0.003832, 'input_v':0.94328, 'in_temp':0.32543, 'ex_temp':0.6213, 'ex_hum':0.95389},
            {'rectifierId':"1",  'time':1602130240000, 'output_v':-0.00088, 'output_a':0.003845, 'input_v':0.94325, 'in_temp':0.32643, 'ex_temp':0.6213, 'ex_hum':0.95289},
            {'rectifierId':"1",  'time':1602130241000, 'output_v':-0.00085, 'output_a':0.003875, 'input_v':0.94323, 'in_temp':0.32173, 'ex_temp':0.6233, 'ex_hum':0.95389},
            {'rectifierId':"1",  'time':1602130242000, 'output_v':-0.00089, 'output_a':0.003842, 'input_v':0.94324, 'in_temp':0.32143, 'ex_temp':0.6233, 'ex_hum':0.95289},
            {'rectifierId':"1",  'time':1602130243000, 'output_v':-0.00085, 'output_a':0.003876, 'input_v':0.94322, 'in_temp':0.32343, 'ex_temp':0.6243, 'ex_hum':0.95489},
            {'rectifierId':"1",  'time':1602130244000, 'output_v':-0.00084, 'output_a':0.003897, 'input_v':0.94324, 'in_temp':0.32443, 'ex_temp':0.2323, 'ex_hum':0.95289},
            {'rectifierId':"1",  'time':1602130245000, 'output_v':-0.00083, 'output_a':0.003854, 'input_v':0.94424, 'in_temp':0.32146, 'ex_temp':0.1213, 'ex_hum':0.95689}]
