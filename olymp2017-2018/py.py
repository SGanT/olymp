n = int( input() )
k = int( input() )

def bsort(a):
    for i in range( len(a) ):
        for j in range( len(a)-1, i , -1):
            if len(a[j]) > len(a[j-1]):
                b = a[j]
                a[j] = a[j-1]
                a[j-1] = b
    return a

map = ['0' for i in range(n)]
ln = len(map)
print(map)
for i in range(k):
    if ln % 2 == 0:
        x = ln // 2 - 1
        map[x] = '1'
    else:
        x = ln // 2
        map[x] = '1'

    map = bsort( ''.join(map).split('1') )
    
    print(map)
