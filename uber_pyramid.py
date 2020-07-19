"""
This problem was asked by Uber.

You have N stones in a row, and would like to create from them a pyramid. 
This pyramid should be constructed such that the height of each stone 
increases by one until reaching the tallest stone, after which the heights decrease by one. 
In addition, the start and end stones of the pyramid should each be one stone high.

You can change the height of any stone by paying a cost of 1 unit to 
lower its height by 1, as many times as necessary. Given this information, 
determine the lowest cost method to produce this pyramid.

For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is to pay 2 to create [0, 1, 2, 3, 2, 1].
"""

import unittest

def find_min_cost_to_make_pyramid(arr):
    N = len(arr)
    summit = [0] * N
    cost = 0

    if N<3: return None

    top_idx = 0
    top_val = 0
    for i in range(N):
        pre_el = 0 if i==0 else arr[i-1]
        next_el = 0 if i==N-1 else arr[i+1]

        summit[i] = min(arr[i], 1 + min(pre_el, next_el))
        
        if summit[i]>top_val:
            top_idx = i
            top_val = summit[i]
    
    for i in range(N):
        summit[i] = max(top_val - abs(top_idx - i), 0)
        cost += arr[i] - summit[i]

    return cost
    

class FindMinCostPyramidTestCase(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual(find_min_cost_to_make_pyramid([1, 1, 3, 3, 2, 1]), 2)

    def test_sample_2(self):
        self.assertEqual(find_min_cost_to_make_pyramid([2, 1, 3, 2, 3, 1, 2]), 10)


if __name__=='__main__':
    unittest.main()


