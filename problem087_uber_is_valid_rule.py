'''
This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.
'''

# @rules is list of rule. [(a, dir, b)]
# direction is North South East West or NE, etc.
def isValid(rules):
    dir_ops = {'N':'S', 'S':'N', 'W':'E', 'E':'W'}
    rule_map = {}
    for (a, direction, b) in rules:
        for d in direction:
            rule = (a, d)
            if rule not in rule_map:
                rule_map[rule] = set()
            rule_map[rule].add(b)
            rule = (b, dir_ops[d])
            if rule not in rule_map:
                rule_map[rule] = set()
            rule_map[rule].add(a)

            #check rule's validity
            stack = [x for x in rule_map[(a, d)]]
            while stack:
                c = stack.pop()
                if c==a:
                    return False
                if (c, d) in rule_map:
                    for x in rule_map[(c, d)]:
                        stack.append(x)
    return True


if __name__ == "__main__":
    data = [
            [
             [('A', 'N', 'B'), ('B', 'NE', 'C'), ('C', 'N', 'A')],
             False
            ],
            [
             [('A', 'NW', 'B'), ('A', 'N', 'B')],
             True
            ]
    ]
    for d in data:
        print('input', d[0], 'output', isValid(d[0]))