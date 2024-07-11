def solution(n):
    matrix = [[0] * n for _ in range(n)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current = 0

    row, col = 0, 0
    for num in range(1, n * n + 1):
        matrix[row][col] = num
        next_row = row + directions[current][0]
        next_col = col + directions[current][1]

        if (
            next_row < 0
            or next_row >= n
            or next_col < 0
            or next_col >= n
            or matrix[next_row][next_col] != 0
        ):
            current = (current + 1) % 4
            next_row = row + directions[current][0]
            next_col = col + directions[current][1]

        row, col = next_row, next_col

    return matrix


def main():
    n1 = 4
    n2 = 5

    print(solution(n1))
    print(solution(n2))


if __name__ == "__main__":
    main()
