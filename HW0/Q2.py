#-*- coding:utf-8 -*-

# Author:james Zhang
# Datetime:20-2-26 上午10:12
# Project: CS224W
"""

This part asks for two tasks:
1. Plot out degree distribution, and,
2. Compute linear coefficient and plot the linear line

"""


import snap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


DATA_PATH = './Wiki-Vote.txt'


if __name__ == '__main__':

    # Build Wiki Graph
    G1 = snap.LoadEdgeList(snap.PNGraph, DATA_PATH, 0, 1)

    DegToCntV = snap.TIntPrV()

    snap.GetOutDegCnt(G1, DegToCntV)

    out_deg = []
    deg_cnt = []

    for item in DegToCntV:
        deg_cnt.append(item.GetVal2())
        out_deg.append(item.GetVal1())

    out_deg_dis = pd.DataFrame({'Out_Degree_Value': out_deg, "Out_Degree_Cnt": deg_cnt})
    out_deg_dis.drop(index=0, inplace=True)

    # print(out_deg_dis.head(10))
    # print(out_deg_dis.shape)

    # As polyfit and poly1d does not work, I try to use liear reression to get the coefficient and intercept
    log_ODV = np.log10(out_deg_dis.Out_Degree_Value).values
    log_ODV = log_ODV[:, np.newaxis]
    log_ODC = np.log10(out_deg_dis.Out_Degree_Cnt).values

    l_r = LinearRegression()
    l_r.fit(log_ODV, log_ODC)
    print(l_r.coef_, l_r.intercept_)

    baseline = l_r.predict(log_ODV)

    preds = np.power(baseline, 10)
    preds[preds<1] = 1

    out_deg_dis['Out_Deg_Fit'] = pd.Series(preds)

    print(out_deg_dis.head(-10))
    print(out_deg_dis.shape)

    # plot_log_log(out_deg_dis, 'Out_Degree_Value', "Out_Deg_Fit"))
    ax = out_deg_dis.plot('Out_Degree_Value', 'Out_Deg_Fit', lw=2, color='red',logy=True, logx=True, figsize=(10,10),
                          label="Y = {:.2f}x + {:.2f}".format(l_r.coef_[0], l_r.intercept_))
    out_deg_dis.plot('Out_Degree_Value', 'Out_Degree_Cnt', lw=2, color='blue',logy=True, logx=True, ax=ax,
                     label="Log-Log Degree cnt vs Degree Freq".format(l_r.coef_, l_r.intercept_))
    plt.show()
