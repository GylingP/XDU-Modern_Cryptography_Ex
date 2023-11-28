def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fast_mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

p=1009
q=3643
n=p*q
phi=(p-1)*(q-1)

e_list=[]
for i in range(phi):
    if(i%2!=0 and gcd(i,phi)==1):
        e_list.append(i)
e_dict={}
for i in e_list:
    count=1
    for j in range(2,n):
        if(fast_mod_exp(j,i,p)==j and fast_mod_exp(j,i,q)==j):
            count+=1
    e_dict.update({str(i):count})
print(e_dict)