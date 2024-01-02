print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

text = "Jasmine Is Great!"
print(text.lower())

if playing != "Yes":
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input("What does CPU Stand for? ")
if answer == "Central Processing Unit":
    print('Correct!')
    score += 1

else:
    print("Incorrect!")

answer = input("What does GPU Stand for? ")
if answer == "Graphical Processing Unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM Stand for? ")
if answer == "Random Access Memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM Stand for? ")
if answer == "Read Only Memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " Questions Correct ")
print("You got " + str((score / 4) * 100) + "%.")
