# this function takes keyboard input from a user, gets that input
# and adds it together, and then divides by the number of integer inputs
# entered by the user to determine the average item level of a character's gear
# in World of Warcraft

# define the character_ilvl()
def char_avg_ilvl():
    #defines the variable names and takes an keyboard input from the user
    char_name = input("What is your character's name?: ")
    char_class = input("What class is your character?: ")
    char_spec = input("What specialization is your character played in?: ")
    gear_head = int(input("What is the current item level of your head piece?: "))
    gear_neck = int(input("What is the current item level of your neck piece?: "))
    gear_shoulder = int(input("what is the current item level of your shoulder piece?: "))
    gear_back = int(input("What is the current item level of your back piece?: "))
    gear_wrist = int(input("What is the current item level of your wrist piece?: "))
    gear_hands = int(input("What is the current item level of your gloves?: "))
    gear_belt = int(input("What is the current item level of your belt piece?: " ))
    gear_pants = int(input("What is the current item level of your pants?: "))
    gear_shoes = int(input("What is the current item level of your shoes/boots?: "))
    gear_ring1 = int(input("What is the current item level of your slot 1 ring?: "))
    gear_ring2 = int(input("What is the current item level of your slot 2 ring?: "))
    gear_trinket1 = int(input("What is the current item level of your slot 1 trinket?: "))
    gear_trinket2 = int(input("What is the current item level of your slot 2 trinket?: "))
    comp_check = input("If you see this statement, please type done: ")
    #if the user does not enter the word done in the comp_check variable input field, it prompts
    #the user to enter 'done' again until they do
    while comp_check != "done":
        comp_check = input("If you see this statement, please type done: ")
    else:
        #if the user does enter the word dne in the comp_check input field, it adds together all the integers
        #from the inputed numbers then divides by the total number of gear pieces to get the average item level
        if comp_check == "done":
            ilvl_totals = (gear_head + gear_neck + gear_shoulder + gear_back + gear_wrist + gear_hands + gear_belt + gear_pants + gear_shoes + gear_ring1 + gear_ring2 + gear_trinket1 + gear_trinket2)
            avg_ilvl = ilvl_totals / 13
            #once it gets the average item level, it prints a new line, and then tells the character what
            #what their average item level is.
            print("\n")
            print("Hello", char_name + ", your", char_spec, char_class + "'s average item level is: ", avg_ilvl)
