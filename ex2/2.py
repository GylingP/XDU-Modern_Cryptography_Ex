from Crypto.Cipher import AES
import base64
from hashlib import sha1

def calculate_check_digit(data, weights):
    checksum = 0
    for i in range(len(data)):
        checksum += data[i] * weights[i]
        checksum %= 10
    return checksum

def calculate_sha1_hash(data):
    return sha1(data.encode()).hexdigest()

def generate_key_from_seed(seed):
    constant = '00000001'
    concatenated_data = seed + constant
    return sha1(bytes.fromhex(concatenated_data)).hexdigest()

def apply_odd_parity(ka):
    k = []
    binary_representation = bin(int(ka, 16))[2:]
    for i in range(0, len(binary_representation), 8):
        parity_bit = '1' if binary_representation[i:i+7].count('1') % 2 == 0 else '0'
        k.append(binary_representation[i:i+7] + parity_bit)
    return hex(int(''.join(k), 2))[2:]

def decrypt_aes_cbc(ciphertext, key):
    cipher = AES.new(bytes.fromhex(key), AES.MODE_CBC, bytes.fromhex('0'*32))
    return cipher.decrypt(ciphertext).decode()

if __name__ == "__main__":
    weights_a = [7, 3, 1, 7, 3, 1]
    data_a = [1, 1, 1, 1, 1, 6]
    checksum_a = calculate_check_digit(data_a, weights_a)

    passport_data = '12345678<8<<<1110182<111116'+str(checksum_a)+'<<<<<<<<<<<<<<<4'
    passport_number = passport_data[:10]
    birth_date = passport_data[13:20]
    arrival_date = passport_data[21:28]
    mrz_data = passport_number + birth_date + arrival_date
    hash_mrz = calculate_sha1_hash(mrz_data)

    key_seed = hash_mrz[:32]
    generated_key_hash = generate_key_from_seed(key_seed)

    ka_part = apply_odd_parity(generated_key_hash[:16])
    kb_part = apply_odd_parity(generated_key_hash[16:32])
    final_key = ka_part + kb_part

    cipher_text = '9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI'
    cipher_text_decoded = base64.b64decode(cipher_text)

    decrypted_result = decrypt_aes_cbc(cipher_text_decoded, final_key)
    print(decrypted_result)
