import time
start_time = time.time()

def solution(l, r):
    num_list = []
    answer = []

    for i in range(1, 64):
        num_list.append(5 * int(bin(i)[2:]))

    for v in num_list:
        if v > r:
            break
        elif l <= v <= r:
            answer.append(v)

    if not answer:
        return [-1]

    return answer

def main():
    l_first = 5
    r_first = 555

    print(solution(l_first, r_first))

    l_second = 10
    r_second = 20

    print(solution(l_second, r_second))

if __name__ == "__main__":
    main()

print("--- %s seconds ---" % (time.time() - start_time))
