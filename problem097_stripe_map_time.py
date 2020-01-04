'''
This problem was asked by Stripe.

Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

set(key, value, time): sets key to value for t = time.
get(key, time): gets the key at t = time.
The map should work like this. If we set a key at a particular time, 
it will maintain that value forever or until it gets set at a later time. 
In other words, when we get a key at a time, it should return the value 
that was set for that key set at the most recent time.

Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2
d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, -1) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
'''

import bisect

class MapTimeNode:
    def __init__(self):
        self._data = {}
        self._times = []

    def set(self, time, value):
        if time not in self._times:
            bisect.insort(self._times, time)
        self._data[time] = value

    def get(self, time):
        idx = bisect.bisect_left(self._times, time)
        if idx==0 and len(self._times) and self._times[0]>time:
            return
        if idx>=len(self._times):
            idx = -1
        elif self._times[idx]>time:
            idx -= 1
        return self._data[self._times[idx]]

class MapTime:
    def __init__(self):
        self._data = {}

    def set(self, key, value, time):
        if key not in self._data:
            self._data[key] = MapTimeNode()
        self._data[key].set(time, value)

    def get(self, key, time):
        if key in self._data:
            return self._data[key].get(time)


if __name__ == "__main__":
    data = [
            [
             [
              ['s', 1, 1, 0],
              ['s', 1, 2, 2],
              ['g', 1, 1],
              ['g', 1, 3],
              ['s', 1, 1, 5],
              ['g', 1, -1],
              ['g', 1, 10],
              ['s', 1, 1, 0],
              ['s', 1, 2, 0],
              ['g', 1, 0]
             ]
            ]
        ]
    for d in data:
        mt = MapTime()
        for cmd in d[0]:
            if cmd[0]=='s':
                print('set for ', cmd[1:])
                mt.set(*cmd[1:])
            else:
                print('get for ', cmd[1:], 'is',  mt.get(*cmd[1:]))
