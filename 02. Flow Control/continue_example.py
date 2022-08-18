spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue # jumps back to start of the loop, so it skips 3.
    print('spam is ' + str(spam))
