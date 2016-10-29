# Title: Hack:BitwiseOps
## Timestamp: 2016-01-30 08:39:30 +0000
## Created: 2016-01-30 08:25:20 +0000
## Last Accessed: 2016-01-30 08:25:20 +0000
## Times Accessed: 0
## Tags: Bitwise, Hacks
## Metadata: 
## gpslongitude=-93.642660,gpslatitude=42.040632

#----
i = int(input('i: '))
print(' ')
print('Bitwise alternatives to division, multiplication, and modulus.')
print('----')
print(' ')

print('Multiplication')
print('----')
print('Typical: ', i*8)
# print('i*8', i*8)
#    normal
print('Bitwise: ', i << 3, bin(i << 3))
print(' ')

print('Division')
print('----')
print('Typical: ', i/16)
# normal
print('Bitwise: ', i >> 4, bin(i >> 4))

print(' ')
print('Modulus')
print('----')
print('Must be in binary!!')
print('i:', i, bin(i))
print('i & 3: ', i & 3, bin(i & 3))
print('((i << 2) -i) : ', ((i << 2) -i), bin((i << 2) - i) )  
# i.e 1 << 2 gives you 3 applied as ((1 << 2) -1)

print(' ')
print('"Ceiling" Hack')
print('----')
print('We wanted the next multiple of 512 of a given number n:')
n = i 
m = (n << 9)
o = m + 1
multiple = o * 512
print('n: ', n)
print('Multiple: ', multiple)

#(n << 9) = m
# m + 1
# (m + 1)*512