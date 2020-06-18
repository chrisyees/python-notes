from random import randint

solution = randint(1, 100)
response = int(input("Try to guess the answer: "))
lastGuess = response
if abs(lastGuess - solution) > 10:
    print("COLD!")
elif abs(lastGuess - solution) < 10:
    print("WARM!")
while response != solution:
    if response > 100 or response < 1:
        print("OUT OF BOUNDS")
    elif abs(response - solution) > abs(lastGuess - solution):
        print("COLDER!")
    elif abs(response - solution) < abs(lastGuess - solution):
        print("WARMER!")
    lastGuess = response
    response = int(input("Try again: \n"))
print("You got it! The number was {}".format(solution))