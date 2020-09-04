import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("example_4.csv")


# Get Data
orange_pos = np.array([df["position_px_x-darkorange"][3:],df["position_px_y-darkorange"][3:]])
green_pos = np.array([df["position_px_x-green"][3:],df["position_px_y-green"][3:]])
yellow_pos = np.array([df["position_px_x-yellowneon"][3:],df["position_px_y-yellowneon"][3:]])      

