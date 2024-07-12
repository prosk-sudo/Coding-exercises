def replace_exclamation(st):
    for i in range(len(st)):
        if st[i].lower() in "aeiou":
            st = st[:i] + "!" + st[i + 1 :]
    return st


def main():
    print(replace_exclamation("Hi!"))
    print(replace_exclamation("!Hi! Hi!"))
    print(replace_exclamation("aeiou"))
    print(replace_exclamation("ABCDE"))


if __name__ == "__main__":
    main()
