# ### Simulating the most exciting philosophical thought experiement in game theory Monty Hall
# The Monty Hall problem is a famous probability puzzle based on a TV game show called “Let’s Make a Deal”, hosted by Monty Hall.
# It shows how human intuition about probability can be wrong, even when the situation seems simple.

import random

NumberOfTrailRun=1000
 #door 2 has a car other has goat
winStatus=False  #Check for winStatus
choices=[1,2,3]
###ramdom Number generator function

### win and loss count variables
winCount=0
lossCount=0


def random_choice_generator(givenChoice):
    return random.choice(givenChoice)
###check for car or goat behind the door
def check_for_car(choice):
    ### door 2 has a car other has goat
    if choice==2:
        return True
    else:
        return False

for i in range(NumberOfTrailRun):
    choices = [1, 2, 3]
    print(f"Trail {i}")
    firstChoice=random_choice_generator(choices)
    choices.remove(firstChoice)
    print(f"First choice door number {firstChoice}")
    winStatus=check_for_car(firstChoice)
    if winStatus==False:
        secondChoice = random_choice_generator(choices)
        print(f"Your Second choice is ${secondChoice}")
        print(f"Would you like to switch the door?")
        # print(f"{choices} debug part*******")
        choices.remove(secondChoice)
        lastChoice =random_choice_generator(choices)
        print(f"Door switched from {secondChoice} to {lastChoice}")
        winStatus=check_for_car(lastChoice)
        if winStatus:
            winCount=winCount+1
            print(f"___You win this {i} trail and continue to next trail_____")
        else:
            lossCount=lossCount+1
            print(f"You losse trail {i} with goat")
    else:
       winCount=winCount+1
       print(f"______You win this {i} trail and continue to next trail__________")
       continue


print(f"Total win during switch{winCount}")
print(f"Total loss count {lossCount}")