from set2_10 import AES_pkcs7_unpad

if __name__ == '__main__':
    AES_pkcs7_unpad(b'ICE ICE BABY\x04\x04\x04\x04')
    #AES_pkcs7_unpad(b'ICE ICE BABY\x05\x05\x05\x05')
    #AES_pkcs7_unpad(b'ICE ICE BABY\x01\x02\x03\x04')
    #AES_pkcs7_unpad(b'ICE ICE BABY')