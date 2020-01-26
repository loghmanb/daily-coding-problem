'''
Order of People Heights
Asked in: Google

https://www.interviewbit.com/problems/order-of-people-heights/

You are given the following :

A positive number N
Heights : A list of heights of N persons standing in a queue
Infronts : A list of numbers corresponding to each person (P) that gives the number of persons who are taller than P and standing in front of P
You need to return list of actual order of persons’s height

Consider that heights will be unique

Example

Input : 
Heights: 5 3 2 6 1 4
InFronts: 0 1 2 0 3 2
Output : 
actual order is: 5 3 2 1 6 4 
So, you can see that for the person with height 5, there is no one taller than him who is in front of him, and hence Infronts has 0 for him.

For person with height 3, there is 1 person ( Height : 5 ) in front of him who is taller than him.

You can do similar inference for other people in the list.


Hint:

This problem is slightly tricky.

Really inefficient but correct approach :

Try out all possible permutation of the give numbers, and verify if the infronts numbers match for the given sequence.
This is obviously too inefficient. O(N!).
Lets see if we can do something better.

Hint towards something better

What can you say about the position of the shortest person ? If the position of the shortest person is i, how many people would be in front of the shortest person ?

Once you fix the position of the shortest person, what can you say about the position of the second shortest person ?

If we take that approach, do we need to sort the heights first ?

'''

import unittest

# @param Heights : list of integers
# @param InFronts : list of integers
# @return a list of integers
def order_people(Heights, InFronts):
    N = len(Heights)
    result = [0] * N
    open_pos = [i for i in range(N)]
    heights_infrons = sorted([(h, n) for h, n in zip(Heights, InFronts)])
    for h,n in heights_infrons:
        pos = open_pos[n]
        result[pos] = h
        del open_pos[n]
    return result


class OrderPeopleTest(unittest.TestCase):

    def test_order_1(self):
        result = order_people([5, 3, 2, 6, 1, 4], [0, 1, 2, 0, 3, 2])
        expected = [5, 3, 2, 1, 6, 4]
        self.assertEqual(result, expected)


if __name__ == "__main__":

    unittest.main()