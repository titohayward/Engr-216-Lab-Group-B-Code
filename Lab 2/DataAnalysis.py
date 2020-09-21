

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    meters = (1/1000)*(300/length_ave)*pixels # flip the data here due to an offset origin.
    error = np.nanstd(length)
    return meters, error


# Create class that will:
#   import data to arrays and calculate values.
#   convert from milliseconds to seconds.
#   use np.gradient to find the vel and acceleration

class object_puck:
    def __init__(self, dataframe, start = 1):
        gx = np.array([dataframe["gx"][start:]])
        self.gx, self.errorX = convert(gx)
        gy = np.array([dataframe["gy"][start:]])
        self.gy, self.errorY = convert(gy)
        time_ms = np.array([dataframe["time"][start:]])
        self.time = time_ms / 1000
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
    
trial1 = object_puck(puck1_df, 85)
trial2 = object_puck(puck2_df, 10)
trial3 = object_puck(puck3_df, 10)
trial1.dataframe()
trial2.dataframe()
trial3.dataframe()

# Creates an Excel File with the data
def createExcel():
    with pd.ExcelWriter("Lab2Data.xlsx") as writer:
        trial1.data_df.to_excel(writer,sheet_name = "Trial 1")
        trial2.data_df.to_excel(writer,sheet_name = "Trial 2")
        trial3.data_df.to_excel(writer,sheet_name = "Trial 3")

