def solution(number):
    return int(number) % 9

def main():
    number1, number2 = "123", "78720646226947352489"

    print(solution(number1))
    print(solution(number2))

if __name__ == "__main__":
    main()

