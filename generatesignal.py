from utils import correlate, sample
from prngen import prn
import struct
import numpy as np
from matplotlib import pyplot as plt

def receive(signal, sr):
    spc = int(sr/1023000)
    out = [0]*len(signal)*spc
    outs = []
    for i in range(len(signal)):
        out[(i*spc):((i*spc)+spc)] = [signal[i]]*spc
    return out

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
# s2 = prn(5)[0]
# s3 = prn(10)[0]
# # print(s1)
# mod1 = s1 + s1
# mod2 = [0]*300 + s2
# mod3 = [0]*600 + s3
# mod2 += [0]*(len(mod1) - len(mod2))
# mod3 += [0]*(len(mod1) - len(mod3))
# s = np.array(mod2) + np.array(mod1) + np.array(mod3)

sl = receive(s1, 4092000)
# for i in range(len(sl)):
#     if sl[i] == -1:
#         sl[i] = 0
# # print(sl)
#
# fins = bytearray(sl)
# with open('out.bin', 'wb') as file:
#     file.write(fins)

# print(f"Binary saved.")
# #
# # for _ in range(1,33):
# #     plt.plot(loopcor(sl, _, 4092000))
#
x = loopcor(sl, 1, 4092000)
print(x)
# plt.plot(loopcor(sl, 1, 4092000))
# plt.show()
