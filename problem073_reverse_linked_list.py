'''
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
'''

class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse(head):
    pre_pre_node = None

    while head:
        pre_node = head
        head = head.next
        pre_node.next = pre_pre_node
        pre_pre_node = pre_node
    
    return pre_node


def create_linked_list(arr):
    head = LinkedListNode(arr[0])
    node = head
    for i in range(1, len(arr)):
        node.next = LinkedListNode(arr[i])
        node = node.next
    return head


def linked_list_to_list(node):
    ans = []
    while node:
        ans.append(node.val)
        node = node.next
    return ans


if __name__ == "__main__":
    data = [
            [[1, 2, 3], [3, 2, 1]]   
    ]
    for d in data:
        arg = create_linked_list(d[0])
        print('input', linked_list_to_list(arg))
        print('output', linked_list_to_list(reverse(arg)))