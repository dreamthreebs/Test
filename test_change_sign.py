import numpy as np

a = np.array([-1, 1, 2, -3, 4, -5])
sign_change = np.where(np.diff(np.sign(a)))[0]
print(sign_change)

