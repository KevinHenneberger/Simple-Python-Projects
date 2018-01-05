import math

def primality_test(n):

    if (n < 2):
        return -1
        
    elif (n == 2):
        return True

    elif (n % 2 == 0):
        return False

    i = 3

    while (i <= math.sqrt(n)): 
        if (n % i == 0):
            return False

        i += 2

    return True

print(primality_test(9))
