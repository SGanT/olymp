map = [
        [1,2,3,4,53,54],
        [5,6,7,8,51,52],
        [9,10,11,12,49,50],
        [13,14,15,16,47,48],
        [17,18,19,20,45,46],
        [21,22,23,24,43,44],
        [25,26,27,28,41,42],
        [29,30,31,32,39,40],
        [33,34,35,36,37,38]
    ]
free = []
n = int(input())
for i in range(n):
    free.append( int( input() ) )

counter = 0
checked = []
for i in map:
    tmp = 0
    for j in free:
        if j in i and j not in checked:
            checked.append( j )
            tmp+=1
    if tmp == 6:
        counter += 1
print(counter)
