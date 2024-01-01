import gmpy2
import math
import binascii


# 欧几里得算法
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def CRT(items):
    N = 1
    for a, n in items:
        N *= n
        result = 0
    for a, n in items:
        m = N // n
        d, r, s = egcd(n, m)
        if d != 1:
            N = N // n
            continue
        result += a * s * m
    return result % N, N


# 低加密指数e == 3


def Be_3():
    Brange = [7, 11, 15]
    for i in range(3):
        c = int(C[Brange[i]], 16)
        n = int(NN[Brange[i]], 16)
        print("This is frame" + str(i))
        for j in range(20):
            plain = gmpy2.iroot(gmpy2.mpz(c + j * n), 3)
            print("This is test" + str(j))
            print(binascii.a2b_hex(hex(plain[0])[2:]))


def low_e_3():
    ss = [
        {"c": int(C[7], 16), "n": int(NN[7], 16)},
        {"c": int(C[11], 16), "n": int(NN[11], 16)},
        {"c": int(C[15], 16), "n": int(NN[15], 16)},
    ]
    data = []
    for session in ss:
        data = data + [(session["c"], session["n"])]
    x, y = CRT(data)
    #开三次方根
    plaintext7_11_15 = gmpy2.iroot(gmpy2.mpz(x), 3)
    return binascii.a2b_hex(hex(plaintext7_11_15[0])[2:])


def low_e_5():
    ss = [
        {"c": int(C[3], 16), "n": int(NN[3], 16)},
        {"c": int(C[8], 16), "n": int(NN[8], 16)},
        {"c": int(C[12], 16), "n": int(NN[12], 16)},
        {"c": int(C[16], 16), "n": int(NN[16], 16)},
        {"c": int(C[20], 16), "n": int(NN[20], 16)},
    ]
    data = []
    for session in ss:
        data = data + [(session["c"], session["n"])]
    x, y = CRT(data)
    # 直接开五次方根
    plaintext3_8_12_16_20 = gmpy2.iroot(gmpy2.mpz(x), 5)
    return binascii.a2b_hex(hex(plaintext3_8_12_16_20[0])[2:])


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
    plaintext3_8_12_16_20 = low_e_5()
    print(plaintext3_8_12_16_20)
    plaintext7_11_15 = low_e_3()
    print(plaintext7_11_15)  # low_e_3的是无法破解的
