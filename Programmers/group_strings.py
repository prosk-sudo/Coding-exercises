def solution(strArr):
    #    d = {}
    #
    #    for string in strArr:
    #        if len(string) not in d:
    #            d[len(string)] = 1
    #        else:
    #            d[len(string)] += 1
    #
    #    max_key = max(d, key=d.get)
    #    return d[max_key]

    lst = [0] * 31
    for string in strArr:
        lst[len(string)] += 1
    return max(lst)


def main():
    strArr1 = ["a", "bc", "d", "efg", "hi"]

    print(solution(strArr1))


if __name__ == "__main__":
    main()
