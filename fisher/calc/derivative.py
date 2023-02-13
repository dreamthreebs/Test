import numpy as np
def ombh2_prime():
    pass

def omch2_prime():
    pass

def create_array():
    return np.ones(100)

if __name__=='__main__':
    arr=create_array()
    np.save('../data/derivative/derivative.npy', arr)
