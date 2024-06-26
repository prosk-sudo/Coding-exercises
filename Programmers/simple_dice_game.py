import time
start_time = time.time()

def solution(a, b):
        #    if a % 2 == 0 and b % 2 == 0:
        #        return abs(a - b)
        #    elif a % 2 == 1 and b % 2 == 1:
        #        return a**2 + b**2
        #    else:
        #        return 2 * (a + b)

    if a % 2 == b % 2:
        if a % 2 == 0:
            return abs(a - b)
        else:
            return a**2 + b**2
    else:
        return 2 * (a + b)

def main():
    a_one, b_one = 3, 5
    a_two, b_two = 6, 1
    a_three, b_three = 2, 4

    print(solution(a_one, b_one))
    print(solution(a_two, b_two))
    print(solution(a_three, b_three))
    
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
