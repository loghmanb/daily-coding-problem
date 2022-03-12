'''
Hotel Reviews
Asked in: Booking.com

https://www.interviewbit.com/problems/hotel-reviews/

Given a set of reviews provided by the customers for different hotels and a string containing “Good Words”, 
you need to sort the reviews in descending order according to their 
“Goodness Value” (Higher goodness value first). We define the “Goodness Value” of a string 
as the number of “Good Words” in that string.

Note: Sorting should be stable. If review i and review j have the same “Goodness Value” 
then their original order would be preserved.

 You are expected to use Trie in an Interview for such problems 

Constraints:

1.   1 <= No.of reviews <= 200
2.   1 <= No. of words in a review <= 1000
3.   1 <= Length of an individual review <= 10,000
4.   1 <= Number of Good Words <= 10,000
5.   1 <= Length of an individual Good Word <= 4
6.   All the alphabets are lower case (a - z)
Input:

S : A string S containing "Good Words" separated by  "_" character. (See example below)
R : A vector of strings containing Hotel Reviews. Review strings are also separated by "_" character.
Output:

A vector V of integer which contain the original indexes of the reviews in the sorted order of reviews. 

V[i] = k  means the review R[k] comes at i-th position in the sorted order. (See example below)
In simple words, V[i]=Original index of the review which comes at i-th position in the sorted order. 
(Indexing is 0 based)
Example:

Input: 
S = "cool_ice_wifi"
R = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]

Output:
ans = [2, 0, 1]
Here, sorted reviews are ["cool_wifi_speed", "water_is_cool", "cold_ice_drink"]
'''

import unittest


def findHotelOrder2(S, R):
    good_words = set(S.split('_'))
    reviews = R
    rank_idx_list = sorted(
        [(sum(1 for s in review.split('_') if s in good_words), -idx) for idx, review in enumerate(reviews)], 
        reverse=True)
    return [-idx for _,idx in rank_idx_list]


def findHotelOrder(S, R):
    S = set(S.split('_'))
    ans = []
    for i, review in enumerate(R):
        score = 0
        for key in review.split('_'):
            if key in S:
                score += 1
        ans.append([score, i])
    ans.sort(key= lambda x:x[0], reverse=True)
    return list(map(lambda x:x[1], ans))


class FindHotelOrderTest(unittest.TestCase):
    
    def test_findHotelOrder_1(self):
        result = findHotelOrder("cool_ice_wifi", ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"])
        expected = [2, 0, 1]
        self.assertEqual(expected, result)
        
    def test_findHotelOrder2_1(self):
        result = findHotelOrder2("cool_ice_wifi", ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"])
        expected = [2, 0, 1]
        self.assertEqual(expected, result)

if __name__ == "__main__":

    unittest.main()