"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""
import unittest

def number_of_queens(N):
    if N<=1: 
        return N
    queens = [{'row':1, 'col':1}]
    invalid_cols = {1}
    for i in range(2, N+1):
        queen_found = False
        for j in range(2, N+1):
            invalid = False
            if j not in invalid_cols:
                for q in queens:
                    if i-q['row']==j-q['col'] or i-q['row']==q['col']-j:
                        invalid = True
                        break         
            if not invalid:
                queen_found = True
                break
        if queen_found:
            queens.append({'row':i, 'col': j})
    return len(queens)


class TestNoOfQueens(unittest.TestCase):
    def test_3(self):
        self.assertEqual(number_of_queens(3), 2)

if __name__=='__main__':
    unittest.main()
 