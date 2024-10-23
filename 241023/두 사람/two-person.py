valueAge1, valueSex1 = input().split()
valueAge2, valueSex2 = input().split() 

print(  1 if ( int(valueAge1) >= 19 or int(valueAge2) >= 19 ) or ( valueSex1 == 'M' or valueSex2 == 'M' ) else 0)