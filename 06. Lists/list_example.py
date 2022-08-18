# Recap

# A list is a value that contains multiple values

spam = [1, 2, 3, 4, 5, 6] # The values in a list are also called items

# You can access items in a list with its integer index

# The indexes start at 0, not 1

# You can also use negative indexes. -1 refers to the last item, -2 refers to
# the second last item, and so on.
print (spam[-1])

# You can get multiple items from the list using a slice.
print (spam[1:3])

# The slice has two indexes. The new list's items start at the first index and
# go up to, but doesn't include, the second index

# The len()function, concatenation, and replication work the same way with lists
# that they do with strings
print(len(spam))
# You can convert a value into a list by passing it to the list() function.
print(list('spam'))
