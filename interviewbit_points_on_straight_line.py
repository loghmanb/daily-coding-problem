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


def no_of_lines(X, Y):
    pass


class NoOfLinesTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(1, no_of_lines([(1, 1), (2, 2)]))


if __name__ == "__main__":
    unittest.main()
