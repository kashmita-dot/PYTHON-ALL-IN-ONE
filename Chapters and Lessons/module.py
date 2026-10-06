# MODULE = A file containing Python code that can be imported into another Python file 
# useful to breakup a large program reusable separate files

import math
print(math.pi)

import math as m
print(m.pi)

from math import pi
from math import e
print(pi)
print(e)

from math import e
import math
a, b, c, d = 1, 2, 3, 4
print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)

import module_example

result = module_example.pi
print(result)
result = module_example.square(3)
print(result)
result = module_example.cube(3)
print(result)
result = module_example.circumference(5)
print(result)