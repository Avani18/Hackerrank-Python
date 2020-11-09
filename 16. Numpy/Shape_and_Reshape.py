import numpy as np

ar = list(map(int, input().split()))
npar = np.array(ar)
print (np.reshape(npar,(3,3)))
