'''
This problem was asked by Dropbox.
Given the root to a binary search tree, find the second largest node in the tree.


       10
      /   \
    5      [20]
             \ 
              30 

        30
      /
    [20]
    /
   10

        30
       /
      10
        \
        [20]

'''

def find_second_largest(root, *t):
    d = {}
    for n in t:
        d[n[0]] = [n[1], n[2]]

    pre_n = d[root][0]
    n = root
    while n in d and d[n][1]:
        pre_n = n
        n = d[n][1]
    
    if n in d:
        n = pre_n
        while n in d and d[n][1]:
            n = d[n][1]
    else:
        n = pre_n
    return n

if __name__ == '__main__':
    data = [
            [20, [10, (10, 5, 20), (20, None, 30)]],
            [20, [30, (30, 20, None), (20, 10, None)]],
            [20, [30, (30, 10, None), (10, None, 20)]],
            ]
    
    for r in data:
        print('second largest is ', find_second_largest(*r[1]))