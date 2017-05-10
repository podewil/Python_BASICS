a = "Python String"
b = " is awesome"
print('Python Strings')
print("Python's Strings")

#print('Python's Strings')       # SyntaxError: invalid syntax
print('Python\'s Strings')       # This will fix the SyntaxError

print("Python's Strings")        # This is correct
print("Python Strings")

print(a*3)
print(a+b)
print(a + " is awesome")

# Issues when we print out directory
print("C:\Desktop\podewil\new")  # "\n" is a special character which represents "convert row"
                                 # This will print out
                                 #           C:\Desktop\podewil
                                 #           ew

print(r'C:\Desktop\podewil\new') # By adding 'r' we can resolve above issue
                                 # This will print out C:\Desktop\podewil\new