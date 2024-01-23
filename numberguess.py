import random
top = input("Enter the top number upto which you want to generate ")
if top.isdigit():
    top = int(top)
    if top <=0:
     print("Please enter a number greater than 0")
     quit()

else:
    print("Please type a digit next time")
    quit()

number = random.randint(0,top)
score = 0
while True:
    score += 1
    guess = input("Enter your guess ")
    if guess.isdigit():
        guess = int(guess)

    else:
        print("Please type a number")
        continue

    if(guess == number):
        print("You got it!!")
        break
    else:
        if guess > number:
            print("You were above the number")
        else:
            print("You are below the number")
print("You got it in",score,"number of guesses")
