import time

start_time = time.time()


def solution(myString):
    #    return list(map(len, myString.split("x")))
    return [len(i) for i in myString.split("x")]


def main():
    myString1 = "oxooxoxxox"
    myString2 = "xabcxdefxghi"

    print(solution(myString1))
    print(solution(myString2))

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
