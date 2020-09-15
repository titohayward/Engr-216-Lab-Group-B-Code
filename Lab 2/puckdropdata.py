
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def fin_diff( value_array,change_array):
        der_list = []
        for i in range(len(value_array)-1):
            der = (( value_array[i+1] -  value_array[i]) / (change_array[i+1] - change_array[i]))
            der_list.append(der)
        derivative = np.array([der_list])
        return derivative


class object_puck: 
    def __init__(self, csv_file, start):
        """start value"""
        df = pd.read_csv(csv_file)
        self.xpos = df["gx"][start:]
        self.ypos = df["gy"][start:]
        time_ms = df["time"][start:]
        self.time = time_ms / 1000

puck1 = object_puck("puck_drop.csv",61)
puck2 = object_puck("puck_drop_2.csv",4)
puck3 = object_puck("puck_drop_3.csv",4)




