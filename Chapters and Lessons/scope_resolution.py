# VARIABLE SCOPE = where a variable is visible and accessible
# SCOPE RESOLUTION = (LEGB) Local -> Enclosed -> global -> Built-in

from math import e

def func1():
    print(e)

e = 3
func1()