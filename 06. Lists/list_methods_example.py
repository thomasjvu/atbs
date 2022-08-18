# All list values have a METHOD called "index"
## Each data type has its own METHODS


# index() METHOD
## The index() list method returns the index of an item in the list

spam = ['hello', 'hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello')) # prints the index number of the first time this argument is called in the list
print(spam.index('heyas')) # prints the index number of the given argument
## print(spam.index('does not exist')) ## returns an error if it doesn't exist


# append() METHOD
## The append() list method adds a value to the end of a list
spam = ['cat', 'dog', 'bat']
spam.append('moose') # this METHOD adds this value to the end of the list
print(spam)
spam.append('moose') # this METHOD adds this value to the end of the list
print(spam)

# insert() METHOD
## The insert() list method adds a value anywhere inside a list


# remove() METHOD
## The remove() list method removes an item, specified by the value, from a list

spam = ['cat', 'dog', 'bat', 'bat', 'dog', 'bat']
spam.remove('bat') # this METHOD removes the first occuring instance of the value 'bat'
print(spam)

spam.remove('bat') # this METHOD removes the next instance of 'bat'
print(spam)

spam.remove('bat') # this METHOD removes the next instance of 'bat'
print(spam)

# sort() METHOD
## The sort() list method sorts the items in a list
spam = [99, 47, 32, 5, 12]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers']
spam.sort()
print(spam)
spam.sort(reverse=True) ## sorts list in reverse order
print(spam)

## Python cannot sort lists that have strings and integer types
## Sort uses ASCII-betical order. Uppercase comes before lowercase.

spam = ['Thomas', 'Elizabeth', 'carol', 'cats']
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower) #sets normal alphabetical order
print(spam)

# List methods operate on the list "in place', rather than returning a new list value
