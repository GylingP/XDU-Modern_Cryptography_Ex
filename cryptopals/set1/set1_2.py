def xor_str_hex(str1,str2):
    hex1_bytes=bytes.fromhex(str1)
    hex2_bytes=bytes.fromhex(str2)
    xor_bytes=bytes(x ^ y for x, y in zip(hex1_bytes, hex2_bytes))
    xor_str = ''.join(['{:02x}'.format(byte) for byte in xor_bytes])
    return xor_str

if __name__=="__main__":
    hex_str1 = "1c0111001f010100061a024b53535009181c"
    hex_str2 = "686974207468652062756c6c277320657965"
    result = xor_str_hex(hex_str1, hex_str2)
    print(result)