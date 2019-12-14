'''
Merge K Sorted Lists
Asked in: Flipkart, Amazon, Google

https://www.interviewbit.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list.

Example :

1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
'''

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param A : list of linked list
# @return the head node in the linked list
def mergeKLists(A):
    heap = [(x.val, x) for x in A]
    heapq.heapify(heap)
    head = None
    pre_node = None
    while heap:
        val, node = heapq.heappop(heap)
        if head is None:
            head = pre_node = node
        else:
            pre_node.next = node
            pre_node = node
        if node.next is not None:
            node = node.next
            heapq.heappush(heap, (node.val, node))
    return head


