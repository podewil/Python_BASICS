String = "Python is Awesome"

print(String[0])    # Prints out "P"
print(String[1])    # Prints out "y"
print(String[6])    # Prints out " "
#print(String[17])  # IndexError: string index out of range

print(String[4:8])  # Prints out "on i"
print(String[:8])   # Prints out "thon is Awesome"
print(String[8:])   # Prints out "thon is Awesome"
print(String[:])    # Prints out "Python is Awesome"

print(len("Python is Awesome"))     # len() returns the length of string
print(len(String))                  # len() returns the length of string