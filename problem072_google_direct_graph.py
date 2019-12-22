'''
This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A
[(0, 0)]
Should return null, since we have an infinite loop.
'''

def graphMaxValue(labels, edges):
    graph = {}
    dests = set()
    for (src, dest) in edges:
        if src not in graph:
            graph[src] = set([dest])
        else:
            graph[src].add(dest)
        dests.add(dest)
    srcs = set()
    for src in graph.keys():
        if src not in dests:
            srcs.add(src)
    
    maxVal = 0
    edges = [ [{}, src] for src in srcs]
    while edges:
        item = edges.pop()
        if item[1] is None:
            max_label_occ = max(item[0].values())
            if maxVal<max_label_occ:
                maxVal = max_label_occ
        else:
            for node in graph.get(item[1], (None,)):
                label_occ = item[0].copy()
                if labels[item[1]] in label_occ:
                    label_occ[labels[item[1]]] += 1
                else:
                    label_occ[labels[item[1]]] = 1
                edges.append([label_occ, node])
    return maxVal or None


if __name__ == "__main__":
    data = [
             [
               [
                "ABACA",
                [(0, 1),
                 (0, 2),
                 (2, 3),
                 (3, 4)]
               ]
             ] 
    ]
    for d in data:
        print('input', d[0], 'output', graphMaxValue(*d[0]))