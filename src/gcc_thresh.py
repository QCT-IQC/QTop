#
# QTop
#
# Copyright (c) 2016 Jacob Marks (jacob.marks@yale.edu)
#
# This file is part of QTop.
#
# QTop is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

L = np.array([2,3,5,8,13,25,50,101,7919])
# L = np.array([2,3,5,8,13,50,7919])

sigma = np.ones(9)
# sigma[[-1,-2]] = 0.01
thresh = np.array([.0975,.118,.145,.162,.165,.167,.1698,.170,.177])
# thresh = np.array([.0975,.118,.145,.162,.165,.1698,.177])

plt.plot(L[:-1], thresh[:-1], '.', label="Empirical Data")
# plt.plot(L, thresh)

def func(x, a, b, c):
    return a - float(b)/(c + x)

xs = np.linspace(2,110,1000)
# popt, pcov = curve_fit(func, L, thresh, sigma=sigma)
popt, pcov = curve_fit(func, L, thresh)


plt.plot(xs, func(xs, *popt), label="Fitted Curve")

ys = [popt[0]] * 1000
thr = round(popt[0],3)
plt.plot(xs, ys, 'r--', label="Plateau at " + str(thr))


title = "Threshold vs Qudit dimension"
plt.title(str(title))
plt.xlabel("Qudit dimension d")
plt.ylabel("Threshold")
plt.legend(loc=4)
plt.savefig('../plots/gcc_thresh1.png')
plt.show()
