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


DATA_PATH = './stackoverflow-Java.txt'


if __name__ == '__main__':

    # Build Java Stackoverflow Graph
    G1 = snap.LoadEdgeList(snap.PNGraph, DATA_PATH, 0, 1)

    # Get the number of Wcc
    Wccs = snap.TCnComV()
    snap.GetWccs(G1, Wccs)

    print("Weakly connected components: {:d}".format(len(list(Wccs))))

    # Get the number of nodes and edges on the largest Wcc
    MxWcc = snap.GetMxWcc(G1)
    num_nodes = len(list(MxWcc.Nodes()))
    num_edges = len(list(MxWcc.Edges()))

    print("The largest WCC has {:d} nodes; {:d} edges".format(num_nodes, num_edges))

    # Get top 3 RageRank IDs
    PRankH = snap.TIntFltH()
    snap.GetPageRank(G1, PRankH)

    top_3 = []

    for item in PRankH:
        top_3.append((PRankH[item], item))
        if len(top_3) > 3:
            top_3 = sorted(top_3, key=lambda x:x[0], reverse=True)[:3]

    print("Top 3 PageRank IDs: {}, {}, {}".format(top_3[0][1], top_3[1][1], top_3[2][1]))

    # Get top 3 Hubs and Authorities IDs
    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(G1, NIdHubH, NIdAuthH)

    top_3_hub = []
    for item in NIdHubH:
        top_3_hub.append((NIdHubH[item], item))

        if len(top_3_hub) > 3:
            top_3_hub = sorted(top_3_hub, key=lambda x:x[0], reverse=True)[:3]

    print("Top 3 Hubs IDs: {}, {}, {}".format(top_3_hub[0][1], top_3_hub[1][1], top_3_hub[2][1]))

    top_3_auth = []
    for item in NIdAuthH:
        top_3_auth.append((NIdAuthH[item], item))

        if len(top_3_auth) > 3:
            top_3_auth = sorted(top_3_auth, key=lambda x:x[0], reverse=True)[:3]

    print("Top 3 Authorities IDs: {}, {}, {}".format(top_3_auth[0][1], top_3_auth[1][1], top_3_auth[2][1]))