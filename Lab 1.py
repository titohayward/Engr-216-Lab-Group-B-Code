# Juan Hayward
# Karin testing first change proposal - this comment is the change proposal :) 9/6/2020 11:30am
# Engr Lab 1: Error Propogation
# Data code

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# import the csv into pandas for easy access of information
df = pd.read_csv("example_4.csv")

def error_add(*errors):
      """ 
      This function computes error for adding and subtracting values.
      For this lab the assumed error value is 3 px. 

      """
      error = np.array([errors])
      return np.average(np.sqrt(np.sum((error)**2)))

def error_mult(error, value, val_1):
      """
      This function takes in:
      1. an array of errors
      2. an array of values
      3. a known value for the calculation answer that we are finding the uncertainty of.

      """
      return np.average(val_1 * np.sqrt(np.sum((error/value)**2)))

def error_mult_mod(error, value, val_1):
      """
      This function takes in:
      1. an array of errors
      2. an array of values
      3. a known value for the calculation answer that we are finding the uncertainty of.

      """
      return np.average(val_1 * np.sqrt(np.sum(2*(error/value)**2)))

# dot positions
orange_x_pos = np.array(df["position_px_x-darkorange"][3:])
orange_y_pos = np.array(df["position_px_y-darkorange"][3:])

green_x_pos = np.array(df["position_px_x-green"][3:])
green_y_pos = np.array(df["position_px_y-green"][3:])

yellow_x_pos = np.array(df["position_px_x-yellowneon"][3:])
yellow_y_pos = np.array(df["position_px_y-yellowneon"][3:])

# Length = the distance between the green and yellow dot
# Width = the distance between the green and orange dot
rd_length = np.round(np.sqrt((green_x_pos - yellow_x_pos)**2+(green_y_pos - yellow_y_pos)**2))
rd_width = np.round(np.sqrt((green_x_pos - orange_x_pos)**2+(green_y_pos - orange_y_pos)**2))
dist_array = np.array([np.average(rd_length),np.average(rd_width)])

# error in length calc:
# 3 phases:
error_dx = error_add(0.3)
error_dy = error_add(0.3)
error = np.array([error_dx,error_dy])

# error in length
dx_length = np.average(green_x_pos - yellow_x_pos)
dy_length = np.average(green_y_pos - yellow_y_pos)
dlen_array = np.array([np.average(dx_length),np.average(dx_length)])
error_len = error_mult_mod(error,dlen_array,rd_length)

# error in width
dx_width = np.average(green_x_pos - orange_x_pos)
dy_width = np.average(green_y_pos - orange_y_pos)
dwide_array = np.array([np.average(dx_width),np.average(dx_width)])
error_wid = error_mult_mod(error,dwide_array,rd_width)


# find the ave length and width
ave_len = np.average(rd_length)
ave_wid = np.average(rd_width)

# average area
ave_area = ave_len*ave_wid
ave_array = np.array([ave_len,ave_wid])
err_ave_array = np.array([error_len,error_wid])
error_ave_area = error_mult(err_ave_array,ave_array,ave_area)


# plot the hist for length and width
bins = np.arange(158,171)
plt.title("Length and Width")

# plot 1 
plt.subplot(211)
plt.hist(rd_length, bins = bins, edgecolor = "black", color = 'green', label = "Length" )
plt.axvline(ave_len, color = 'red', label = "Ave Length")
plt.legend()

# plot 2
plt.subplot(212)
plt.hist(rd_width, bins = bins, edgecolor = "black", color = 'blue', label = 'Width')
plt.axvline(ave_wid, color = 'red', label = "Ave Width")
plt.legend()
plt.show()

# print the results
print("The average length  is %f \n its uncertainty is %f." %(round(ave_len, 3), round(error_len, 3)))
print("The average width is %f \n its uncertainty is %f." %(round(ave_wid, 3), round(error_wid, 3)))
print()
print("The average area is %f \n its uncertainty is %f." %(round(ave_area, 3), round(error_ave_area, 3)))
