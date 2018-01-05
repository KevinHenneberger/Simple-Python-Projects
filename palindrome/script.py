import math

def first_digit(n):
    return n[0]


def last_digit(n):
    return n[-1]


def middle_digits(n):
    return n[1:-1]


def palindrome(n):

    if (len(n) <= 1):
        return True

    if (first_digit(n) != last_digit(n)):
        return False

    return palindrome(middle_digits(n))


def greatest_palindromic_product(number_of_digits):

    max_value = int(math.pow(10, number_of_digits) - 1)

    a = max_value
    b = max_value

    greatest_palindrome = 0

    while (a > 0):
        while (b > 0):

            product = a * b

            if (palindrome(str(product))):
                while (product > greatest_palindrome):
                    greatest_palindrome = product

            b -= 1

        a -= 1
        b = max_value

    return greatest_palindrome

print("Answer: %s" %greatest_palindromic_product(3))
