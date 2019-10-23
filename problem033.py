'''
This problem was asked by Microsoft.
Compute the running median of a sequence of numbers. That is, given a stream of
numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle
numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
print out:
2
1.5
2
3.5
2
2
2
'''

from collections import defaultdict

def find_median_in_window(arr):
    def find_median(d, n):
        middle = n // 2 + n % 2
        cnt = 0
        v1, v2 = None, None
        for val in sorted(d.keys()):
            cnt += d[val]
            if cnt>=middle:
                if n%2==1:
                    return val
                elif cnt>middle:
                    if v1 is None:
                        return val
                    else:
                        v2 = val
                        break
                else:
                    v1 = val
        return (v1+v2)/2


    ans = []
    d = defaultdict(int)
    for i,x in enumerate(arr):
        d[x] += 1
        ans.append(find_median(d, i+1))
    return ans

if __name__ == '__main__':
    print('Median in list problem')

    data = [[2, 1, 5, 7, 2, 0, 5]]
    for l in data:
        print('input: ', l, ' output: ', find_median_in_window(l))