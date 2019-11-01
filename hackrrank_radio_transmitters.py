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

def hackerlandRadioTransmitters(houses, k):
    if not houses: return 0

    no_of_transmitter = 1
    found_new_group = True
    n = len(houses)

    houses = sorted(houses)
    target_house = houses[0]
    
    for i in range(1, n):
        if houses[i]-target_house>2*k:
            no_of_transmitter += 1
            target_house = houses[i]
            found_new_group = True
        elif houses[i]-target_house>k:
            if found_new_group:
                target_house = houses[i-1]
                if houses[i]-target_house<=k:
                    found_new_group = False
                    continue
            
            no_of_transmitter += 1
            target_house = houses[i]
            found_new_group = True
    
    return no_of_transmitter


if __name__ == '__main__':
    data = [
            [([9, 5, 4, 2, 6, 15, 12], 2), ],
            [([2, 5], 2), 2],
            [([1, 2, 3, 4, 5], 1), 2],
            [([1, 2, 3, 5, 9], 1.3), 3],
            ]
    for d in data:
        print('houses at ', d[0][0], ' with transmission range ', d[0][1], ', so minimum no of transmitters is ', hackerlandRadioTransmitters(*d[0]))