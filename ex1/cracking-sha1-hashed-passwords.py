#coding:utf-8
import hashlib
import itertools
import datetime
starttime = datetime.datetime.now()
hash1="67ae1a64661ac8b4494666f58c4822408dd0a3e4"
str1="QqWw%58(=0Ii*+nN"
str2=[['Q', 'q'],[ 'W', 'w'],[ '%', '5'], ['8', '('],[ '=', '0'], ['I', 'i'], ['*', '+'], ['n', 'N']]
def sha_encrypt(str):
    str=str.encode('utf-8')
    sha = hashlib.sha1(str)
    encrypts = sha.hexdigest()
    return encrypts

str3 = itertools.product(*str2)

for s in str3:
    newS = "".join(s)
    for i in itertools.permutations(newS, 8):
        str4 = sha_encrypt("".join(i))
        if str4 == hash1:
            print("The matching string is: {}".format("".join(i)))
            endtime = datetime.datetime.now()
            print("The running time is: {} seconds".format((endtime - starttime).seconds))
            break
    else:
        continue
    break