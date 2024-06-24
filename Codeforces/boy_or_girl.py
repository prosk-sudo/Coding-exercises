def main():
    username = input().split()

    for i in range(len(username)):
        username = set(username[i])

    if len(username) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

    return "CHAT WITH HER!" if len(username) % 2 == 0 else "IGNORE HIM!"


if __name__ == "__main__":
    main()
