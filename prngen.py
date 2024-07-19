from utils import xor
from cacode import Svidtap

def polynomialg1(bits):
    xored = xor(bits[2], bits[9])
    outbit = bits[9]
    bits[1:len(bits)] = bits[0:len(bits)-1]
    bits[0] = xored
    return bits, outbit

def polynomialg2(bits, sattelitecode):
    # h = [2,6]
    agenda = [6,8,9,10]
    zeroth = xor(bits[1],bits[2])
    outbit = xor(bits[sattelitecode[0]-1],bits[sattelitecode[1]-1])
    for i in range(len(agenda)):
        zeroth = xor(zeroth, bits[agenda[i]-1])
    bits[1:10] = bits[0:len(bits)-1]
    bits[0] = zeroth
    return bits, outbit

def prn(satelliteno):
    list = [1,1,1,1,1,1,1,1,1,1]
    out = [0]*1023
    stringout = ""
    listy = list.copy()
    for i in range(1023):
        list, term = polynomialg1(list)
        # print(f"list: {list}")
        satelliteg2 = Svidtap(satelliteno).g2
        listy, outer = polynomialg2(listy, satelliteg2)
        # print(f"listy: {listy}")
        # print(f"term = {term}, outer = {outer}, iteration = {i}")
        out[i] = xor(term, outer)
        stringout += str(out[i])
        # print(f"xor: {out[i]}")
    return out, stringout


def main():
    print(prn(1)[0])
    # print(polynomialg2([1,1,0,1,0,1,0,1,0,1], Svidtap(1).g2))
if __name__ == "__main__":
    main()
