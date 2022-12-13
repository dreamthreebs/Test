import numpy as np

# fxprime=3y, fyprime=3x fxyprime=3e^x+3x*e^x 3(e+e)
def func(x,y):
    return 3*x*y*np.exp(x)



x0=1
y0=4
start=1e-7
stop=1e-1
length=10
xcordinate=np.geomspace(start, stop,length)
dp=np.zeros((length,length))

for i,h1 in enumerate(xcordinate):
    for j,h2 in enumerate(xcordinate):
        dp[i,j]=(func(x0+h1, y0+h2)-func(x0+h1, y0-h2)-func(x0-h1, y0+h2)+func(x0-h1, y0-h2))/(4*h1*h2)

