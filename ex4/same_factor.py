import gmpy2
import binascii
import math

if __name__ == "__main__":
    N = []
    C = []
    E = []
    for i in range(21):
        with open("./frame_set/Frame" + str(i), "r") as f:
            tmp = f.read()
            N.append(tmp[0:256])
            E.append(tmp[256:512])
            C.append(tmp[512:768])
    plaintext = []
    index = []
    for i in range(21):
        for j in range(i + 1, 21):
            if int(N[i], 16) == int(N[j], 16):
                continue
            prime = gmpy2.gcd(int(N[i], 16), int(N[j], 16))
            if prime != 1:
                print((N[i], N[j]))
                print((i, j))
                index.append(i)
                index.append(j)
                Pframe = prime
    Qframe1 = int(N[index[0]], 16) // Pframe  # 通过碰撞因数求得p、q
    Qframe18 = int(N[index[1]], 16) // Pframe
    print(Pframe)
    print(Qframe1, Qframe18)

    φframe1 = (Pframe - 1) * (Qframe1 - 1)
    φframe18 = (Pframe - 1) * (Qframe18 - 1)

    d_of_frame1 = gmpy2.invert(int(E[index[0]], 16), φframe1)
    d_of_frame18 = gmpy2.invert(int(E[index[1]], 16), φframe18)

    Pframe1 = gmpy2.powmod(
        int(C[index[0]], 16), d_of_frame1, int(N[index[0]], 16)
    )
    Pframe18 = gmpy2.powmod(
        int(C[index[1]], 16), d_of_frame18, int(N[index[1]], 16)
    )

    PLAIN1 = binascii.a2b_hex(hex(Pframe1)[2:])
    PLAIN18 = binascii.a2b_hex(hex(Pframe18)[2:])

    plaintext.append(PLAIN1)
    plaintext.append(PLAIN18)

    print(plaintext)
