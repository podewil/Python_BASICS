Grades =[77, 80, 99, 100, 65]

print(Grades[0])       # Prints out "[77]"
print(Grades[1])       # Prints out "[80]"
print(Grades[2])       # Prints out "[99]"
#print(Grades[5])    # IndexError: list index out of range

new_Grades = Grades + [80, 87, 60]
print(new_Grades)       # Prints out "[77, 80, 99, 100, 65, 80, 87, 60]"

# Using .append()
Grades.append(80) # Note! append() takes exactly one argument
Grades.append(87)
Grades.append(60)
print(Grades)           # Prints out "[77, 80, 99, 100, 65, 80, 87, 60]"

Grades[:2] = [0,0]
print(Grades)           # Prints out "[0, 0, 99, 100, 65, 80, 87, 60]"

Grades[:2] = []
print(Grades)           # Prints out "[99, 100, 65, 80, 87, 60]"

Grades[:] = []
print(Grades)           # Prints out "[]"