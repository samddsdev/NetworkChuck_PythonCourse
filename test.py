#### Test file to test out bits of code ####
#------------------------------------------#

# How to get current time and then print it:
import time
local_time = time.localtime()
#print(local_time)
print(local_time.tm_hour, local_time.tm_min, local_time.tm_sec, sep=":")

# How to create a list of items and print it:
coffee_menu = "1. Cappuccino\n" + "2. Caf\u00e9 Latte\n" + "3. Espresso\n"
print(coffee_menu + "\n\n")

# How to check if user has inputted a yes or a no and display an error message if not.
while True: # The Condition is true, so causes an intentional infinite loop until the loop is escaped.
        yesno = input("Please type yes or no\n").lower().strip()

        if yesno == "yes" or yesno == "no":
            break # User has entered yes or no. continue with program. (escape out of loop!)
        else:
            print("\033[31mInvalid input:\033[0m Please type yes or no.\n")
print("\nYou typed " + yesno + "!")


