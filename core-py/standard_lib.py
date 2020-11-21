
from math import factorial as fac

n = 100
k = 2

# single /
x1 = fac(n) / (fac(k) * fac(n-k))
# double //
x2 = fac(n) // (fac(k) * fac(n-k))

print(str(x1) + "\r", x2)






#