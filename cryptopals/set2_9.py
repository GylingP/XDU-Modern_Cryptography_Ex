def block_padding(ori_bytes,target_len):
    padding_len=target_len-len(ori_bytes)
    if padding_len<0 or padding_len>256:
        raise ValueError()
    res_bytes=ori_bytes+bytes([padding_len])*padding_len
    return res_bytes

if __name__=="__main__":
    ori_bytes=b'YELLOW SUBMARINE'
    print(block_padding(ori_bytes,20))