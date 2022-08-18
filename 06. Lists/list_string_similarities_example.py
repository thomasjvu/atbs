# Lists and Strings
print(list('Hello')) # Prints a list of the string

# Strings can do a lot of the same things lists can do, but strings are immutable
# Immutable values like strings and tuples cannot be modified "in place"
# Mutale values like lists can be modified in place
# Variables don't contain lists, they contain references to lists
# When passing a list argument to a function, you are actually passing a list reference
# Changes made to a list in a function will affect the list outside the function


# List is Mutable and can be changed
# String is immutable and cannot be changed

# The proper way to modify a string is by using slices
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

# The difference between immutable and mutables comes up with "references"
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

# Lists create references to the data, so the same list is changed
# Variables don't create lists, they create references to a created list
# Mutable variables / values can be considered as references
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese)
print(spam)

# Immutable values don't have this problem because they can't be modified "in place", they can only be replaced by new values.
