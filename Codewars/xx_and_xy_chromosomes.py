def chromosome_check(chromosome):
    if chromosome == "XY":
        return "Congratulations! You're going to have a son."
    else:
        return "Congratulations! You're going to have a daughter."


def main():
    print(chromosome_check("XY"))
    print(chromosome_check("XX"))


if __name__ == "__main__":
    main()
