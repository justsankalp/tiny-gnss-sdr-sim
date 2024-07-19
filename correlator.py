from utils import correlate, sample
from prngen import prn
import numpy as np
from matplotlib import pyplot as plt

with open('out.bin', 'rb') as file:
    binary_data = file.read()

signal = list(binary_data)

for i in range(len(signal)):
    if signal[i] == 0:
        signal[i] = -1

def loopcor(list1, sv, sr):
    cs = 0
    ini = 0
    outl = []
    n = int(sr/1000) # 1023
    for i in range(((len(list1)//n)-1)*n):
        c = correlate(list1[i:n+i], sample(prn(sv)[0], sr))
        if c > ini:
            ini = c
            cs = i
        outl.append(c)
    return outl


s1 = prn(1)[0]
s2 = prn(5)[0]
s3 = prn(10)[0]

mod1 = s1 + s1
mod2 = [0]*300 + s2
mod3 = [0]*600 + s3
mod2 += [0]*(len(mod1) - len(mod2))
mod3 += [0]*(len(mod1) - len(mod3))
s = np.array(mod2) + np.array(mod1) + np.array(mod3)

signal = sample(s, 4092000)


plt.plot(loopcor(signal, 5, 4092000))
plt.show()
