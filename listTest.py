import time

local_time = time.localtime()

#print(local_time)
print(local_time.tm_hour, local_time.tm_min, local_time.tm_sec, sep=":")

coffee_menu = "1. Cappuccino\n" + "2. Caf\u00e9 Latte\n" + "3. Espresso\n"

print(coffee_menu)