def fibonacci_sequence(t):

    sequence = []

    a = 0
    b = 0
    c = 1

    while (len(sequence) < t):

        sequence.append(c)
        
        a = b
        b = c
        c = a + b

    return sequence

print(fibonacci_sequence(10))
