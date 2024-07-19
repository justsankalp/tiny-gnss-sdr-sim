def xor(a, b):
    if a == b:
        return -1
    else:
        return 1

def pad(list):
    n = len(list)
    out = [0]*(3*n-3)
    out[n-1:2*n-2] = list
    return out

def correlate(list1, list2):
    sum = 0
    for i in range(len(list1)):
            sum += list1[i] * list2[i]
    return sum

def sample(signal, sr):
    spc = int(sr/1023000)
    out = [0]*len(signal)*spc
    outs = []
    for i in range(len(signal)):
        out[(i*spc):((i*spc)+spc)] = [signal[i]]*spc
    return out
