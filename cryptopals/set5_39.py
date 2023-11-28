from Crypto.Util.number import getPrime

def ext_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = ext_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def invmod(e, et):
    gcd,x,y = ext_gcd(e, et)
    if gcd != 1:
        return None
    else:
        return x+et

def fast_mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

class RSA_e_3:
    def __init__(self,n_len):
        self.n_len=n_len
        self.p_len=(n_len+1)//2
        self.q_len=self.p_len
        p,q,n=(0,0,0)
        while n.bit_length()!=n_len or ext_gcd(3,(p-1)*(q-1))[0]!=1 or p==q:
            p=getPrime(self.p_len)
            q=getPrime(self.q_len)
            n=p*q
        else:
            self.p=p
            self.q=q
            self.n=n
        self.et=(self.p-1)*(self.q-1)
        self.e=3
        self.d=invmod(self.e,self.et)
        self.public_key=(self.n,self.e)
        self.private_key=(self.n,self.d)
    def encrypt(self,plainnum):
        return fast_mod_exp(plainnum,self.e,self.n)
    def decrypt(self,ciphernum):
        return fast_mod_exp(ciphernum,self.d,self.n)
    
if __name__=="__main__":
    rsa_cipher=RSA_e_3(2048)
    print("========choose p,q========")
    print("p:",rsa_cipher.p)
    print("q:",rsa_cipher.q)
    print("========calculate n========")
    print(rsa_cipher.n)
    print("========public key========")
    print(rsa_cipher.public_key)
    print("========plaintext========")
    print(42)
    print("========ciphertext========")
    ciphertext=rsa_cipher.encrypt(42)
    print(ciphertext)
    print("========private key========")
    print(rsa_cipher.private_key)
    print("========solve plaintext========")
    plaintext_solved=rsa_cipher.decrypt(ciphertext%rsa_cipher.n)
    print(plaintext_solved)
    print("========whether the plaintext solved is equal to the true plaintext========")
    print(plaintext_solved==42)
        
        
