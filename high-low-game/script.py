import random

num_range = [1, 10]
current_number = random.randint(num_range[0], num_range[1])
score = 0

while (True):

    user_guess = input("%s\n" %current_number)
    previous_number = current_number
    
    # prevents the same random number being generated 2x in a row
    while (current_number == previous_number):
        current_number = random.randint(num_range[0], num_range[1])

    # checks whether the user's answer is right or wrong
    if (user_guess == "l"):
        if (current_number < previous_number):
            score += 1
            print("Correct!")
        else:
            print("Incorrect!. The number was %s. Your final score is %s." %(current_number, score))
            break
    elif (user_guess == "h"):
        if (current_number > previous_number):
            score += 1
            print("Correct!")
        else:
            print("Incorrect!. The number was %s. Your final score is %s." %(current_number, score))
            break
    else:
        print("Error!")
        break
