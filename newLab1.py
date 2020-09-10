import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# import the csv into pandas for easy access of information
df = pd.read_csv("example_4.csv")

gx = np.array(df["position_px_x-green"][3:])
gy = np.array(df["position_px_y-green"][3:])
yx = np.array(df["position_px_x-yellowneon"][3:])
yy = np.array(df["position_px_y-yellowneon"][3:])
ox = np.array(df["position_px_x-darkorange"][3:])
oy = np.array(df["position_px_y-darkorange"][3:])

#   Find length = green and yellow, Width = green and orange

# 1. x_diff, y_diff
xdiff_len = (yx - gx)
ydiff_len = (yy - gy)
xdiff_wid = (ox - gx)
ydiff_wid = (oy - gy)
#        ### Error: ###  
err_xdiff_len = np.sqrt(3**2 + 3**2)
err_ydiff_len = np.sqrt(3**2 + 3**2)
err_xdiff_wid = np.sqrt(3**2 + 3**2)
err_ydiff_wid = np.sqrt(3**2 + 3**2)
print(err_xdiff_len)


# 2. x_exp, y_exp
xexp_len = (xdiff_len)**2
yexp_len = (ydiff_len)**2
xexp_wid = (xdiff_wid)**2
yexp_wid = (ydiff_wid)**2
#       ### Error: ###
err_xexp_len = xexp_len*2*(err_xdiff_len/(xdiff_len))
err_yexp_len = yexp_len*2*(err_ydiff_len/(ydiff_len))
err_xexp_wid = xexp_wid*2*(err_xdiff_wid/(xdiff_wid))
err_yexp_wid = yexp_wid*2*(err_xdiff_wid/(ydiff_wid))


# 3. yxsum

yxsum_len = yexp_len + xexp_len
yxsum_wid = yexp_wid + xexp_wid
#       ### Error: ###
err_yxsum_len = np.sqrt((err_yexp_len)**2 + (err_xexp_len)**2)
err_yxsum_wid = np.sqrt((err_yexp_wid)**2 + (err_xexp_wid)**2)


# 4. L = yxsum, W = yxsum

length = np.sqrt(yxsum_len)
width = np.sqrt(yxsum_wid)
ave_len = np.average(length)
ave_wid = np.average(width)
#       ### Error: ###
error_length = np.abs(length)*0.5*(err_yxsum_len/np.abs(yxsum_len))
error_width = np.abs(width) * 0.5 * (err_yxsum_wid /(yxsum_wid))


# histogram of width and length

# plot 1 
plt.subplot(211)
plt.hist(length, edgecolor = "black", color = 'green', label = "Length" )
plt.axvline(ave_len, color = 'red', label = "Ave Length")
plt.legend()

# plot 2
plt.subplot(212)
plt.hist(width, edgecolor = "black", color = 'blue', label = 'Width')
plt.axvline(ave_wid, color = 'red', label = "Ave Width")
plt.legend()
plt.show()