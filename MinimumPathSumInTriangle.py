def minimum_path_sum(triangle, n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for row in range(1, n):
        for col in range(row + 1):
            if col == 0:
                dp[row][col] = triangle[row][col] + dp[row - 1][col]
            elif col == row:
                dp[row][col] = triangle[row][col] + dp[row - 1][col - 1]
            else:
                dp[row][col] = triangle[row][col] + min(dp[row - 1][col], dp[row - 1][col - 1])
    return min(dp[n-1])


def main():
    # Define the input triangle and its size
    triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
    n = len(triangle)

    # Call the minimum_path_sum function and print the result
    print(minimum_path_sum(triangle, n))


if __name__ == '__main__':
    main()
