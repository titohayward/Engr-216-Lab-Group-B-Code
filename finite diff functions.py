# Juan Hayward #
### this is a general finite difference function

import numpy as np

time = np.array([0,2,4,6,8,10,12,14,16])
pos = np.array([0,0.7,1.8,3.4,5.1,6.3,7.3,8.0,8.4])

def fin_diff(value_array,time_arrray):
    """ Input is arrays for both position and time """
    # Test array length
    print("value array:", len(value_array), "time array:", len(time_arrray))
    if len(value_array) != len(time_arrray):
        print("Array length does not match. Please check your data and try again.")
    # create vel array
    der_list = []
    for i in range(len(value_array)-1):
        vel = (( value_array[i+1] -  value_array[i]) / (time_arrray[i+1] - time_arrray[i]))
        der_list.append(vel)
    derivative = np.array([der_list])
    return derivative

print(fin_diff(pos,time))

def error_findiff():
    pass