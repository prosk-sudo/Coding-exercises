def solution(board, k):
    row_count = len(board)
    col_count = len(board[0])
    #    sum = 0
    #
    #    for i in range(row_count):
    #        for j in range(col_count):
    #            if i + j <= k:
    #                sum += board[i][j]
    #    return sum

    return sum(
        board[i][j] for i in range(row_count) for j in range(col_count) if i + j <= k
    )


def main():
    board1, k1 = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]], 2

    print(solution(board1, k1))


if __name__ == "__main__":
    main()
