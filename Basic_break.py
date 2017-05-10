targetNumber = input('please enter target Number ')  # (CBJ) input function save the user input as string


range_limit = input('please enter range limit great than ' + targetNumber)
range_limit = int(range_limit)

print(type(targetNumber))                            # (CBJ) check the type of input variable
targetNumber = int(targetNumber)                     # (CBJ) convert the string type variable into integer

if targetNumber > range_limit:                       # (CBJ) Note: Check the types of the var.
                                                     # (CBJ)       if the types are diff you cannot use the if statement
    print(targetNumber, "is out of range ", "Please try with other values")

else:
    for n in range(range_limit+1):                  # (CBJ) Note: range starts from 0 to 50

        if n is targetNumber:

            print(n, "is the target number")

            break       # (CBJ) Quit the "for loop" only
           # quit()      # (CBJ) quit the process

        else:

            print(n)



