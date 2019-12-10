'''
SUBTRACT
Given a singly linked list, modify the value of first half nodes such that :

https://www.interviewbit.com/problems/subtract/

1st node’s new value = the last node’s value - first node’s current value
2nd node’s new value = the second last node’s value - 2nd node’s current value,
and so on …

 NOTE :
If the length L of linked list is odd, then the first half implies at first floor(L/2) nodes. So, if L = 5, the first half refers to first 2 nodes.
If the length L of linked list is even, then the first half implies at first L/2 nodes. So, if L = 4, the first half refers to first 2 nodes.
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5,

You should return 4 -> 2 -> 3 -> 4 -> 5
as

for first node, 5 - 1 = 4
for second node, 4 - 2 = 2
Try to solve the problem using constant extra space.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param A : head node of linked list
# @return the head node in the linked list
def subtract(A):
    pre_pre_node, pre_node = None, None
    slow = A
    fast = A
    while fast and fast.next:
        pre_pre_node = pre_node
        pre_node = slow
            
        slow = slow.next
        fast = fast.next.next
            
        pre_node.next = pre_pre_node
        
    if fast:
        right = slow.next
        left = slow.next = pre_node
    else:
        right = slow
        left = slow = pre_node

    right_node = right
        
    while left and right:
        left.val = right.val-left.val
        left = left.next
        right = right.next

    node = slow
    pre_pre_node, pre_node = right_node, None
    while node:
        pre_node = node
        node = node.next
        pre_node.next = pre_pre_node
        pre_pre_node = pre_node
            
    return A