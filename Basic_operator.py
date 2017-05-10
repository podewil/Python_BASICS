#https://docs.python.org/3/library/operator.html

import operator

a,b,c,d,e,f=1,3,7,'hello','world',' '
h=['a','b','c']
g=operator.iadd(d,f)
print(operator.iadd(h,g))
print(operator.add(a,b))
print(operator.iadd(g,e))
