from os import replace
import numpy as np
from numpy.core.fromnumeric import mean
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import math as mt

# pull Data from file
meter_df = pd.read_csv("Data Files/meter_stick.csv")
puck1_df = pd.read_csv("Data Files/puck_drop.csv")
puck2_df = pd.read_csv("Data Files/puck_drop_2.csv")
puck3_df = pd.read_csv("Data Files/puck_drop_3.csv")

# input in px * (300 mm/ length) * ( 1m / 1000mm ) = output in meters 
px = np.array([meter_df["px"]]) 
py = np.array([meter_df["py"]]) 
yx = np.array([meter_df["yx"]]) 
yy = np.array([meter_df["yy"]]) 
length = np.sqrt( (px-yx)**2  + (py - yy)**2  )
length_ave = np.nanmean(length)

def convert(pixels):
    meters = (1/1000)*(300/length_ave)*pixels 
    return meters

def motion_plot(df1, start = 1, end = 1):
    # Data
    gx = np.array([df1["gx"][start:end]])
    gx= convert(gx)
    gx = gx.flatten()
    gy = np.array([df1["gy"][start:end]])
    gy = convert(gy)
    gy = gy.flatten()
    time_ms = np.array([df1["time"][start:end]])
    time = time_ms / 1000
    time = time.flatten()
    vx = np.gradient(gx.flatten(),time.flatten())
    vy = np.gradient(gy.flatten(),time.flatten())
    ax = np.gradient(vx.flatten(),time.flatten())
    ay = np.gradient(vy.flatten(),time.flatten())

    # PLot Data

    # x - pos
    plt.subplot(321)
    plt.plot(time, gx)
    plt.xlabel("Time")
    plt.ylabel("X Pos")
    plt.title("X Position vs. Time")
    
    # x - vel
    plt.subplot(323)
    plt.plot(time,vx, color = "green")
    plt.xlabel("Time")
    plt.ylabel("X Vel")
    plt.title("X Velocity vs. Time")
    
    # x - acc
    plt.subplot(325)
    plt.plot(time,ax, color = "red")
    plt.xlabel("Time")
    plt.ylabel("X Acc")
    plt.title("X Acceleration vs. Time")
    

    # y - pos
    plt.subplot(322)
    plt.plot(time,gy)
    plt.xlabel("Time")
    plt.ylabel("Y Pos")
    plt.title("Y Position vs. Time")
    

    # y - vel
    plt.subplot(324)
    plt.plot(time, vy, color = "green")
    plt.xlabel("Time")
    plt.ylabel("Y Vel")
    plt.title("Y Velocity vs. Time")
    
    # y - acc
    plt.subplot(326)
    plt.plot(time, ay, color = "red")
    plt.xlabel("Time")
    plt.ylabel("Y Acc")
    plt.title("Y Acceleration vs. Time")
    plt.legend()

    plt.show()

    return 

def data_frame(df1, start =1, end = 1):
    # Data
    gx = np.array([df1["gx"][start:end]])
    gx= convert(gx)
    gx = gx.flatten()
    gy = np.array([df1["gy"][start:end]])
    gy = convert(gy)
    gy = gy.flatten()
    time_ms = np.array([df1["time"][start:end]])
    time = time_ms / 1000
    time = time.flatten()
    vx = np.gradient(gx.flatten(),time.flatten())
    vy = np.gradient(gy.flatten(),time.flatten())
    ax = np.gradient(vx.flatten(),time.flatten())
    ay = np.gradient(vy.flatten(),time.flatten())

    dataFrame = pd.DataFrame({
        "xpos": gx.flatten(),
        "ypos": gy.flatten(),
        "xvel": vx.flatten(),
        "yvel": vy.flatten(),
        "xacc": ax.flatten(),
        "yacc": ay.flatten(),
        "time": time.flatten()
        })

    return dataFrame


def acc_aquire(df1, start = 1):
    # Data
    gx = np.array([df1["gx"][start:]])
    gx= convert(gx)
    gx = gx.flatten()
    gy = np.array([df1["gy"][start:]])
    gy = convert(gy)
    gy = gy.flatten()
    time_ms = np.array([df1["time"][start:]])
    time = time_ms / 1000
    time = time.flatten()

    # cut function: 
    array_cut = np.where(gy <= -0.85 )
    gx =  np.delete(gx, array_cut)
    gy =  np.delete(gy, array_cut)
    time =  np.delete(time, array_cut)

    vx = np.gradient(gx.flatten(),time.flatten())
    vy = np.gradient(gy.flatten(),time.flatten())
    ax = np.gradient(vx.flatten(),time.flatten())
    ay = np.gradient(vy.flatten(),time.flatten())


    return ax, ay

def acc_analysis(title, a1, a2, a3, iter,sample_no, exp_value):
    sample = np.hstack(( a1, a2, a3 )).ravel()

    # Take samples, default = 200
    sample_arr = np.array([])
    for i in range(iter):
        sample_choice = np.random.choice(sample,sample_no, replace = True)
        mean_sample = np.nanmean(sample_choice)
        sample_arr = np.append(sample_arr,mean_sample)

    bin = np.linspace(np.min(sample_arr),np.max(sample_arr),50)
    plt.figure()
    plt.hist(sample_arr, bins = bin, color = "seagreen")
    plt.xlabel("Samples of Acceleration")
    plt.ylabel("Frequency")
    mean = np.nanmean(sample_arr)
    std = np.std(sample_arr)
    stddev = np.array([mean - 3*std, mean - 2*std, mean - std, mean, mean + std, mean + 2*std,mean + 3*std ])
    plt.axvline(mean, label = "Mean value", linewidth = 2, color = "red")
    plt.axvline(exp_value, label = "Expected Value", linewidth = 2, color = "blue")
    plt.xticks(stddev)
    plt.title(title)
    plt.legend()
    plt.show()

p1ax , p1ay = acc_aquire(puck1_df, 110)
p2ax , p2ay = acc_aquire(puck2_df, 81)
p3ax , p3ay = acc_aquire(puck3_df, 88)

g = - 9.8 * mt.sin(
    3.6 * (mt.pi / 180)
)

# start values for trials
# 1. 85
# 2. 10
# 3. 10

motion_plot(puck1_df,110,184)

trial1 = data_frame(puck1_df,110,184)
trial1.to_excel("AccMethod.xlsx" )


