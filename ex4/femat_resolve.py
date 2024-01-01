import gmpy2
import binascii
import math
import time

def pq(n):
    B = math.factorial(2 ** 14)
    u = 0
    v = 0
    i = 0
    u0 = gmpy2.iroot(n, 2)[0] + 1
    timeStart = time.time()
    while i <= (B - 1):
        u = (u0 + i) * (u0 + i) - n
        if gmpy2.is_square(u):
            v = gmpy2.isqrt(u)
            break
        i = i + 1
        timeEnd = time.time()
        if timeEnd-timeStart>1:
            return 0 #超时
    p = u0 + i + v
    return p


def fermat_resolve():
    ilist = []
    for i in range(10, 16):
        timeStart = time.time()
        N = int(NN[i], 16)
        p = pq(N)
        timeEnd = time.time()
        print(f"i={i},p={p},time={timeEnd-timeStart}")
        if p != 0:
            ilist.append(i)
    print(f"Fermat攻击尝试结束。{ilist}是可以进行攻击的。")

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
    fermat_resolve()

    #底下的代码是根据上面解出的结果再写的
    p = 9686924917554805418937638872796017160525664579857640590160320300805115443578184985934338583303180178582009591634321755204008394655858254980766008932978699
    n = int(NN[10], 16)
    c = int(C[10], 16)
    e = int(E[10], 16)
    q = n // p
    φframe10 = (p - 1) * (q - 1)
    d = gmpy2.invert(e, φframe10)
    m = gmpy2.powmod(c, d, n)
    Plain = binascii.a2b_hex(hex(m)[2:])
    print(Plain)
