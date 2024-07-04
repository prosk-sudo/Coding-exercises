def solution(nums):
    answer = 0
    is_prime = True

    # something

    total = 1

    for i in range(2, int(total)):
        if int(total) % i == 0:
            is_prime = False
            break

    if is_prime:
        answer += 1

    return answer


def main():
    nums1 = [1, 2, 3, 4]
    nums2 = [1, 2, 7, 6, 4]

    print(solution(nums1))
    print(solution(nums2))


if __name__ == "__main__":
    main()
