'''
This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
'''

def noOfAttacks(N, A):
    left_diagonal = {}
    right_diagnoal = {}

    for bishop in A:
        bias = min(bishop)
        key = (bishop[0]-bias, bishop[1]-bias)
        left_diagonal[key] = left_diagonal.get(key, 0) + 1

        bias = min(bishop[0], N-1-bishop[1])
        key = (bishop[0]-bias, N-1-bishop[1]-bias)
        right_diagnoal[key] = right_diagnoal.get(key, 0) + 1

    no_of_attacks = 0
    for key in left_diagonal:
        no_of_attacks += left_diagonal[key]*(left_diagonal[key]-1)//2
    for key in right_diagnoal:
        no_of_attacks += right_diagnoal[key]*(right_diagnoal[key]-1)//2
    return no_of_attacks


if __name__ == "__main__":
    data = [
            [[5, [(0, 0), (1, 2), (2, 2), (4, 0)]], 2],
    ]
    for d in data:
        print('input', d[0], 'output', noOfAttacks(*d[0]))
