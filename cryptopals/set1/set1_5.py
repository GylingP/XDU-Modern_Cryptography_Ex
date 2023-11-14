def xor_repeated_key_str(plaintext,key):
    plain_bytes=bytes(plaintext,'utf-8')
    key_bytes=bytes(key,'utf-8')
    xor_bytes=bytes(x ^ key_bytes[i%3] for x, i in zip(plain_bytes, range(0,len(plain_bytes))))
    xor_str = ''.join(['{:02x}'.format(byte) for byte in xor_bytes])
    return xor_str

if __name__=="__main__":
    text="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key="ICE"
    result = xor_repeated_key_str(text,key)
    print(result)