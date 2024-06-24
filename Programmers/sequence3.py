def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        if int(intStr[s:s+l]) > k:
            answer.append(int(intStr[s:s+l]))
    return answer

def main():
    intStrs_one = ["0123456789","9876543210","9999999999999"]
    k_one = 50000
    s_one = 5
    l_one = 5

    print(solution(intStrs_one, k_one, s_one, l_one))       # [56789, 99999]

if __name__ == "__main__":
    main()
