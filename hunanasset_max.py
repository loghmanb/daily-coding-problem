'''
Maximum Consecutive Gap
Asked in: Hunan Asset

https://www.interviewbit.com/problems/maximum-consecutive-gap/

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Example :

Input : [1, 10, 5]
Output : 5 
Return 0 if the array contains less than 2 elements.

You may assume that all the elements in the array are non-negative integers and 
fit in the 32-bit signed integer range.

You may also assume that the difference will not overflow.

----------------
Solution by: https://www.interviewbit.com/problems/maximum-consecutive-gap/

Any form of sorting is going to be at least O(n * log n), so we need to think outside of sorting.

Also, you can use extra O(n) space.

Try to think starting from maximum and minimum of array.

How can you use the gap between them to separate elements into different blocks/buckets 
in such a way that you dont have to evaluate the answer for elements within buckets.

Now, first try to think if you were already given the minimum value MIN and 
maximum value MAX in the array of size N, under what circumstances would 
the max gap be minimum and maximum ?

Obviously, maximum gap will be maximum when all elements are either MIN or MAX 
making maxgap = MAX - MIN.

Maximum gap will be minimum when all the elements are equally spaced apart 
between MIN and MAX. Lets say the spacing between them is gap.

So, they are arranged as

MIN, MIN + gap, MIN + 2*gap, MIN + 3*gap, ... MIN + (N-1)*gap 
where

MIN + (N-1)*gap = MAX 
=> gap = (MAX - MIN) / (N - 1). 
So, we know now that our answer will lie in the range [gap, MAX - MIN].
Now, if we know the answer is more than gap, what we do is create buckets of size gap for ranges

  [MIN, MIN + gap), [Min + gap, `MIN` + 2* gap) ... and so on
There will only be (N-1) such buckets. We place the numbers in these buckets based on their value.

If you pick any 2 numbers from a single bucket, their difference will be less than gap, 
and hence they would never contribute to maxgap ( Remember maxgap >= gap ). 
We only need to store the largest number and the smallest number in each bucket, 
and we only look at the numbers across bucket.

Now, we just need to go through the bucket sequentially ( they are already sorted by value ), 
and get the difference of min_value with max_value of previous bucket with at least one value. 
We take maximum of all such values.
'''


def maximumGap(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    if len(arr) < 2:
        return 0

    min_v, max_v = min(arr), max(arr)
    if max_v - min_v < 2:
        return max_v - min_v

    min_gap = max(1, (max_v - min_v) // (len(arr)))  # The minimum possible gap
    sentinel_min, sentinel_max = 2 ** 32 - 1, -1
    buckets_min = [sentinel_min] * len(arr)
    buckets_max = [sentinel_max] * len(arr)

    for x in arr:
        i = min((x - min_v) // min_gap, len(arr) - 1)
        buckets_min[i] = min(buckets_min[i], x)
        buckets_max[i] = max(buckets_max[i], x)

    max_gap = 0
    prev_max = buckets_max[0]  # First gap is always non-empty
    for i in range(1, len(arr)):
        if buckets_min[i] == sentinel_min:
            continue
        max_gap = max(buckets_min[i] - prev_max, max_gap)
        prev_max = buckets_max[i]

    return max_gap


if __name__ == '__main__':

    data = [
            [[1, 10, 5], 5]
            ]
    
    for l in data:
        print('input', l[0], 'output', maximumGap(l[0]))