from set1_3 import xor_decrypt,score_plaintext,find_xor_key_str

def get_best_score(hex_str):
    best_score = 0
    for key in range(256):
        current_decryption = xor_decrypt(hex_str, key)
        current_score = score_plaintext(current_decryption)
        if current_score > best_score:
            best_score = current_score
    return best_score  

if __name__=="__main__":
    with open('4.txt') as f:
        problem=f.read()
        problem_list=problem.split()
    scores_list=[get_best_score(m) for m in problem_list]
    best_index=scores_list.index(max(scores_list))
    print(problem_list[best_index])
    print(find_xor_key_str(problem_list[best_index]))
