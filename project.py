lowerbound=int(input("Enter the lower bound: "))
upperbound=int(input("Enter the upper bound: "))
chances=int(input("Enter the number of chances needed: "))
print("Hi welcome to the game, This is a number guessing game.\nYou got",chances,"chances to guess the number. Let's start the game")
number_to_guess = random.randint(lowerbound,upperbound)
guess_counter = 0
while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input('Please Enter your Guess : '))
    if my_guess == number_to_guess:
        print(f'The number is {number_to_guess} and you found it right !! in the {guess_counter} attempt')
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'Oops sorry, The number is {number_to_guess} better luck next time')
    elif my_guess > number_to_guess:
        print('Your guess is higher ')
    elif my_guess < number_to_guess:
        print('Your guess is lesser')