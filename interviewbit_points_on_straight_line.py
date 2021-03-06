'''
Asked on interviewbit.com

Points on the Straight Line
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Sample Input :

(1, 1)
(2, 2)
Sample Output :

2
You will be given 2 arrays X and Y. Each point is represented by (X[i], Y[i])

'''

import unittest
from collections import defaultdict


def no_of_lines(X, Y):
    N = len(X)
    if N <= 1:
        return N
    elif N == 2:
        return 1

    lines = defaultdict(set)
    for i in range(N):
        for j in range(N):
            if i != j:
                if X[i] == X[j]:
                    lines[X[i]].add(i)
                    lines[X[i]].add(j)
                else:
                    a = float(Y[j]-Y[i]) / (X[j]-X[i])
                    b = Y[j] - a * X[j]
                    lines[(a, b)].add(i)
                    lines[(a, b)].add(j)
    return max(len(lines[k]) for k in lines)


class NoOfLinesTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, no_of_lines((1, 2), (1, 2)))

    def test_2(self):
        self.assertEqual(4, no_of_lines((1, 1, 3, 4, 1, 1),
                                        (2, 3, 3, 4, 5, 7)))


if __name__ == "__main__":
    unittest.main()
