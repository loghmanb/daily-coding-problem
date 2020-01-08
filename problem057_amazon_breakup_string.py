'''
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. 
You must break it up so that words don't break across lines. 
Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, 
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. 
No string in the list has a length of more than 10.
'''

def breakupString(string, k):
    ans = []

    string = string.split()
    line = ''
    for i in range(len(string)):
        if not line and len(string[i])>k:
            return 0
        elif len(line)+len(string[i])+1>k:
            ans.append(line)
            line = string[i]
        else:
            if line: line += ' '
            line += string[i]
    if line:
        ans.append(line)

    return ans


if __name__ == "__main__":
    data = [
            [
                ["the quick brown fox jumps over the lazy dog", 10],
                ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
            ]
    ]
    for d in data:
        print('input', d[0], 'output', breakupString(*d[0]))