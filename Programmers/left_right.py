def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i] == "r":
            return str_list[i+1:]
        elif str_list[i] == "l":
            return str_list[:i]
    return []

def main():
    str_list_one = ["u", "u", "l", "r"]
    str_list_two = ["l"]

    print(solution(str_list_one))
    print(solution(str_list_two))

if __name__ == "__main__":
    main()
