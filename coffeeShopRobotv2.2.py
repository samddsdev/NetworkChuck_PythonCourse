############# Program a robot to take your coffee order ######################  (NetworkChuck Youtube Python course)

# imports:
import sys  # Used to manipulate the Python runtime. Needed for sys.exit()
import time  # Needed to access system time. Needed for time.sleep()


# Clear the terminal screen before running Python script.
def clear_screen():
    print("\033[H\033[2J\n", end="")  # \033[H moves the cursor to the top left corner. \033[2J clears the terminal screen.


# Fake loading animation. Can be customised with "text" and how many times to loop it
def loadingdots(text, duration_cycles):
    loadCount = 0
    while loadCount < duration_cycles:
        clear_screen()
        # time.sleep(0.3)
        print(text, ".", end="", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        loadCount += 1

# Find current local time
local_time = (time.localtime())  # Presents local time in human readable format. Used to extract .tm_hour value.

# Change salutation based on time of day; morning, afternoon, evening.
if local_time.tm_hour >= 18:
    salutation = "evening"
elif local_time.tm_hour >= 12:
    salutation = "afternoon"
else:
    salutation = "morning"


#### Main program starts here: ####

try:  # "Listens" for Ctrl+C input to end program cleanly.
    ## Greeting Section: ##
    clear_screen()
    print(f"Good {salutation} and welcome to our coffee shop!\n")
    time.sleep(0.5)  # breifly pauses the program for (seconds)
    name = (input("What is your name?\n").capitalize().strip())  # capitalises first letter of name and removes spaces.

    if name == "Ben":
        clear_screen()
        evil_status = input("Are you evil?\n").lower().strip()
        if (evil_status == "yes"):  # denies evil Ben entry to coffee shop and ends program
            clear_screen()
            print("You're not welcome in here " + name + "! Get Out!!")
            sys.exit(0)  # ends the program cleanly without errors (0)
        else:
            clear_screen()
            print("Oh, you're one of those good Bens. Come on in!")
            time.sleep(3)
    else:
        print("\nHi " + name + ", thank you for coming in today!\n")

    ## Taking order section: ##
    clear_screen()

    print("What would you like to order " + name + "?\n")
    time.sleep(0.2)

    # Store coffee menu as list
    coffee_menu = ["Americano","Cappuccino","Caf\u00e9 Latte","Espresso","Flat White"]

    # Displays the coffee menu. Uses a for loop to count the items in the coffee_menu list and prints it
    for number, drink in enumerate(coffee_menu, start=1):  # Start counting at 1 rather than 0.
        print(f"{number}. {drink}")

    # Make sure the user enters an integer
    while True:
        try:
            time.sleep(0.5)
            coffee_selection = int(input("\nPlease enter the number option of your choice.\n").strip())

            # Make sure number entered is between 1 and 5.
            if (1 <= coffee_selection <= len(coffee_menu)):  # If 1 is less than or equal to the number entered and less than or equal to the length of the coffee list.
                break  # Valid input, continue with program.
            else:
                print(f"\033[31mInvalid input:\033[0m Please type a number between 1 and  {len(coffee_menu)}.\n")

        except ValueError:  # Catches error if a non integer is inputted.
            print("\033[31mInvalid input:\033[0m Please type a whole number.\n")

    # Set price for the coffee
    if coffee_selection == 1:
        coffee_price = 2.60
    elif coffee_selection == 2:
        coffee_price = 3.00
    elif coffee_selection == 3:
        coffee_price = 3.00
    elif coffee_selection == 4:
        coffee_price = 2.30
    elif coffee_selection == 5:
        coffee_price = 2.80

    # Ask customer how many coffees they would like to order and calculate their total bill
    print(f"\n{coffee_menu[coffee_selection - 1]}s are £{coffee_price:.2f}")
    # Make sure user inputs integer
    while True:
        try:
            no_of_coffees = int(input("\nHow many " + coffee_menu[coffee_selection - 1] + "s would you like?\n").strip())
            break # input correct, continue with program
        except ValueError: # if a non integer is inputted display error
            print("\033[31mInvalid input:\033[0m Please type a whole number.\n")

    total_bill = coffee_price * no_of_coffees
    clear_screen()
    input(f"\nYour total is: £{total_bill:.2f}\n(Press enter to pay)")

    loadingdots("Payment processing", 2)
    clear_screen()
    print("Payment Successful!")

    if no_of_coffees > 1:
        print(f"\nThank you {name}, your {no_of_coffees} {coffee_menu[coffee_selection - 1]}s are coming right up!\n")
    else:
        print(f"\nThank you {name}, your {coffee_menu[coffee_selection - 1]} is coming right up!\n")

except KeyboardInterrupt:  # When Ctrl+C is pressed, end the program cleanly.
    print("\033[31m -- Program Interrupted --\033[0m")
    sys.exit(0)  # ends the program cleanly without errors (0)