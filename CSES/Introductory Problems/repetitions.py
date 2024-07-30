def main():
    user_input = input()
    count = 1
    previous = user_input[0]
    occurence_list = []

    for char in user_input[1:]:
        if previous == char:
            count += 1
        else:
            occurence_list.append(count)
            count = 1
        previous = char
    occurence_list.append(count)
    print(max(occurence_list))

if __name__ == "__main__":
    main()
