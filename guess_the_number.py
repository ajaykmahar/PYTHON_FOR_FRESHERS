import random

# generate random number btw 1 to 20
number = random.randint(1, 20)

# user will have 3 try to guess the correct number
attempt = 3

# infinite while loop
while True:
    # execute all the statements inside 'if' block
    # if user have any attempt left
    if attempt > 0:
        print("You have {} attempts left.".format(attempt))

        # print line to sperate each execution.
        print("_" * 60)

        # asking user to guess the number
        guess = int(input("Enter an integer from 1 to 20: "))

        # if user guess the right number
        if guess == number:
            print("Congratulations! You have guessed it right. ")
            break

        # if the guess number is less than original number
        elif guess < number:
            print("Nope! It's littel higher than that.")

        # else block if guess number is grater than original number.
        else:
            print("Nope! It's littel lower than that.")

        # reduce the attempt by 1 each time
        attempt -= 1

    # if all the attempt used Game over.
    else:
        print("Game over. :( Right number was : {}".format(number))
        break

