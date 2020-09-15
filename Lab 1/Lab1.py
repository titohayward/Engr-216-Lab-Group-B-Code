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

l_bins = np.arange(160,171)
w_bins = np.arange(158,169)

# plot 1 
plt.subplot(211)
plt.title("Length and Width")
plt.hist(length, bins = l_bins, edgecolor = "black", color = 'green', label = "Length" )
plt.axvline(ave_len, color = 'red', label = round(ave_len,2))
plt.legend()

# plot 2
plt.subplot(212)
plt.hist(width, bins = w_bins, edgecolor = "black", color = 'blue', label = 'Width')
plt.axvline(ave_wid, color = 'red', label = round(ave_wid,2))
plt.legend()
plt.show()

# Calculate area using 2 methods:
# 1. Find area from ave length and ave widths
# 2. Find area from individual lengths and widths

# Method 1

#1. lsum and wsum
lsum = np.sum(length)
wsum = np.sum(width)
#       ### Error: ###
err_lsum = np.sqrt(np.sum(error_length)**2)
err_wsum = np.sqrt(np.sum(error_width)**2)

#2. l_ave and w_ave
l_ave = np.average(lsum)
w_ave = np.average(wsum)
#       ### Error: ###
err_l_ave = np.sqrt((err_lsum/lsum)**2)
err_w_ave = np.sqrt((err_wsum/wsum)**2)

#3. Area_ave
area_meth1 = l_ave * w_ave
#       ### Error: ###
err_area_meth1 = np.sqrt((err_l_ave/l_ave)**2 + (err_w_ave/w_ave)**2)

# Method 2:

# 1.  A_ind
a_ind = length * width 
#       ### Error: ###
err_a_ind = np.sqrt((error_length)**2 + (error_width)**2)

#2. Asum_ind 
asum_ind = np.sum(a_ind)
#       ### Error: ###
err_asum_ind = np.sqrt(np.sum(err_a_ind)**2)

#3. area_meth2
area_meth2 = np.average(asum_ind)
err_area_meth2 = np.sqrt((err_asum_ind/asum_ind)**2)
# result
print(ave_len, np.average(error_length))
print(ave_wid,np.average(error_width))
print("Method 1: Area ", round(area_meth1, 2),"its uncertainty", round(err_area_meth1,3))
print("Method 2: Area ", round(area_meth2, 2),"its uncertainty", np.std(a_ind))




