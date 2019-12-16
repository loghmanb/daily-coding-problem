'''
Shortest Unique Prefix
Asked in: Google

https://www.interviewbit.com/problems/shortest-unique-prefix/

Find shortest unique prefix to represent each word in the list.

Example:

Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
 NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.
'''

def insert(bst, word):
    if not word: 
        bst['.'] = True
    else:
        if word[0] not in bst:
            bst[word[0]] = {'no': 1, 'tree':{}}
        else:
            bst[word[0]]['no'] += 1
        insert(bst[word[0]]['tree'], word[1:])
        
# @param words : list of strings
# @return a list of strings
def prefix(words):
    prefix_dict = {}
    bst = {'no':0, 'tree':{}}
    for word in words:
        insert(bst['tree'], word)
    stack = [(bst, '', '')]
    while stack:
        node, p, w = stack.pop()
        if node==True:
            prefix_dict[w] = p
            continue
            
        for key in node['tree']:
            if node['no']==1:
                pre = p
            else:
                pre = p + key
            stack.append((node['tree'][key], pre, w+key if key!='.' else w))

    result = [prefix_dict[w] for w in words]
    return result

if __name__ == "__main__":
    data = [
            [
                ['zebra', 'dog', 'duck', 'dove'],
                ['z', 'dog', 'du', 'dov']
            ]
    ]

    for d in data:
        print('input', d[0], prefix(d[0]))