'''
This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL',
you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', 
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
'''

def get_path(path, start):
    if not path: 
        return [start]
    elif start not in path: 
        return None

    next_path = sorted(list(path[start]))
    for p in next_path:
        if len(path[start])==1:
            del path[start]
        else:
            path[start].remove(p)
        ans = get_path(path, p)
        if p not in path:
            path[p] = set([p])
        else:
            path[p].add(p)
        if ans: return [start]+ans
    return None


def possible_path(path_arr, start):
    path = {}
    for p in path_arr:
        if p[0] not in path:
            path[p[0]]= set()
        path[p[0]].add(p[1])
    
    return get_path(path, start)


if __name__ == "__main__":
    data = [
            [
             [[('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'],
             ['A', 'B', 'C', 'A', 'C']
            ],
            [
             [[('SFO', 'COM'), ('COM', 'YYZ')], 'COM'],
             None
            ],
            [
             [[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'], 
             ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
            ],

    ]
    for d in data:
        print('input', d[0], 'output', possible_path(*d[0]))