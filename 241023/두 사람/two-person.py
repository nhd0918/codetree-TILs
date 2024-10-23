valueAge1, valueSex1 = input().split()
valueAge2, valueSex2 = input().split() 

print(  1 if ( int(valueAge1) >= 19 and valueSex1 == 'M' ) or ( int(valueAge2) >= 19 and valueSex2 == 'M' ) else 0)