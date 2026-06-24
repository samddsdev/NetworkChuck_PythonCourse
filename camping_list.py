#### Learn about Python lists ####

# Boring ordinary string
camping_stuff = "tent, sleeping bags, water, raspberry pi, coffee, knife, ethernet cable, flash drive, beard oil, marshmallows"
print(camping_stuff + "\n")

# PYTHON LIST
camping_list = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 89.3, True]

me = camping_list[4]
you = camping_list[-1]

print(me)
print(you)

print(f"\n{camping_list}\n")

# Add toilet paper to the camping_list

camping_list.append("toilet paper")
print(f"\n{camping_list}\n")

# Add more than one item to the camping_list using .extend 
camping_list.extend(["bidet", "cookies"])
print(f"\n{camping_list}\n")

# Alternate way to add items to a list:
camping_list = camping_list + ["headphones", "USB charger"]
print(f"\n{camping_list}\n")


# Add an item inside the list using .insert
camping_list.insert(0, "sunglasses")
print(f"\n{camping_list}\n")

camping_list.insert(6, "kindle")
print(f"\n{camping_list}\n")

camping_list.insert(-1, "wet wipes")
print(f"\n{camping_list}\n")


# Remove items from a list by name (one item at a time)
camping_list.remove("tent")
camping_list.remove("sleeping bags")
print(f"\n{camping_list}\n")

# Remove items from a list by the index number and return the value
print("These items were just deleted:\n" + camping_list.pop(6))
print(camping_list.pop(5))
print(f"\n{camping_list}\n")

# Clear all items from a list
camping_list.clear()
print(f"\n{camping_list}\n")