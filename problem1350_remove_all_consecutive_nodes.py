"""
This problem was asked by Amazon.

Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, 
you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
"""
import unittest

def remove_all_consecutive_nodes(nodes):
    p = 0
    visited = {}
    s = 0
    for p, node in enumerate(nodes):
        s += node
        if s in visited or s==0:
            s1 = s
            nodes[p] = 0
            start = 0 if s == 0 else visited[s]+1
            for i in range(start, p):
                s1 += nodes[i]
                nodes[i] = 0
                if s1 in visited:
                    del visited[s1]
        else: 
            visited[s] = p

    return list(filter(lambda x:x!=0, nodes))


class TestRemoveConsecutive(unittest.TestCase):
    def test_1(self):
        result = remove_all_consecutive_nodes([5, 3, 2, -2, -1, -2])
        self.assertEqual(result, [5])

    def test_2(self):
        result = remove_all_consecutive_nodes([3, 4, -7, 5, -6, 6])
        self.assertEqual(result, [5])

if __name__=='__main__':
    unittest.main()
