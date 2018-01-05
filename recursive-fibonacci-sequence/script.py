def fibonacci_sequence(t):

    if (t == 0):
        return 1

    if (t == 1):
        return 1

    return fibonacci_sequence(t - 2) + fibonacci_sequence(t - 1)

for i in range(10):
    print(fibonacci_sequence(i))
