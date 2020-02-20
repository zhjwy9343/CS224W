#-*- coding:utf-8 -*-

# Author:james Zhang
# Datetime:20-2-20 下午4:55
# Project: CS224W

import snap

G1 = snap.TNGraph.New()
G1.AddNode(1)
G1.AddNode(5)
G1.AddNode(32)
G1.AddEdge(1,5)
G1.AddEdge(5,1)
G1.AddEdge(5,32)

for node in G1.Nodes():
    print(node.GetId())

for edge in G1.Edges():
    print(edge.GetId())

if __name__ == '__main__':
    pass