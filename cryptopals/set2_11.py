import random
from Crypto.Cipher import AES
from set2_10 import AES_pkcs7_pad,AES_CBC_encrypt
from set1_8 import get_score_ecb

def random_key_16():
    return bytes([random.randint(0,255)]*16)

def AES_ECB_encrypt(plaintext,key):
    aes_cipher=AES.new(key,AES.MODE_ECB)
    plaintext_padding=AES_pkcs7_pad(plaintext)
    plaintext_block=[plaintext_padding[i*AES.block_size:(i+1)*AES.block_size] for i in range(len(plaintext_padding)//AES.block_size)]
    ciphertext_block=[aes_cipher.encrypt(b) for b in plaintext_block]
    return b''.join(ciphertext_block)

def encryption_oracle(plaintext_raw):
    key=random_key_16()
    pre_bytes=bytes([random.randint(0,255)]*random.randint(5,10))
    next_bytes=bytes([random.randint(0,255)]*random.randint(5,10))
    plaintext=pre_bytes+plaintext_raw+next_bytes
    iv=bytes([random.randint(0,255)]*AES.block_size)#compute no matter whether we choose CBC mode later to resist SCA
    coin=random.random()
    if coin<0.5:
        return 'ecb',AES_ECB_encrypt(plaintext,key)
    else:
        return 'cbc',AES_CBC_encrypt(plaintext,key,iv)

def detect_oracle(ciphertext):
    score=get_score_ecb(ciphertext)
    if score>0:
        print("detect: encrypted with ECB mode")
        return 'ecb'
    else:
        print("detect: encrypted with CBC mode")
        return 'cbc'

if __name__=="__main__":
    acc=0
    for i in range(10):
        print("================")
        plaintext=bytes([0]*128)
        padding,ciphertext=encryption_oracle(plaintext)
        print("encryption mode: "+padding)
        detection=detect_oracle(ciphertext)
        if padding==detection:
            acc+=1
    print("========statistics========")
    print("accuracy: "+str(acc/10))
