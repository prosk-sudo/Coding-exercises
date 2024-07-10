def solution(orders):
    #    answer = 0
    #    for order in orders:
    #        if "cafelatte" in order:
    #            answer += 5000
    #        elif "americano" in order:
    #            answer += 4500
    #        else:
    #            answer += 4500
    #    return answer

    return sum([5000 if "cafelatte" in order else 4500 for order in orders])


def main():
    order1 = ["cafelatte", "americanoice", "hotcafelatte", "anything"]
    order2 = ["americanoice", "americano", "iceamericano"]

    print(solution(order1))
    print(solution(order2))


if __name__ == "__main__":
    main()
