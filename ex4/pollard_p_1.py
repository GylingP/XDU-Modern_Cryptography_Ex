import math
import gmpy2
import binascii

def pollardPMinus1(n):
    B = 2 ** 20
    a = 2
    for i in range(2*2, (B + 1)*2 , 2):
        a = pow(a, i, n)
        d = gmpy2.gcd(a - 1, n)
        if (d >= 2) and (d <= (n - 1)):
            q = n // d
            n = q * d
    return d

if __name__ == "__main__":
    NN = []
    C = []
    E = []
    for i in range(21):
        with open("./frame_set/Frame" + str(i), "r") as f:
            tmp = f.read()
            NN.append(tmp[0:256])
            E.append(tmp[256:512])
            C.append(tmp[512:768])
    index_list = [2, 6, 19]
    plainTextList = []
    for i in range(3):
        N = int(NN[index_list[i]], 16)
        c = int(C[index_list[i]], 16)
        e = int(E[index_list[i]], 16)
        p = pollardPMinus1(N)
        print("p of " + str(index_list[i]) + " is : " + str(p))
        q = N // p
        φofFrame = (p - 1) * (q - 1)
        d = gmpy2.invert(e, φofFrame)
        m = gmpy2.powmod(c, d, N)
        plainTextList.append(binascii.a2b_hex(hex(m)[2:]))
    print(plainTextList)
    print("Pollard finished!")
