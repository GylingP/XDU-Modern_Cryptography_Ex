from set1_3 import score_plaintext
import math
import base64

def hamming_distance(bytes1,bytes2):
    distance=sum(bin(x^y).count('1') for x,y in zip(bytes1,bytes2))
    return distance

def make_partition(ciphertext,keysize):
    partition=[bytes(ciphertext[i*keysize:(i+1)*keysize]) for i in range(0,math.floor(len(ciphertext)/keysize))]
    return partition

def get_hamming_score(ciphertext,keysize):
    partition=make_partition(ciphertext,keysize)
    hamming_score_sum=sum(hamming_distance(partition[i],partition[i+1])/keysize for i in range(0,len(partition)-1))
    hamming_score=hamming_score_sum/((len(partition)-1))
    return hamming_score

def guess_key_len(ciphertext):
    scores_list=[get_hamming_score(ciphertext,keysize) for keysize in range(1,40)]
    best_score=min(scores_list)
    guess_len=scores_list.index(best_score)+1
    return guess_len

def xor_repeated_key_bytes(text,key):
    xor_bytes=bytes(x ^ key[i%len(key)] for x, i in zip(text, range(0,len(text))))
    return xor_bytes

def find_xor_key(ciphertext):
    best_key = 0
    best_score = 0
    for key in range(256):
        current_decryption = bytes(x^key for x in ciphertext)
        current_score = score_plaintext(current_decryption.decode('utf-8',errors='ignore'))
        if current_score > best_score:
            best_key = key
            best_score = current_score
    return best_key  

if __name__ == "__main__":
    with open("6.txt") as f:
        problem=f.read()
    ciphertext=bytes(problem,'utf-8')
    ciphertext=base64.b64decode(ciphertext)
    keysize=guess_key_len(ciphertext)
    partition=make_partition(ciphertext,keysize)
    same_position_list=[]
    for i in range(keysize):
        same_position_list.append(bytes(b[i] for b in partition))
    best_key=bytes(find_xor_key(c) for c in same_position_list)
    print("=======The key is:========")
    print(best_key)
    plaintext=xor_repeated_key_bytes(ciphertext,best_key)
    print("========The plaintext is (utf-8) : ========")
    print(plaintext.decode('utf-8'))
    