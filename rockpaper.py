import random
user = 0
computer = 0
option = ["rock","paper","scissors"]
while True:
    userpick = input("Type Rock/Paper/Scissors or Q to quit ").lower()
    if userpick == 'q':
        break

    if userpick not in option:
        continue
    number = random.randint(0,2)
    # rock = 0,paper = 1,scissors = 2
    pick = option[number].lower()
    print("Computer picked",pick)
    if(userpick == 'rock' and pick == 'scissors'):
        print("You win")
        user +=1
        continue
    elif (userpick== 'paper' and pick == 'rock'):
        print("You win")
        user += 1
        continue
    elif (userpick == 'scissors' and pick == 'paper'):
        print("You win")
        user += 1
        continue
    elif (userpick == 'rock' and pick == 'rock')or(userpick == 'paper' and pick == 'paper')or (userpick == 'scissors' and pick == 'scissors'):
        continue
    else:
        print("You lost!!")
        computer += 1

print("You won ",user," times")
print("Computer won ", computer," times")
print("Goodbye!!")




