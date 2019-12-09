'''
Remove Duplicates from Sorted List
Asked in:  
Microsoft
VMWare
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param A : head node of linked list
# @return the head node in the linked list
def deleteDuplicates(A):
    pre_node = A
    node = A and A.next
    while node:
        if pre_node.val==node.val:
            pre_node.next = node.next
        else:
            pre_node = node
        node = node.next
    return A

