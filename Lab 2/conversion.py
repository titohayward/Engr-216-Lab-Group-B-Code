# Juan Hayward #
### this is a general finite difference function

import numpy as np
import pandas as pd

def fin_diff(value_array,change_array):
    """ Input can be arrays or lists for both position and time.
        note: First input is the values,
              Second input is change.    """
    # Test array length
    print("value array:", len(value_array), "change array:", len(change_array))
    if len(value_array) != len(change_array):
        print("Array length does not match. Please check your data and try again.")
    # create vel array
    der_list = []
    for i in range(len(value_array)-1):
        vel = (( value_array[i+1] -  value_array[i]) / (change_array[i+1] - change_array[i]))
        der_list.append(vel)
    derivative = np.array([der_list])
    return derivative

df = pd.read_csv("meter_stick.csv")
px = df['px']
py = df['py']
yx = df['yx']
yy = df['yy']
for i in  px:
    print(i)





