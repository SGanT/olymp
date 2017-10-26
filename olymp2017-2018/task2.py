def fnc(m):
    if (m % 3) != 0 and (m % 4) != 0:
        a = m - 3 - (m % 3)
        b = m - a
        if a > 0 and b > 0 and (b % 4) == 0:
            print( int( a // 3 ) )
            print( int( b // 4 ) )
        else:
            print( 0 )
            print( 0 ) 
    elif (m % 3) == 0:
        a = m - 12
        b = 12
        if a > 0:
            print(a//3)
            print(b//4)
        else:
            print(m//3)
            print(0)
    elif (m % 4) == 0:
        b = m - (m % 4)
        a = m - b
        print( int( a // 3 ) )
        print( int( b // 4 ) )


fnc( int( input() ) )
