def summation(*args):  # asterisk sign '*' means there will be a bunch of unknown arguments
                         # args: this is common notation among Python programmers
    sum = 0              # initialize
    for a in args:
        sum += a         # sum = adding all arguments

    return sum

print(summation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(summation(1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100))

