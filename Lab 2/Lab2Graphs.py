import matplotlib.pyplot as plt
import numpy as np
import math as mt

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
        est_g =   9.8 * mt.sin( 
            3.6 * ( mt.pi / 180 )
        )
        plt.title(self.name)
        plt.hist(self.ay_hist, bins = bins, edgecolor = "darkslategrey", color = "seagreen")
        plt.xticks(ticks)
        plt.axvline(est_g, color = "goldenrod", lw = 3, label = round(est_g, 5))
        plt.legend()
        plt.show()
     
