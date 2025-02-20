import numpy as np
a = np.zeros((2,4), dtype=int)

print(a)

a[1][3] = 1
print(a)

a[1][-2] = 5
print(a)
print (f"{a.size=}" )

