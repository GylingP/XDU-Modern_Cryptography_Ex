import gmpy2
import binascii
import math


# 欧几里得算法
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)



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
    # 使用公共模数攻击的方法还原出Frame0和Frame4
    # Frame0: My secre
    # Frame4: My secre
    i1 = 0
    i2 = 0
    for i in range(21):
        for j in range(i + 1, 21):
            if N[i] == N[j]:
                print("寻找到公共模数:" + str((N[i], N[j])))
                i1, i2 = i, j
    e1 = int(E[i1], 16)
    e2 = int(E[i2], 16)
    n = int(N[i1], 16)
    c1 = int(C[i1], 16)
    c2 = int(C[i2], 16)
    s = egcd(e1, e2)
    s1 = s[1]
    s2 = s[2]
    # 求模反元素
    if s1 < 0:
        s1 = -s1
        c1 = gmpy2.invert(c1, n)
    elif s2 < 0:
        s2 = -s2
        c2 = gmpy2.invert(c2, n)

    m = pow(c1, s1, n) * pow(c2, s2, n) % n

    print(m)
    print(binascii.a2b_hex(hex(m)[2:]))
    plaintext0_and_4 = binascii.a2b_hex(hex(m)[2:])
    print(plaintext0_and_4)
