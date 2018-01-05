import random

num_range = [1, 10]
random_number = random.randint(num_range[0], num_range[1])
num_guesses = 0

while True:

    user_input = int(input("Guess a number between %s and %s...\n" %(num_range[0], num_range[1])))
    user_number = int(user_input)

    # tell the user feedback on their guess
    if (user_number == random_number):
        print("Correct! It took you %s guesses." %num_guesses)
        break
    else:
        num_guesses += 1

        if (user_number < random_number):
            print("Too low!")
        else:
            print("Too high!" )  
