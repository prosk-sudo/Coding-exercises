def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


def main():
    print(is_anagram("foefet", "toffee"))
    print(is_anagram("Buckethead", "DeathCubeK"))
    print(is_anagram("Twoo", "WooT"))
    print(is_anagram("dumble", "bumble"))
    print(is_anagram("ound", "round"))
    print(is_anagram("apple", "pale"))


if __name__ == "__main__":
    main()
