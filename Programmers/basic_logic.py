def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)

def main():
    x1_1, x2_1, x3_1, x4_1 = False, True, True, True
    x1_2, x2_2, x3_2, x4_2 = True, False, False, False

    print(solution(x1_1, x2_1, x3_1, x4_1))
    print(solution(x1_2, x2_2, x3_2, x4_2))

if __name__ == "__main__":
    main()
