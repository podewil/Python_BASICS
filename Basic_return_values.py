# For better understanding, compare with the BASIC_function.py

def currency_exchange_USD_to_WON(USD):

    WON = USD * 1200
    print("$", USD, " is  \\", WON, sep='')      # (CBJ) in order to print out backslash "\"  you need "\\"
                                                 # (CBJ) remove spaces between values

    print("$", USD, " is  \\", WON)              # (CBJ) without removing spaces between values

    return WON                                  # with out this line, 15th command line returns "None"

value = currency_exchange_USD_to_WON(100)                # (CBJ) call the previously defined function

print(value)