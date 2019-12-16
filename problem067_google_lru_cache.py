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
    
    def __str__(self):
        return self.value

    def __repr__(self):
        return '%s[%s]' % (self.key, self.value)

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
        node = Node(key, value)
        node.next = self.head
        if self.head:
            self.head.back = node
        self.head = node
        if self.last_node is None:
            self.last_node = node
        self.size += 1
        return node

    def remove_from_tail(self):
        node = self.last_node
        self.last_node = self.last_node.back
        if self.last_node is not None:
            self.last_node.next = None
        self.size -= 1
        node.back = None
        return node

    def move_to_head(self, node):
        if self.head==self.last_node or self.head==node:
            return
        elif node==self.last_node:
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
        self.head = node

    def __len__(self):
        return self.size

    def __str__(self):
        s = ''
        node = self.head
        while node:
            s += '->%s' % (repr(node),)
            node = node.next
        
        s2 = ''
        node = self.last_node
        while node:
            s2 = '%s<-' % (repr(node),) + s2
            node = node.back
        return s+' || '+s2

    def __repr__(self):
        return self.__str__()


class LRUCache:
    def __init__(self, n):
        self.size = n
        self.mem = LinkedList()
        self.mem_key = {}

    def set(self, key, value):
        node = self.mem_key.get(key)
        if node is None:
            if len(self.mem)>=self.size:
                node = self.mem.remove_from_tail()
                del self.mem_key[node.key]
            node = self.mem.insert_in_head(key, value)
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


if __name__ == "__main__":
    data = [
          [
            [59, [['S', [2, 1]], ['S', [1, 10]],['S', [8, 13]], ['G', 12], ['S', [2, 8]], ['G', 11], ['G', 7], ['S', [14, 7]],
                  ['S', [12, 9]], ['S', [7, 10]], ['G', 11], ['S', [9, 3]], ['S', [14, 15]], ['G', 15], ['G', 9], ['S', [4, 13]],
                  ['G', 3], ['S', [13, 7]], ['G', 2], ['S', [5, 9]], ['G', 6], ['G', 13], ['S', [4, 5]], ['S', [3, 2]], ['S', [4, 12]], 
                  ['G', 13], ['G', 7], ['S', [9, 7]], ['G', 3], ['G', 6], ['G', 2], ['S', [8, 4]], ['S', [8, 9]], ['S', [1, 4]], ['S', [2, 9]],
                  ['S', [8, 8]], ['G', 13], ['G', 3], ['G', 13], ['G', 6], ['S', [3, 8]], ['G', 14], ['G', 4], ['S', [5, 6]], ['S', [10, 15]], 
                  ['G', 12], ['S', [13, 5]], ['S', [10, 9]], ['S', [3, 12]], ['S', [14, 15]], ['G', 4], ['S', [10, 5]], ['G', 5], ['G', 15],
                  ['S', [7, 6]], ['G', 1], ['S', [5, 12]], ['S', [1, 6]], ['S', [11, 8]]]
           ],
           [None, None, None, None, None, 3, None, 8, None, 7, 7, -1, 2, None, 8, 7, 2, 7, None, -1, 12, -1, 12, 6, -1, -1,]
          ],
          [
           [2, [['S', [1, 10]], ['S', [5, 12]], ['G', 5], ['G', 1], ['G', 10], ['S', [6, 14]], ['G', 5]]],
           []
          ],
    ]
    for d in data:
        lru = LRUCache(d[0][0])
        print('input', d[0][1])
        for cmd in d[0][1]:
            if cmd[0]=='S':
                lru.set(*cmd[1])
            else:
                print(lru.get(cmd[1]))