# Clear the terminal screen before running Python script.
import os # imports the module that allows Python to talk to the OS terminal.
# 'nt' means Windows, 'posix' means a Unix based OS
# define it as a function to be called later in the program
def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')

def loadingdots() : 
    loadCount = 0
    while loadCount < 2:
        clear_screen()
        time.sleep(0.2)
        print(" .", end="", flush=True)
        time.sleep(0.2)
        print(" .", end="", flush=True)
        time.sleep(0.2)
        print(" .", end="", flush=True)
        time.sleep(0.2)
        clear_screen()
        loadCount += 1

############# Program a robot to take your coffee order ######################

#Find current local time
import time
import sys
local_time = time.localtime()
#print(local_time.tm_hour)

# Change salutation based on time of day; morning, afternoon, evening.
if local_time.tm_hour >= 18:
    salutation = "evening"
elif local_time.tm_hour >= 12:
    salutation = "afternoon"
else:
    salutation = "morning"

try: # Listens for Ctrl+C to end program cleanly.
    loadingdots()

    ### Greeting Section: ###
    clear_screen()
    print(f"Good {salutation} and welcome to our coffee shop!\n")
    time.sleep(0.5) # breifly pause the program for (seconds)
    name = input("What is your name?\n")

    print("\nHi " + name + ", thank you for coming in today!\n")

    ### Taking order section: ###
    clear_screen()

    print("What would you like to order " + name + "?\n")
    time.sleep(0.5)

    # Store coffee menu as list
    coffee_menu = ["Americano", "Cappuccino", "Caf\u00e9 Latte", "Espresso", "Flat White"]

    # Displays the coffee menu. Uses a for loop to count and print the coffee_menu list
    for number, drink in enumerate(coffee_menu, start=1):
        print(f"{number}. {drink}")
        time.sleep(0.05)


    # Make sure the user enters an integer
    while True:
        try: 
            coffee_selection = int(input("\nPlease enter the number option of your choice.\n"))

            # Make sure number entered is between 1 and 5. 
            if 1 <= coffee_selection <= len(coffee_menu): # If 1 is less than or equal to the number entered and less than or equal to the length of the coffee list.
                break # Valid input, continue with program.
            else:
                print(f"\033[31mInvalid input:\033[0m Please type a number between 1 and  {len(coffee_menu)}.\n")
        
        except ValueError: 
            print("\033[31mInvalid input:\033[0m Please type a whole number.\n")

    loadingdots()

    print("\nYour " + coffee_menu[coffee_selection - 1] + " is coming right up!\n")







except KeyboardInterrupt: # When Ctrl+C is pressed, end the program cleanly.
    print("\033[31m -- Program Interrupted --\033[0m")
    sys.exit(0) # cleanly ends program without errors.