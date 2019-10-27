'''
Amazon Interview Question for Quality Assurance Engineers

https://www.careercup.com/question?id=5151251952566272

Given an array of positive and negative integers {-1,6,9,-4,-10,-9,8,8,4} (repetition allowed) 
sort the array in a way such that the starting from a positive number, 
the elements should be arranged as one positive and one negative element maintaining insertion order. 
First element should be starting from positive integer and 
the resultant array should look like {6,-1,9,-4,8,-10,8,-9,4}
'''

def sort_positive_negative(arr):
    i = 0
    while i<len(arr)-1:
        if arr[i]>0 and arr[i+1]<0:
            i += 2
        elif arr[i]<0 and arr[i+1]>0:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 2
        else:
            postive = 1
            if arr[i]>0:
                postive = -1
            for j in range(i+2, len(arr)):
                if postive*arr[j]>0:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                    break
    return arr


if __name__=='__main__':
    data = [
         [
          [-1, 6, 9, -4, -10, -9, 8, 8, 4],
          [6, -1, 9, -4, 8, -10, 8, -9, 4]
         ]
        ]

    for d in data:
        print('input', d[0], 'sort postive-negetive', sort_positive_negative(d[0]), 'expected', d[1])