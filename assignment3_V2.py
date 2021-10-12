#Function to ask for the player's name.

def get_name():

    player_name = input("What is your name traveler? > ")

    if player_name == "":

     print("Okay, I'll grant you a name traveler.")

     player_name = "Traveler"

    print("Let's begin your story, " + player_name + ".")

    return player_name

#This starts the adventure for the player and askes for a choice.
    
def start_adventure():
         
    choice_picked = input("Which door do you choose? > ")
                          
    if choice_picked == "Blue":
        print("You have picked the Blue door.")
                          
    elif choice_picked == "Red":
        print("You have picked the Red door.")

    else:
        print("Sorry, the correct answer is either ‘Red’ or ‘Blue’. Game over.")

#Main Program Flow
        

character = get_name()

print(character," steps into the room.")

print(character," arrives into a room with a Blue and a Red door. Please type in Blue or Red.")

start_adventure()
