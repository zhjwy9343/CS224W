#-*- coding:utf-8 -*-

# Author:james Zhang
# Datetime:20-3-8 上午10:34
# Project: CS224W
"""
    This version is purely based on python library without use SNAP

    SNAP vesion cuold be found in the hw1-q1-starter.py file
"""


import snap
import numpy as np
import itertools as itt


def create_snap_graph(node_list, edge_list):
    graph = snap.PUNGraph.New()

    for node in node_list:
        graph.AddNode(node)

    # Have to complain that SNAP is sooooooo wierd in its data type! has to use int() to convert a variable so that
    # the AddEdge fn can work. Tooooo noisy!
    for edge in edge_list:
        src = int(edge[0])
        dst = int(edge[1])
        graph.AddEdge(src, dst)

    print("Create a graph with nodes: {}".format(len(list(graph.Nodes()))))
    print("Create a graph with nodes: {}".format(len(list(graph.Edges()))))
    return graph


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
        if (n < 0) or (e < 0) or (e > (n * n / 2)):
            raise Exception("The given number of edges {} is greater than theorical upper limit".format(e))

        # call method
        self.graph = self._generate_graph()

    def _generate_graph(self):
        """
        This version use random pick instead of full combination.
        :return:
        """
        # create nodes
        node_list = np.arange(self.n)

        # create edges randomly
        count = 0
        edge_set = set()

        while count < self.e:
            # randint is half open, but random_integers is full closure
            rand_pair = np.random.randint(low=0, high=self.n, size=2)
            if (rand_pair[0] != rand_pair[1]) and (not ((rand_pair[0], rand_pair[1]) in edge_set)):
                edge_set.add((rand_pair[0], rand_pair[1]))
                count += 1

        # set an SNAP graph
        return create_snap_graph(node_list.tolist(), list(edge_set))


    def _generate_graph_v1(self):
        """
        This version is too slow, becuase it create the full combination of nodes, which is n^2.
        :return:
        """
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
        return create_snap_graph(node_list.tolist(), edge_list.tolist())


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

        # sanity check
        if (n < 0) or (e < 0) or (e > (n * n / 2)):
            raise Exception("The given number of edges {} is greater than theorical upper limit".format(e))

        if (e < 2 * n):
            raise Exception('The number of edges is not big enough for this method')

        self.graph = self._generate_graph()

    def _generate_graph(self):

        # get node list with given size
        node_list = np.arange(self.n)

        # edge with neighbors, use (i + n +-1) % n to get neighbors
        # SNAP undirected graph can detect duplicate edges, but here I will use
        edge_set = set()
        for node in node_list:
            dst_p1 = (node + self.n + 1) % self.n
            dst_n1 = (node + self.n - 1) % self.n

            dst_p2 = (node + self.n + 2) % self.n
            dst_n2 = (node + self.n - 2) % self.n

            if not (dst_p1, node) in edge_set:
                edge_set.add((node, dst_p1))
            if not (dst_n1, node) in edge_set:
                edge_set.add((node, dst_n1))
            if not (dst_p2, node) in edge_set:
                edge_set.add((node, dst_p2))
            if not (dst_n2, node) in edge_set:
                edge_set.add((node, dst_n2))

        rest_edges = self.e - len(edge_set)

        count = 0
        while count < rest_edges:
            rand_pair = np.random.randint(low=0, high=self.n, size=2)
            if (rand_pair[0] != rand_pair[1]) and (not ((rand_pair[0], rand_pair[1]) in edge_set)):
                edge_set.add((rand_pair[0], rand_pair[1]))
                count += 1

        # create SNAP graph
        return create_snap_graph(node_list.tolist(), list(edge_set))


if __name__ == '__main__':
    g_ER = ER_graph(n=5242, e=14484)

    # SNAP implementation of ER graph is much faster than my naive version
    # g1 = snap.GenRndGnm(snap.PUNGraph, 5242, 14484)
    # print(len(list(g1.Nodes())))

    g_SW = small_world_graph(n=5242, e=14484)