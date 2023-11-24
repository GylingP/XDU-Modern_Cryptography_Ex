from set2_10 import AES_pkcs7_unpad
from set2_11 import AES_ECB_encrypt
from Crypto import Random
from Crypto.Cipher import AES

def aes_ecb_decrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return AES_pkcs7_unpad(cipher.decrypt(data))


class ECBOracle:
    def __init__(self):
        self._key = Random.new().read(AES.key_size[0])
    def encrypt(self, email):
        encoded = profile_for(email)
        bytes_to_encrypt = encoded.encode()
        return AES_ECB_encrypt(bytes_to_encrypt, self._key)
    def decrypt(self, ciphertext):
        return aes_ecb_decrypt(ciphertext, self._key)

def kv_encode(dict_object):
    encoded_text = ''
    for item in dict_object.items():
        encoded_text += item[0] + '=' + str(item[1]) + '&'
    return encoded_text[:-1]

def kv_parse(cookie):
    pairs = cookie.split('&')
    parsed_data = {}
    for pair in pairs:
        key, value = pair.split('=')
        parsed_data[key] = value
    return parsed_data

def profile_for(email):
    email = email.replace('&', '').replace('=', '')     
    return f"email={email}&uid=10&role=user"


def ecb_cut_and_paste(encryption_oracle):
    prefix_len = AES.block_size - len("email=")
    suffix_len = AES.block_size - len("admin")
    email1 = 'x' * prefix_len + "admin" + (chr(suffix_len) * suffix_len)
    encrypted1 = encryption_oracle.encrypt(email1)
    email2 = "attack@em.com"
    encrypted2 = encryption_oracle.encrypt(email2)
    forced = encrypted2[:32] + encrypted1[16:32]
    return forced


if __name__=="__main__":
    oracle = ECBOracle()
    forced_ciphertext = ecb_cut_and_paste(oracle)
    decrypted = oracle.decrypt(forced_ciphertext)
    parsed = kv_parse(decrypted.decode())
    print (parsed['role'])
