# ====================== #
# Acceleration Analysis with the removal of bounces
# ====================== #

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as mt

# pull Data from file
meter_df = pd.read_csv("meter_stick.csv")
puck1_df = pd.read_csv("puck_drop.csv")
puck2_df = pd.read_csv("puck_drop_2.csv")
puck3_df = pd.read_csv("puck_drop_3.csv")

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

class object_puck_acc:
    def __init__(self, dataframe, start = 1, cut = 0.86):

        self.gx = np.array([dataframe["gx"][start:]])
        self.gx = convert(self.gx)

        self.gy = np.array([dataframe["gy"][start:]])
        self.gy = convert(self.gy)
        
        self.time_ms = np.array([dataframe["time"][start:]])
        self.time = self.time_ms / 1000

        array_cut = np.where(self.gy >= cut )
        self.gx =  np.delete(self.gx, array_cut)
        self.gy =  np.delete(self.gy, array_cut)
        self.time =  np.delete(self.time, array_cut)
        
        
        
    def dataframe(self):
        self.velx = np.gradient(self.gx.flatten(),self.time.flatten())
        self.vely = np.gradient(self.gy.flatten(),self.time.flatten())
        self.xacc = np.gradient(self.velx.flatten(),self.time.flatten())
        self.yacc = np.gradient(self.vely.flatten(),self.time.flatten())
        self.data_df = pd.DataFrame({
        "xpos": self.gx.flatten(),
        "ypos": self.gy.flatten(),
        "xvel": self.velx.flatten(),
        "yvel": self.vely.flatten(),
        "xacc": self.xacc.flatten(),
        "yacc": self.yacc.flatten(),
        "time": self.time.flatten()
        })
    def remove_bounce(self):
        pass

class graph:
    def __init__(self, name, title):
        self.name = str(title)
        self.gx = np.negative(name.data_df["xpos"])
        self.gy = np.negative(name.data_df["ypos"])
        self.vx = np.negative(name.data_df["xvel"])
        self.vy = np.negative(name.data_df["yvel"])
        self.ax = np.negative(name.data_df["xacc"])
        self.ay = np.negative(name.data_df["yacc"])
        self.time = name.data_df["time"]
        
    def motiongraphs(self):  
        # y pos
        plt.subplot(311)
        plt.plot(self.time,self.gy, color = "darkorchid", label = "Position")
        plt.xlabel("time")
        plt.ylabel("$m$")


        # y vel
        plt.subplot(312)
        plt.plot(self.time,self.vy, color = "crimson", label = "Velocity")
        plt.xlabel("time")
        plt.ylabel("$m/s$")


        # y acc
        plt.subplot(313)
        plt.plot(self.time,self.ay, color = "midnightblue", label = "Acceleration")
        plt.xlabel("time")
        plt.ylabel("$m/s^2$")

        plt.show()

    def hist(self):
        self.ay_hist = np.negative(self.ay)
        bins = np.linspace(-2,2,20)
        ticks = np.linspace(-2,2,8)
        plt.title(self.name)
        plt.hist(self.ay_hist, bins = bins, edgecolor = "darkslategrey", color = "seagreen")
        plt.xticks(ticks)
        plt.legend()
        plt.show()
     
trial1 = object_puck_acc(puck1_df, 85)
trial2 = object_puck_acc(puck2_df, 10)
trial3 = object_puck_acc(puck3_df, 10)
trial1.dataframe()
trial2.dataframe()
trial3.dataframe()

# Creates an Excel File with the data
def createExcel():
    with pd.ExcelWriter("Lab2Acc.xlsx") as writer:
        trial1.data_df.to_excel(writer,sheet_name = "Trial 1")
        trial2.data_df.to_excel(writer,sheet_name = "Trial 2")
        trial3.data_df.to_excel(writer,sheet_name = "Trial 3")

t1 = graph(trial1, "Puck #1")
t2 = graph(trial2, "Puck #2")
t3 = graph(trial3, "Puck #3")

# t1.motiongraphs()
# t2.motiongraphs()
# t3.motiongraphs()

createExcel()