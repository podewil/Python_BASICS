def function_call():

    print("You called 'function_call' function")

def currency_exchange_USD_to_WON(USD):

    WON = USD * 1200
    print("$", USD, " is  \\", WON, sep='')      # (CBJ) in order to print out backslash "\"  you need "\\"
                                                 # (CBJ) remove spaces between values

    print("$", USD, " is  \\", WON)              # (CBJ) without removing spaces between values



function_call()                                  # (CBJ) call the previously defined function with

currency_exchange_USD_to_WON(100)                # (CBJ) call the previously defined function
