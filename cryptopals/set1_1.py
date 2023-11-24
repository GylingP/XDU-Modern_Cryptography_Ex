import base64

def hex_sto_base64(str_hex):
    bytes_hex = bytes.fromhex(str_hex)
    str_base64 = base64.b64encode(bytes_hex).decode('utf-8')
    return str_base64


if __name__=="__main__":
    str_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hex_sto_base64(str_hex))