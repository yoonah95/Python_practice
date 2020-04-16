from decimal import *
import math,cmath
d = Decimal ('123.456789012345')
print(math.sqrt(d))
print(cmath.sqrt(-d))
print(d.sqrt())
print(d.quantize(Decimal('.01'),rounding=ROUND_DOWN)
