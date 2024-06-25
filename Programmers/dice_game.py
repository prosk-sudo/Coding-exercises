import time
start_time = time.time()

def solution(a, b, c, d):
    nums_set = {a, b, c, d}
    count = {}

    for num in [a, b, c, d]:
        count[num] = count.get(num, 0) + 1

    if len(nums_set) == 4:
        return min(nums_set)

    elif len(nums_set) == 3:
        p = [i for i in count if count[i] == 2][0]
        q, r = [i for i in nums_set if i != p]
        return q * r

    elif len(nums_set) == 2:
        if 2 in count.values():
            p, q = count.keys()
            return (p + q) * abs(p - q)

        else:
            p = [i for i in count if count[i] == 3][0]
            q = [i for i in count if count[i] == 1][0]
            return (10 * p + q) ** 2
    else:
        return 1111 * a

def main():
    a_1, b_1, c_1, d_1 = 2, 2, 2, 2
    a_2, b_2, c_2, d_2 = 4, 1, 4, 4
    a_3, b_3, c_3, d_3 = 6, 3, 3, 6
    a_4, b_4, c_4, d_4 = 2, 5, 2, 6
    a_5, b_5, c_5, d_5 = 6, 4, 2, 5

    print(solution(a_1, b_1, c_1, d_1))
    print(solution(a_2, b_2, c_2, d_2))
    print(solution(a_3, b_3, c_3, d_3))
    print(solution(a_4, b_4, c_4, d_4))
    print(solution(a_5, b_5, c_5, d_5))

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
