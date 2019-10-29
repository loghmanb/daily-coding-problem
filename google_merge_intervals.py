'''
Merge Intervals
Asked in: Google

https://www.interviewbit.com/problems/merge-intervals/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
'''

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '(%s, %s)' % (self.start, self.end)


def insert(intervals, newInterval):
    if newInterval.start>newInterval.end:
        newInterval.start, newInterval.end = newInterval.end, newInterval.start
    ans = []
    find_start = True
    for i in range(len(intervals)):
        if find_start==True:
            if intervals[i].start>newInterval.end:
                ans.append(newInterval)
                ans += intervals[i:]
                break
            elif intervals[i].end>=newInterval.start:
                if newInterval.end>=intervals[i].start:
                    find_start = False
                    ans.append(Interval(
                                        min(newInterval.start, intervals[i].start), 
                                        max(newInterval.end, intervals[i].end)
                                ))
                    find_start = False
                else:
                    ans.append(newInterval)
                    ans += intervals[i:]
                    break
            else:
                ans.append(intervals[i])
        elif intervals[i].start<=newInterval.end:
            ans[-1].end = max(newInterval.end, intervals[i].end)
        else:
            ans += intervals[i:]
            break
    if not ans or newInterval.start>ans[-1].end:
        ans.append(newInterval)
    return ans


if __name__ == "__main__":
    data = [
            [[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9], [1,2],[3,10],[12,16]]
    ]

    for d in data:
        intervals = [Interval(*x) for x in d[0]]
        newInterval = Interval(*d[1])
        print('input', intervals, newInterval, 'output', insert(intervals, newInterval))