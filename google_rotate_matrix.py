'''
Rotate Matrix
Asked in: Google, Facebook, Amazon

https://www.interviewbit.com/problems/rotate-matrix/

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
'''
import unittest

def rotate90(A):
    N = len(A)
    for k in range(N//2):
        i = j = k
        for l in range(k, N-2*k-1):
            tmp1 = A[i][j]
            for _ in range(4):
                new_i = j
                new_j = N-1-i
                tmp2 = A[new_i][new_j]
                A[new_i][new_j] = tmp1
                tmp1 = tmp2
                i = new_i
                j = new_j
            j += 1
    return A


class TestRotate90(unittest.TestCase):

    def test_rotate90_2x2(self):
        result = rotate90([
                            [1, 2],
                            [3, 4]
                          ])
        expected = [
                    [3, 1],
                    [4, 2]
                   ]
        self.assertEqual(expected, result)

    def test_rotate90_3x3(self):
        result = rotate90(
                          [
                            [1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]
                          ])
        expected = [
                    [7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]
                   ]
                   
        self.assertEqual(expected, result)


if __name__ == "__main__":
    
    unittest.main()
