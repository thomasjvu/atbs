def eggs(cheese):
    cheese.append('Hello')

spam = [1, 2, 3] 
eggs(spam) 
print(spam) ## changes in spam are reflected

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam) ## creates a copy of the list, not the reference
cheese[1] = 42
print(cheese)
print(spam)
