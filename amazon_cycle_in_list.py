'''
List Cycle
Asked in: Amazon, Microsoft, NetApp

https://www.interviewbit.com/problems/list-cycle/

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param A : head node of linked list
# @return the first node in the cycle in the linked list
def detectCycle(A):
    pre_node = None
    node = A
    while node and node.val>0:
        node.val = -node.val
        pre_node = node
        node = node.next
    if node: node.val = -node.val
    return node


