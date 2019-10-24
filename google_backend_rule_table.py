'''
Google Interview Question for Backend Developers

https://www.careercup.com/question?id=5651823193489408

You have a table :
Rule1 Rule2 Rule3 Value
A1      B2      C3      40
A1 	    B1	    C1      20
A2      B2      C2      10
A1      B1      C1      40
*       B1      *       20
A5      B2      *       10

Now if I have a condition A1 & B2 & C3 i will get output as 40.
If I input A1 &amp;&amp; B1 &amp;&amp; C1 I will get two results 40 and 20 here there the rule is ambiguous.
"-" in table means any rule, 5th row matches with any row with B1 as rule2, so there is also ambiguity in result.

Now given that table as input (m * n) where n is number of available rules combination (here its 6) 
and m rules (3 in this case) , output if the table is ambiguous i.e it will output two different result
for same query.
'''

from collections import deque
from bisect import insort

class RuleMap:
    def __init__(self, n):
        self._n = n
        self._rules = {}

    def add_rule(self, rule, value):
        rules = self._rules
        for i,x in enumerate(rule):
            if x not in rules:
                rules[x] = {}
            if i==self._n-1:
                rules[x] = value
            else:
                rules = rules[x]
    
    def get_value(self, rule):
        ans = []
        q = deque()
        #rule/similarity/index
        q.append([self._rules, 0, 0])
        while q:
            curr_rule, similarity, idx = q.popleft()
            if rule[idx] in curr_rule:
                if idx==self._n-1:
                    insort(ans, (similarity+1, curr_rule[rule[idx]]))
                else:
                    q.append([curr_rule[rule[idx]], similarity+1, idx+1])
            if '*' in curr_rule:
                if idx==self._n-1:
                    insort(ans, (similarity, curr_rule['*']))
                else:
                    q.append([curr_rule['*'], similarity, idx+1])
        
        return ans and ans[-1][1]


if __name__=='__main__':
    data = [
            [3,
                [
                 [['A1', 'B1', 'C1'], 30],
                 [['*', 'B1', 'C2'], 20],
                 [['A2', 'B1', '*'], 25]
                ],
                [
                 [['A1', 'B1', 'C1'], 30],
                 [['A1', 'B1', 'C2'], 20],
                 [['A2', 'B1', 'C3'], 25],
                ]
            ]
           ]
           
    print('Check rules with maximum match:')
    for d in data:
        rm = RuleMap(d[0])
        for r in d[1]:
            rm.add_rule(*r)
        for r in d[2]:
            print('for rule: ', r[0], 'output is', rm.get_value(r[0]), 'expected', r[1])


