def solution(babbling):
    vocab = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for word in vocab:
            if word in babbling[i]:
                babbling[i] = babbling[i].replace(word, " ")
        babbling[i] = babbling[i].replace(" ", "")
    return babbling.count("")


def main():
    babbling1 = ["aya", "yee", "u", "maa", "wyeoo"]
    babbling2 = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]

    print(solution(babbling1))
    print(solution(babbling2))


if __name__ == "__main__":
    main()
