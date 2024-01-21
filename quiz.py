print("Welcome to my quiz!!")
playing = input("Do you want to play? ")
if playing.lower() != 'yes':
    quit()
print("Let's start then !!")

score = 0

answer = input("Who invented computer? ").lower()
if answer == "charles babbage":
    print("Correct !!")
    score += 1
else:
    print("Incorrect >_< ")

answer = input("Is java oops?? ").lower()
if answer == "yes":
    print("Correct !!")
    score += 1
else:
    print("Incorrect >_< ")

answer = input("1024 Kilobytes is equal to? ").lower()
if answer == " megabyte ":
    print("Correct !!")
    score += 1
else:
    print("Incorrect >_< ")

answer = input("Most widely spoken language in the world is? ").lower()
if answer == "mandarin":
    print("Correct !!")
    score += 1
else:
    print("Incorrect >_< ")

answer = input(" Sun is a? ").lower()
if answer == "star":
    print("Correct !!")
    score += 1
else:
    print("Incorrect >_< ")

print("You got " + str(score) + " questions correct")
ss = score * 10
print("You scored " + str(ss) + "!!!")
print("You got " + str((score/5)*100) + "% answer correct")

