import math
import cmath
a = int(input("Input A:"))
b = int(input("Input B:"))
c = 0

def bitwise(a,b):
    print(' ')
    print('a and b')
    print('----')
    print('Int: ', a & b)
    print('Binary: ', bin(a & b))
    print(' ')
    print('a or b')
    print('----')
    print('Int: ', a | b)
    print('Binary: ', bin(a | b))
    print(' ')
    print('a xor b')
    print('----')
    print('Int: ', a ^ b)
    print('Binary: ', bin(a ^ b))
    print(' ')
    print('not a')
    print('----')
    print('Int: ', ~a)
    print('Binary: ', bin(~a))
    print(' ')
    print('not b')
    print('----')
    print('Int: ', ~b)
    print('Binary: ', bin(~b))
    print(' ')
    print('Left Shift a << b')
    print('----')
    print('Int: ', a << b)
    print('Binary: ', bin(a << b))
    # left shift
    print(' ')
    print('Right Shift a >> b')
    print('----')
    print('Int: ', a >> b)
    print('Binary: ', bin(a >> b))
    # arithmetic right shift
bitwise(a,b)