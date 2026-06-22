############# Program a robot to take your coffee order ######################  (NetworkChuck Youtube Python course) 

#imports:
import sys # Used to manipulate the Python runtime. Needed for sys.exit()
import os # Allows Python to talk to the Operating System. Needed for clear_screen()
import time # Needed to access system time. Needed for time.sleep()

# Clear the terminal screen before running Python script.
def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear') # 'nt' means Windows, 'posix' means a Unix based OS

# Fake loading animation. Can be customised with "text" and how many times to loop it
def loadingdots(text, duration_cycles) : 
    loadCount = 0
    while loadCount < duration_cycles:
        clear_screen()
        #time.sleep(0.3)
        print(text,".", end="", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        loadCount += 1

#Find current local time
local_time = time.localtime() # Presents local time in human readable format. Used to extract .tm_hour value.

# Change salutation based on time of day; morning, afternoon, evening.
if local_time.tm_hour >= 18:
    salutation = "evening"
elif local_time.tm_hour >= 12:
    salutation = "afternoon"
else:
    salutation = "morning"


#### Main program starts here: ####

try: # "Listens" for Ctrl+C input to end program cleanly.

    ## Greeting Section: ##
    clear_screen()
    print(f"Good {salutation} and welcome to our coffee shop!\n")
    time.sleep(0.5) # breifly pauses the program for (seconds)
    name = input("What is your name?\n")
    name = name.capitalize() # changes customer name to sentence case (i.e. Sam not sam, SAM, sAm etc.)

    if name == "Ben": # denies Ben entry to coffee shop and ends program
        clear_screen()
        print("You're not welcome in here " + name + "! GET OUT!!")
        sys.exit(0) # ends the program cleanly without errors (0)
    else:
        print("\nHi " + name + ", thank you for coming in today!\n")

    ## Taking order section: ##
    clear_screen()

    print("What would you like to order " + name + "?\n")
    time.sleep(0.2)

    # Store coffee menu as list
    coffee_menu = ["Americano", "Cappuccino", "Caf\u00e9 Latte", "Espresso", "Flat White"]

    # Displays the coffee menu. Uses a for loop to count the items in the coffee_menu list and prints it
    for number, drink in enumerate(coffee_menu, start=1): # Start counting at 1 rather than 0.
        print(f"{number}. {drink}")

    # Set a price for the coffee menu
    coffee_price = float(2.50)

    # Make sure the user enters an integer
    while True:
        try: 
            time.sleep(0.5)
            coffee_selection = int(input("\nPlease enter the number option of your choice.\n"))

            # Make sure number entered is between 1 and 5. 
            if 1 <= coffee_selection <= len(coffee_menu): # If 1 is less than or equal to the number entered and less than or equal to the length of the coffee list.
                break # Valid input, continue with program.
            else:
                print(f"\033[31mInvalid input:\033[0m Please type a number between 1 and  {len(coffee_menu)}.\n")
        
        except ValueError: # Catches error if a non integer is inputted.
            print("\033[31mInvalid input:\033[0m Please type a whole number.\n")

    # Ask customer how many coffees they would like to order and calculate their total bill
    no_of_coffees = int(input("\nHow many " + coffee_menu[coffee_selection - 1] + "s would you like?\n"))

    total_bill = float(coffee_price * no_of_coffees)
    clear_screen()
    input(f"\nYour total is: £{total_bill:.2f}\n(Press enter to pay)")

    loadingdots("Payment processing", 3)
    clear_screen()
    print("Payment Successful!")

    if no_of_coffees > 1:
        print(f"\nThank you {name}, your {no_of_coffees} {coffee_menu[coffee_selection - 1]}s are coming right up!\n")
    else: 
        print(f"\nThank you {name}, your {coffee_menu[coffee_selection - 1]} is coming right up!\n")
    exit()

except KeyboardInterrupt: # When Ctrl+C is pressed, end the program cleanly.
    print("\033[31m -- Program Interrupted --\033[0m")
    sys.exit(0) # ends the program cleanly without errors (0)