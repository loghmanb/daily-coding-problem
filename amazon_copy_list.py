'''
Copy List
Asked in: Amazon, Microsoft

https://www.interviewbit.com/problems/copy-list/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

Return a deep copy of the list.

Example

Given list

   1 -> 2 -> 3
with random pointers going from

  1 -> 3
  2 -> 1
  3 -> 1
You should return a deep copy of the list. The returned answer should not contain the same node as the original list, 
but a copy of them. The pointers in the returned list should not link to any node in the original input list.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# @param head, a RandomListNode
# @return a RandomListNode
def copyRandomList(head):
    if not head:
        return None
        
    n = head
    while n:
        n1 = n.next
        n.next = RandomListNode(n.label)
        n.next.next = n1
        n = n1
            
    n = head
    while n:
        if n.random:
            n.next.random = n.random.next
        n = n.next.next
        
    head = head.next
    n = head
    while n:
        n.next = n.next and n.next.next or None
        n = n.next
            
    return head

