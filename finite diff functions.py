# Juan Hayward #
### this is a general finite difference function

import numpy as np

time = np.array([0,2,4,6,8,10,12,14,16])
pos = np.array([0,0.7,1.8,3.4,5.1,6.3,7.3,8.0,8.4])

def velocity(pos_array,time_array):
    print("pos length:", len(pos_array), "time length:", len(time_array))
    if len(pos_array) != len(time_array):
        print("Array length does not match. Please check your data and try again.")
    # create vel array
    der_list = []
    for i in range(len(pos_array)-1):
        vel = (( pos_array[i+1] -  pos_array[i]) / (time_array[i+1] - time_array[i]))
        der_list.append(vel)
    derivative = np.array([der_list])
    return derivative

def acceleration(vel_array,time_array):
    # We want an adjusted time array with a new length in the same time range.
    # We assume that the time intervals are evenly spaced.
    vel_array = vel_array[0] # we want the first item
    newLength = np.array([(np.max(time_array)-np.min(time_array))/(len(vel_array)-1)])
    timeArrayNew = np.array(len(vel_array) * [newLength])

    print("velocity length:", len(vel_array), "time length:", len(timeArrayNew))
    if len(vel_array) != len(timeArrayNew):
        print("Array length does not match. Please check your data and try again.")
    # create vel array
    der_list = []
    for i in range(len(vel_array)-1):
        der_1 = ( vel_array[i+1] -  vel_array[i])
        time_1 =timeArrayNew[i]
        accel = ( der_1/ time_1)
        der_list.append(accel)
    derivative = np.array([der_list])
    return derivative

vel = velocity(pos,time)
print(vel)
acc = acceleration(vel,time)
print(acc)


