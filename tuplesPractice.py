# Practice with tuples and learn how they compare to lists
# tuples use () & , lists use []

alist = ["bernard", "hackwell", 92]
print(alist)

# Change item in list - Cannot change Tuples. 
alist[0] = "Chuck"
print(alist)

atuple = ("bernard", "hackwell", 92)

# Tuples are FASTER than lists
# speed test:

import timeit
#list speed test
print(timeit.timeit(stmt='["red", "blue", "green", 5, 7, 12, 18, "dude"]', number=10000000))

#tuple speed test
print(timeit.timeit(stmt='("red", "blue", "green", 5, 7, 12, 18, "dude")', number=10000000))

# other way of defining a tuple 
tupletest = 1,
print(type(tupletest))
