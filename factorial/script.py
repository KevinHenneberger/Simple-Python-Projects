def factorial(n):

    if (n < 0):
        return -1
    elif (n == 0):
        return 1
    else:
        f = n

        i = n - 1

        while (i >= 1): 
            f *= i
            i -= 1

        return f

print(factorial(5))
