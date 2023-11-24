from base64 import b64decode
from Crypto import Random
from Crypto.Cipher import AES
from set2_11 import AES_ECB_encrypt
from set1_8 import get_score_ecb

def is_pkcs7_padded(binary_data):
    padding = binary_data[-binary_data[-1]:]
    return all(padding[b] == len(padding) for b in range(0, len(padding)))

def pkcs7_unpad(data):
    if len(data) == 0:
        raise Exception("The input data must contain at least one byte")
    if not is_pkcs7_padded(data):
        return data
    padding_len = data[len(data) - 1]
    return data[:-padding_len]

class ECBOracle:
    def __init__(self, secret_padding):
        self._key = Random.new().read(AES.key_size[0])
        self._secret_padding = secret_padding
    def encrypt(self, data):
        return AES_ECB_encrypt(data + self._secret_padding, self._key)

def find_block_length(encryption_oracle):
    my_text = b''
    ciphertext = encryption_oracle.encrypt(my_text)
    initial_len = len(ciphertext)
    new_len = initial_len

    while new_len == initial_len:
        my_text += b'A'
        ciphertext = encryption_oracle.encrypt(my_text)
        new_len = len(ciphertext)

    return new_len - initial_len


def get_next_byte(block_length, curr_decrypted_message, encryption_oracle):
    length_to_use = (block_length - (1 + len(curr_decrypted_message))) % block_length
    prefix = b'A' * length_to_use
    cracking_length = length_to_use + len(curr_decrypted_message) + 1
    real_ciphertext = encryption_oracle.encrypt(prefix)
    for i in range(256):
        fake_ciphertext = encryption_oracle.encrypt(prefix + curr_decrypted_message + bytes([i]))
        if fake_ciphertext[:cracking_length] == real_ciphertext[:cracking_length]:
            return bytes([i])
    return b''


def byte_at_a_time_ecb_decryption_simple(encryption_oracle):
    block_length = find_block_length(encryption_oracle)
    ciphertext = encryption_oracle.encrypt(bytes([0] * 64))
    assert get_score_ecb(ciphertext) > 0
    mysterious_text_length = len(encryption_oracle.encrypt(b''))
    secret_padding = b''
    for i in range(mysterious_text_length):
        secret_padding += get_next_byte(block_length, secret_padding, encryption_oracle)
    return secret_padding

if __name__ == '__main__':
    secret_padding = b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGF"
                               "pciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IH"
                               "RvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    oracle = ECBOracle(secret_padding)
    discovered_secret_padding = byte_at_a_time_ecb_decryption_simple(oracle)
    print(pkcs7_unpad(discovered_secret_padding))