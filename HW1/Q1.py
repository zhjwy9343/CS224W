#-*- coding:utf-8 -*-

# Author:james Zhang
# Datetime:20-3-8 上午10:34
# Project: CS224W


import snap
import numpy as np
import itertools as itt


class ER_graph(object):
    """
    A class of Erdos-Renyi random network.
    """
    def __init__(self, n=2, e=1):
        """
        One method of generating ER network
        :param n: number of nodes to be generated
        :param m: number of edges to be generated
        """
        self.n = n
        self.e = e

        # sanity check
        if (e > (n * n / 2)):
            raise Exception("The given number of edges {} is greater than theorical upper limit".format(e))

        # call method
        self.graph = self._generate_graph()

    def _generate_graph(self):

        print('start...')
        # permunate all edges, size = n(n-1)/2
        node_list = np.arange(self.n)
        edge_list = []

        print('get all edge candidate')
        for edge in itt.combinations(node_list, 2):
            edge_list.append(edge)

        # randomly pick e edges
        print('get all edges, which is the slowest step, as choice fn is too slow')
        e_len = len(edge_list)
        edge_list_idx = np.random.choice(np.arange(e_len), self.e, replace=False)

        # MUST convert to numpy array first, before use index to get the final edges
        edge_list = np.array(edge_list)[edge_list_idx]
        # print(edge_list)

        # create a SNAP graph and set nodes and edges
        print('set a SNAP undirected graph')
        graph = snap.TUNGraph.New()

        for node in node_list.tolist():
            graph.AddNode(node)

        for edge in edge_list.tolist():
            src = edge[0]
            dst = edge[1]
            graph.AddEdge(src, dst)

        # print(len(list(graph.Nodes())))
        return graph


class small_world_graph(object):
    """
    begin with n = 5242 nodes arranged as a ring, i.e., imagine the nodes form a circle and each node is
    connected to its two direct neighbors (e.g., node 399 is connected to nodes 398 and 400),
    giving us 5242 edges. Next, connect each node to the neighbors of its neighbors (e.g., node
    399 is also connected to nodes 397 and 401). This gives us another 5242 edges. Finally,
    randomly select 4000 pairs of nodes not yet connected and add an edge between them. In
    total, this will make m = 5242 · 2 + 4000 = 14484 edges.
    """
    def __init__(self, n=2, e=1):
        self.n = n
        self.e = e

        if (e > (n * n / 2)):
            raise Exception("The given number of edges {} is greater than theorical upper limit".format(e))

        self.graph = self._generate_graph()

    def _generate_graph(self):
        pass


if __name__ == '__main__':
    g = ER_graph(n=5242, e=14484)

    # SNAP implementation of ER graph is much faster than my naive version
    # g1 = snap.GenRndGnm(snap.PUNGraph, 5242, 14484)
    # print(len(list(g1.Nodes())))