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

def count_unconcealed(e,mod):
	result = 0
	for m in range(mod):
		if fast_mod_exp(m, e, mod) == m:
			result += 1
	return result

p=1009
q=3643
n=p*q
phi=(p-1)*(q-1)
infinity=10**10

p_unconcealed_list=[count_unconcealed(e,p) if e % 2 != 0 and gcd(e,p-1)==1 else infinity for e in range(p-1) ]
q_unconcealed_list=[count_unconcealed(e,q) if e % 2 != 0 and gcd(e,q-1)==1 else infinity for e in range(q-1) ]
min_unconcealed_p = min(p_unconcealed_list)
min_unconcealed_q = min(q_unconcealed_list)
ans = sum(e for e in range(phi) if p_unconcealed_list[e % (p - 1)] == min_unconcealed_p and q_unconcealed_list[e % (q - 1)] == min_unconcealed_q)

print(ans)
 