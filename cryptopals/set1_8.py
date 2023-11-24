from Crypto.Cipher.AES import block_size

def get_score_ecb(ciphertext):
    block=[ciphertext[i*block_size:(i+1)*block_size] for i in range(len(ciphertext)//block_size)]
    return len(block)-len(set(block))