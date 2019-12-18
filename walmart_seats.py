'''
Seats
Asked in: Walmart labs

https://www.interviewbit.com/problems/seats/

There is a row of seats. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.

An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')

Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.

Return minimum value % MOD where MOD = 10000003

Example

Here is the row having 15 seats represented by the String (0, 1, 2, 3, ......... , 14) -

              . . . . x . . x x . . . x . .

Now to make them sit together one of approaches is -
                  . . . . . . x x x x . . . . .

Following are the steps to achieve this -
1 - Move the person sitting at 4th index to 6th index -  
    Number of jumps by him =   (6 - 4) = 2

2 - Bring the person sitting at 12th index to 9th index - 
    Number of jumps by him = (12 - 9) = 3

So now the total number of jumps made = 
    ( 2 + 3 ) % MOD = 
    5 which is the minimum possible jumps to make them seat together.

There are also other ways to make them sit together but the number of jumps will exceed 5 and that will not be minimum.

For example bring them all towards the starting of the row i.e. start placing them from index 0. 
In that case the total number of jumps will be 
    ( 4 + 6 + 6 + 9 )%MOD 
    = 25 which is very costly and not an optimized way to do this movement

'''

# @param seats : string
# @return an integer
def seats(seats):
    n = len(seats)
    moves = 0
        
    pos = [i for i,s in enumerate(seats) if s=='x']
    if not pos: return 0
        
    start = end = pos[len(pos)//2]
    while start>=0 and seats[start]=='x':
        start -= 1
    while end<n and seats[end]=='x':
        end += 1
            
    for i in range(start-1, -1, -1):
        if seats[i]=='x':
            moves += start-i
            start -= 1
        
    for i in range(end+1, n):
        if seats[i]=='x':
            moves += i-end
            end += 1
                
    return moves%10000003


if __name__ == "__main__":
    data = [
            ['....x..xx...x..', 5],
    ]
    for d in data:
        print('input', d[0], 'output', seats(d[0]))