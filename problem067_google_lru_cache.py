'''
This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache. 
It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. 
If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. 
If there is a tie, then the least recently used key should be removed.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.

'''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.back = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last_node = None

    def add_to_tail(self, key, value):
        node = Node(key, value)
        if self.head is None:
            self.head = node
        else:
            node.back = self.last_node
            self.last_node.next = node
        self.last_node = node
        self.size += 1

    def insert_in_head(self, key, value):
        node = Node(value)
        node.next = self.head
        self.head.back = node
        self.head = node
        self.size += 1
        return node

    def remove_from_tail():
        node = self.last_node
        self.last_node = self.last_node.back
        if self.last_node is not None:
            self.last_node.next = None
        self.size -= 1
        node.back = None
        return node

    def move_to_head(self, node):
        if self.head==self.last_node:
            return
        elif node == self.last_node:
            self.last_node = node.back
        pre_node = node.back
        if pre_node is not None:
            pre_node.next = node.next
        if node.next is not None:
            node.next.back = pre_node
        node.next = self.head
        if node.next is not None:
            node.next.back = node
        node.back = None

    def __sizeof__(self):
        return self.size


class LRUCache:
    def __init__(self, n):
        self.size = n
        self.mem = LinkedList()
        self.mem_key = {}

    def set(key, value):
        node = self.mem_key.get(key)
        if node is None:
            if len(self.mem)>=self.size:
                node = self.mem.remove_from_tail()
                del self.mem[node.key]
            node = self.mem.insert_in_head(value)
            self.mem_key[key] = node
        else:
            #update its value and move node to the head
            node.value = value
            self.mem.move_to_head(node)

    def get(self, key):
        node = self.mem_key.get(key)
        if node is not None:
            #move to the head
            self.mem.move_to_head(node)
            return node.value
        return None
            