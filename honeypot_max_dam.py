'''
This question asked by honeypot.io

We want to craete a dam to build up a lake

between each concrete wall we can use mud. each mud can maximum 1 unit higher than each sides

we have to array: first for wall position and second for wall height

find max height of mud

Sample1
" used for concreete wall and ' for mud

Input: 

wallPositions = [1, 5, 7]
wallHeights = [2, 3, 2]

Output: 4


    ' '
  ' ' ' " '
" ' ' ' " ' "
" ' ' ' " ' " 
2 3 4 4 3 3 2 : Height 
1 2 3 4 5 6 7 : Position
    ^ ^
    | |
    These are highest mud wall

'''

import unittest

class HoneypotDam:

    def find_max_mud(self, w1, w2, pos1, pos2):
        if w1>w2:
            w1, w2 = w2, w1
        distance = pos2-pos1
        if distance<=1:
            return 0
        elif w2-w1>=distance-1:
            return w1+pos2-pos1-1
        elif w2==w1:
            return w1 + distance//2
        else:
            start, end = 0, distance
            while start<end:
                pos = (end+start)//2
                if pos==start: break
                byw1 = w1 + pos
                byw2 = w2 + distance - pos
                if byw2==byw1 or byw2==byw1+1:
                    return byw1
                elif byw1<byw2:
                    start = pos
                else:
                    end = pos
            return w1+start


    def maxHeight(self, wallPositions, wallHeights):
        N = len(wallPositions) 
        if N<2:
            return 0

        max_height = 0
        for i in range(1, N):
            mud_height = self.find_max_mud(wallHeights[i-1], wallHeights[i], wallPositions[i-1], wallPositions[i])
            if max_height<mud_height:
                max_height = mud_height

        return max_height


class HoneypotDamTest(unittest.TestCase):

    def setUp(self):
        self.honeypotDam = HoneypotDam()

    def test_maxHeight_1(self):
        wallPositions = [1, 5, 7]
        wallHeights = [2, 3, 2]
        expected = 4
        result = self.honeypotDam.maxHeight(wallPositions, wallHeights)
        self.assertEqual(expected, result)

    def test_maxHeight_2(self):
        wallPositions = [1, 3, 7]
        wallHeights = [4, 3, 3]
        expected = 5
        result = self.honeypotDam.maxHeight(wallPositions, wallHeights)
        self.assertEqual(expected, result)

    def test_maxHeight_3(self):
        wallPositions = [1, 10]
        wallHeights = [1, 5]
        expected = 7
        result = self.honeypotDam.maxHeight(wallPositions, wallHeights)
        self.assertEqual(expected, result)


if __name__ == "__main__":

    unittest.main()