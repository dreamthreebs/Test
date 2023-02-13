import numpy as np
def kJy2muK(kJy,freq):
    h=6.626e-34
    k=1.38062852e-23
    c=3e8
    return h*freq/(k*np.log((2*h*freq**3)/(c**2*kJy*1.25664e-22)))

print(kJy2muK(0.78, 5.45e11))

print(kJy2muK(0.72, 8.57e11))


