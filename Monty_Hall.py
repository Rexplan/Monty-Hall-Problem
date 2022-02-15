# This program will simulate the well-known Monty Hall problem a number of times, twice. The first time, the program
# will take a new door after one of the bad doors are exposed and the second time the program will stick to its first
# choice.

# imports here
import random  # Import the random library for random numbers

# Global values are stored here
wins_when_choosing_new_door = 0
loses_when_choosing_new_door = 0

wins_when_sticking_to_choice = 0
loses_when_sticking_to_choice = 0
# This function create
def main():

    # Let the user choose how many times to simulate each scenario
    while True:
        try:
            rounds = int(input("Please enter how many times you wish to simulate each scenario: "))
            if rounds >= 0:
                break
            else:
                print("Invalid input, input must be greater than zero.")
        except:
                print("Error, try again.")

    for i in range(2):
        if i == 0:
            pick_new_door=True
        else:
            pick_new_door=False
        # Simulate the game a hundred time, once with the program sticking to its first choice and once were it doesn't.
        for n in range(rounds):
            # First, we generate which "doors" is good and which two are bad. We make a list of 1 to 3, then we shuffle
            # them into a random order. The content of each door is then assigned a door number.
            doors=["Car","Goat","Goat"]
            random.shuffle(doors)
            door1=doors[0]
            door2=doors[1]
            door3=doors[2]

            # The program will now choose a "door" by picking a random number between 1 and 3
            pc_choice = random.randint(1,3)
            if pc_choice == 1:
                pc_choice = door1
            elif pc_choice == 2:
                pc_choice = door2
            elif pc_choice == 3:
                pc_choice = door3

            # The program will now reveal what's behind one of the two remaining doors, but never the one with the car.
            while True:
                exposed_door_list = [door1, door2, door3]
                random.shuffle(exposed_door_list)
                for door in exposed_door_list:
                    if door == "Goat" and door != pc_choice:
                        door = "Exposed"
                        break
                break

            # If this is the first loop, then the program will pick the sole remaining door instead of sticking with
            # its current one.
            if pick_new_door:
                if door1 != "Exposed" and door1 != pc_choice:
                    new_pc_choice = door1
                elif door2 != "Exposed" and door2 != pc_choice:
                    new_pc_choice = door2
                elif door3 != "Exposed" and door3 != pc_choice:
                    new_pc_choice = door3

            # Now we check if the program picked well or not. If the chosen door is equal to "car", it's a win, if its
            # not, it's a loss. Depending on if it's the first loop or not, the win/loss will be saved to either
            # wins_when_choosing_new_door/loses_when_choosing_new_door or wins_when_sticking_to_choice/
            # loses_when_sticking_to_choice.
            if pick_new_door:
                global wins_when_choosing_new_door, loses_when_choosing_new_door
                if new_pc_choice == "Car":
                    wins_when_choosing_new_door += 1
                else:
                    loses_when_choosing_new_door += 1
            else:
                global wins_when_sticking_to_choice, loses_when_sticking_to_choice
                if pc_choice == "Car":
                    wins_when_sticking_to_choice += 1
                else:
                    loses_when_sticking_to_choice += 1

    # Now we display the results
    results()

def results():
    print("When picking a new door, the computer won", wins_when_choosing_new_door, "times and lost", loses_when_choosing_new_door, "times.")
    print("When sticking to its first choice, the computer won", wins_when_sticking_to_choice, "times and lost", loses_when_sticking_to_choice, "times.")
    input("Press enter to quit")

# Call on main
main()