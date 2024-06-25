import time
start_time = time.time()

def solution(my_string, is_suffix):
    #    return 1 if is_suffix in sorted(my_string[i:] for i in range(len(my_string))) else 0

    #    if my_string[-len(is_suffix):] == is_suffix:
    #        return 1
    #    return 0

    return int(my_string.endswith(is_suffix))

def main():
    my_string_one = "banana"
    is_suffix_one = "ana"
    is_suffix_two = "nan"
    is_suffix_three = "wxyz"
    is_suffix_four = "abanana"

    print(solution(my_string_one, is_suffix_one))
    print(solution(my_string_one, is_suffix_two))
    print(solution(my_string_one, is_suffix_three))
    print(solution(my_string_one, is_suffix_four))

    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == "__main__":
    main()
