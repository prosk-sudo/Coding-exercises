def solution(q, r, code):
#    answer = ''
#    for i in range(len(code)):
#        if i % q == r:
#            answer += code[i]
#    return answer

#    return ''.join(code[i] for i in range(len(code)) if i % q == r)

#    return ''.join(code[i] for i in range(r, len(code), q))

    return code[r::q]

def main():
    q_one, r_one, code_one = 3, 1, "qjnweqgrpirldywt"
    q_two, r_two, code_two = 1, 0, "programmers"

    print(solution(q_one, r_one, code_one))
    print(solution(q_two, r_two, code_two))

if __name__ == "__main__":
    main()
