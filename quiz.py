from tkinter.messagebox import YES


print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

#Q1
answer = input("1. What brand has the slogan ‘Have a break, have a ‘what’’? ").lower()
if answer == "kit kat":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

#Q2
answer = input("2. What is the most played sport in India and has produced many greats of the game including Sachin Tendulkar and Sunil Gavaskar? ").lower()
if answer == "cricket":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

#Q3
answer = input("3. What does www stand for? ").lower()
if answer == "world wide web":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

#Q4
answer = input("4. What is the largest country by area in the world? ").lower()
if answer == "russia":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

#Q5
answer = input("5. What is the main ingredient of bread? ").lower()
if answer == "flour":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

#Q6
answer = input("6. What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

#Q7
answer = input("7. What country is famous for inventing the Taco, Burrito and Quesadilla? ").lower()
if answer == "mexico":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

#Q8
answer = input("8. Who is the South African born CEO of SpaceX and the brains behind Tesla? ").lower()
if answer == "elon musk":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

#Q9
answer = input("9. What is the largest mammal currently inhabiting the earth? ").lower()
if answer == "blue whale":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

#Q10
answer = input("10. What company is responsible for the iPhone, iPad and iWatch and many other products? ").lower()
if answer == "apple":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")
