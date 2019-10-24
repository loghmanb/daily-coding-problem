'''

Given arrays for N (>=2) users, each representing the IDs of hotels visited, 
find the common IDs of the hotels visited amongst the users.

Input:
userA = { 2, 3, 1 }
userB = { 2, 5, 3 }
userC = { 7, 3, 1 }

Output:
{3}

Assumptions:
Arrays are unsorted.

Cases:
1) Each array consists of distinct hotel IDs
2) Each array may contain duplicate hotel IDs
'''

from collections import defaultdict

def find_common_hotels(users):
    no = len(users.keys())
    d = defaultdict(set)
    for user in users:
        for hotel_id in users[user]:
            d[hotel_id].add(user)
    ans = list(filter(lambda hid:len(d[hid])==no, d.keys()))
    return ans

if __name__ == "__main__":
    data = [
            [
                {'userA': [2, 3, 1], 'userB': [2, 5, 3], 'userC': [7, 3, 1]},
                [3]
            ]
        ]

    print('find common hotel ids:')
    for d in data:
        print('users log', d[0], 'result', find_common_hotels(d[0]), 'expected', d[1])
