def div47by(divideBy):
    try:
        return 47 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div47by(2))
print(div47by(12))
print(div47by(0))
print(div47by(1))

# A divide-by-zero error happens when Python divides a number by zero

# Errors cause the program to crash

# An error that happens inside a try block will cause code in the except block
# to execute. That code can handle the error or display a message to the user
# so that the program can keep going
