def xor_decrypt(hex_str, key):
    bytes_data = bytes.fromhex(hex_str)
    decrypted_bytes = bytes(x ^ key for x in bytes_data)
    decrypted_text = decrypted_bytes.decode('utf-8', errors='ignore')
    return decrypted_text

def score_plaintext(plaintext):
    letter_frequency ={
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
    }
    plaintext_lower = plaintext.lower()
    score = sum(letter_frequency.get(char, 0) for char in plaintext_lower)
    return score

def find_xor_key_str(hex_str):
    best_key = 0
    best_score = 0
    decrypted_text = ""
    for key in range(256):
        current_decryption = xor_decrypt(hex_str, key)
        current_score = score_plaintext(current_decryption)
        if current_score > best_score:
            best_key = key
            best_score = current_score
            decrypted_text = current_decryption
    return best_key, decrypted_text

if __name__=="__main__":
    hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    key, decrypted_message = find_xor_key_str(hex_str)
    print("Key:", key)
    print("Decrypted Message:", decrypted_message)
