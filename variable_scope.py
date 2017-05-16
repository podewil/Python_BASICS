# variable accessibility

temp1 = 74

def temp_room1():
    temp2 = 71
    print(temp1)           # command 1

def temp_room2():
    print(temp1)           # command 2
                           # command 1 & 2 both can access the global variable 'temp1'

   # print(temp2)           # this command results in error message
                           # because this tries to access local variable 'temp2'


temp_room1()
temp_room2()