'''
HackerRank 
https://www.hackerrank.com/challenges/hackerland-radio-transmitters

Hackerland is a one-dimensional city with houses aligned at integral locations along a road. 
The Mayor wants to install radio transmitters on the roofs of the city's houses. 
Each transmitter has a fixed range meaning it can transmit a signal to all houses within 
that number of units distance away.

Given a map of Hackerland and the transmission range, determine the minimum number of transmitters 
so that every house is within range of at least one transmitter. Each transmitter must be installed 
on top of an existing house.

For example, assume houses are located at x = [1, 2, 3, 5, 9] and the transmission range k = 1.3.  
antennae at houses 2 and 5 and 9 would provide complete coverage. There is no house at location 7 
to cover both 5 and 9. Ranges of coverage, are [1, 2, 3], [5], and [9].
'''

def hackerlandRadioTransmitters(x, k):
    if not x: return 0

    x = sorted(x)
    t = []

    for i,h in enumerate(x):
        if not t or abs(t[-1]-h)>k:
            h1 = h
            for j in range(i+1, len(x)):
                if x[j]>h+k:
                    h1 = x[j-1]
                    break
            t.append(h1)
    
    return len(t)


if __name__ == '__main__':
    data = [
            ([1, 2, 3, 5, 9], 1.3),
            ]
    for d in data:
        print('houses at ', d[0], ' with transmission range ', d[1], ', so minimum no of transmitters is ', hackerlandRadioTransmitters(*d))