registered_BackNumber = [3, 7, 23, 12, 10, 15]

print ("Please choose your back number one of the followings")

for n in range(1, 30+1):  # Run "for" loop 1 to 30
    if n in registered_BackNumber:   # Check whether a given number is within the registered back numbers
        continue                    # when the "if" statement is satisfied, continues the next iteration of the loop
    print(n)


