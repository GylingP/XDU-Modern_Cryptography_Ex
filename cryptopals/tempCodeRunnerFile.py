def fast_mod_exp(base,exp,mod):
    result=1
    bi_list=[]
    while exp>0:
        bi_list.append(exp%2)
        exp//=2    
    for i in reversed(bi_list) :
        result=result ** 2 % mod
        if i==1:
            result=result * base % mod
    return result