def solution(common):
    #    common_diff = common[1] - common[0]
    #    common_ratio = common[1] / common[0] if common[0] != 0 else None
    #
    #    if common_diff == common[2] - common[1]:
    #        return common[-1] + common_diff
    #    else:
    #        return common[-1] * common_ratio

    a, b, c = common[:3]

    if b - a == c - b:
        return common[-1] + (b - a)
    else:
        return common[-1] * (b // a)


def main():
    common1 = [1, 2, 3, 4]
    common2 = [2, 4, 8]

    print(solution(common1))
    print(solution(common2))


if __name__ == "__main__":
    main()
