eggs = 42 # global variable scope, defined outside of function

def spam():
    global eggs
    eggs = 'Ovaries' # local (temporary) variable scope, defined inside of function
    print(eggs)


spam()
print(eggs)

# scope can be thought of as an area of the source code, as a container of variables
# global scope is code outside of all functions. Variables assigned here are global variables
# each function's code is in its own local scope. Variables assigned here are local variables
# Code in the global scope cannot use any local variables
# code in a function's local scope cannot use variables in any another function's local scope
# if there's an assignment statement for a variable in a function, that is a local variable
