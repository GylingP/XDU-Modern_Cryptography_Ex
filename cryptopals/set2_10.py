from Crypto.Cipher import AES
import base64
from set2_9 import block_padding

def AES_pkcs7_pad(plaintext):
    plaintext_len=len(plaintext)
    if plaintext_len%AES.block_size==0:
        return block_padding(plaintext,plaintext_len+AES.block_size)
    else :
        return block_padding(plaintext,plaintext_len+AES.block_size-plaintext_len%AES.block_size)

def AES_CBC_encrypt(plaintext,key,iv):
    aes_cipher=AES.new(key,AES.MODE_ECB)
    plaintext_padding=AES_pkcs7_pad(plaintext)
    plaintext_block=[plaintext_padding[i*AES.block_size:(i+1)*AES.block_size] for i in range(len(plaintext_padding)//AES.block_size)]
    ciphertext_block=[iv]
    for i in range(len(plaintext_block)):
        _xor_bytes=bytes(x ^ y for x,y in zip(plaintext_block[i],ciphertext_block[i]))
        block=aes_cipher.encrypt(_xor_bytes)
        ciphertext_block.append(block)
    return b"".join(ciphertext_block)

def AES_pkcs7_unpad(plaintext):
    padding_len=int(plaintext[-1])
    for i in range(padding_len):
        if plaintext[-i-1]!=plaintext[-1]:
            raise ValueError()
    return plaintext[:-padding_len]

def AES_CBC_decrypt(ciphertext,key):
    aes_cipher=AES.new(key,AES.MODE_ECB)
    ciphertext_block=[ciphertext[i*AES.block_size:(i+1)*AES.block_size] for i in range(len(ciphertext)//AES.block_size)]
    plaintext_block=[]
    for i in range(1,len(ciphertext_block)):
        _decrypt_bytes=aes_cipher.decrypt(ciphertext_block[i])
        block=bytes(x ^ y for x,y in zip(_decrypt_bytes,ciphertext_block[i-1]))
        plaintext_block.append(block)
    plaintext_padding=b"".join(plaintext_block)
    return AES_pkcs7_unpad(plaintext_padding)

if __name__=="__main__":
    with open('10.txt') as f:
        problem=f.read()
    ciphertext_base64=bytes(problem,'utf-8')
    ciphertext_no_iv=base64.b64decode(ciphertext_base64)
    iv=b'\x00'*AES.block_size
    ciphertext=iv+ciphertext_no_iv
    key=b'YELLOW SUBMARINE'
    plaintext=AES_CBC_decrypt(ciphertext,key)
    print(bytes.decode(plaintext,'utf-8'))