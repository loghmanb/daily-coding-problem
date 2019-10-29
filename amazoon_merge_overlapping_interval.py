'''
Merge Overlapping Intervals
Asked in: Google, Amazon

https://www.interviewbit.com/problems/merge-overlapping-intervals/

Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[12,18].

Make sure the returned intervals are sorted.
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '(%s, %s)' % (self.start, self.end)


# @param intervals, a list of Intervals
# @return a list of Interval
def merge(intervals):
    if not intervals: return []
    ans = []
    arr = []
    for interval in intervals:
        arr.append([interval.start, -1])
        arr.append([interval.end, 1])
    arr = sorted(arr)
    no = 0
    start = None
    for i,x in enumerate(arr):
        no += x[1]
        if start and no==0:
            ans.append(Interval(start, x[0]))
            start = None
        elif no==-1 and start is None:
            start = x[0]
    return ans


if __name__ == "__main__":
    data = [
            [
                [[1,3], [2,6], [8,10], [15,18]], 
                [1,6], [8,10], [15,18]
            ]
        ]

    for d in data:
        intervals = [Interval(*x) for x in d[0]]
        print('input', intervals, 'output', merge(intervals))