'''
This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. 
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
'''

def solve(phone_no, nums):
    if not nums: return []

    ans = phone_no.get(nums[0], [])
    for i in range(1, len(nums)):
        no = ans
        ans = []
        for j in no:
            for k in phone_no.get(nums[i], []):
                ans.append(j+k)
    return ans


if __name__ == "__main__":
    data = [
            [
                [{"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, "23"],
                ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
            ]
    ]
    for d in data:
        print('input', d[0], 'output', solve(*d[0]))