#-*- coding:utf-8 -*-

# Author:james Zhang
# Datetime:20-2-20 下午6:19
# Project: CS224W


import snap


DATA_PATH = './Wiki-Vote.txt'


if __name__ == '__main__':
    G1 = snap.LoadEdgeList(snap.PNGraph, DATA_PATH, 0, 1)

    # Answer 1:
    print('The number of nodes: {}'.format(len(list(G1.Nodes()))))

    # self_loop_v_cnt = 0
    # direct_edge_cnt = 0
    # for edge in G1.Edges():
    #     src, dst = edge.GetSrcNId(), edge.GetDstNId()
    #     # print(src, dst)
    #     if src == dst:
    #         self_loop_v_cnt += 1
    #     else:
    #         direct_edge_cnt += 1

    # Answer 2:
    print('There are {} self-loop nodes'.format(snap.CntSelfEdges(G1)))

    # Answer 3:
    print('Thre are {} directed edges'.format(snap.CntUniqDirEdges(G1)))

    # Answer 4:
    print('There are {} undirect edges'.format(snap.CntUniqUndirEdges(G1)))

    # Answer 5:
    print('There are {} reciprocated edges'.format(snap.CntUniqBiDirEdges(G1)))

    # Answer 6:
    print('There are {} nodes having 0 out-degree'.format(snap.CntOutDegNodes(G1, 0)))

    # Answer 7:
    print('There are {} nodes having 0 in-degree'.format(snap.CntInDegNodes(G1, 0)))

    # Answer 8:
    DegToCntV = snap.TIntPrV()
    snap.GetOutDegCnt(G1, DegToCntV)
    Out10_cnt = 0
    for item in DegToCntV:
        if item.GetVal1() > 10:
            Out10_cnt += 1
    print('There are {} nodes having >10 out-degree'.format(Out10_cnt))

    # Answer 9:
    DegToCntV = snap.TIntPrV()
    snap.GetInDegCnt(G1, DegToCntV)
    In10_cnt = 0
    for item in DegToCntV:
        if item.GetVal1() < 10:
            In10_cnt += 1
    print('There are {} nodes having <10 in-degree'.format(In10_cnt))
