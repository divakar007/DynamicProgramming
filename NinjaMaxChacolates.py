def maximumChocolatesDp(r, c, grid):
    minimum = -float('inf')

    dp = [[[minimum for i in range(c)] for j in range(c)] for k in range(r)]

    for col1 in range(c):
        for col2 in range(c):
            if col1 == col2:
                dp[r - 1][col1][col2] = grid[r - 1][col1]
            else:
                dp[r - 1][col1][col2] = grid[r - 1][col1] + grid[r - 1][col2]

    for row in range(r - 2, -1, -1):
        for col1 in range(c):
            for col2 in range(c):
                for move in range(-1, 2):
                    for move2 in range(-1, 2):
                        if 0 <= col1 + move < c and 0 <= col2 + move2 < c:
                            if col1 != col2:
                                dp[row][col1][col2] = max(dp[row][col1][col2],
                                                          grid[row][col1] + grid[row][col2] + dp[row + 1][col1 + move][
                                                              col2 + move2])
                            else:
                                dp[row][col1][col2] = max(dp[row][col1][col2],
                                                          grid[row][col1] + dp[row + 1][col1 + move][col2 + move2])

    return dp[0][0][c - 1]


def maximumChocolatesMemoization(r, c, grid, row, col1, col2, memo):
    if memo[row][col1][col2] != -1:
        return memo[row][col1][col2]

    if row == r - 1:
        if col1 == col2:
            return grid[row][col1]
        return grid[row][col1] + grid[row][col2]

    maximum = -10 ** 9

    for move in range(-1, 2):
        for move2 in range(-1, 2):
            if 0 <= col1 + move < c and 0 <= col2 + move2 < c:
                if col1 != col2:
                    maximum = max(maximum,
                                  grid[row][col1] + grid[row][col2] + maximumChocolatesMemoization(r, c, grid, row + 1,
                                                                                                   col1 + move,
                                                                                                   col2 + move2, memo))
                else:
                    maximum = max(maximum,
                                  grid[row][col1] + maximumChocolatesMemoization(r, c, grid, row + 1, col1 + move,
                                                                                 col2 + move2, memo))
    memo[row][col1][col2] = maximum
    return maximum


def maximumChocolatesUtil(r, c, grid, row, col1, col2):
    if row == r - 1:
        if col1 == col2:
            return grid[row][col1]
        return grid[row][col1] + grid[row][col2]

    maximum = -10 ** 9

    for move in range(-1, 2):
        for move2 in range(-1, 2):
            if 0 <= col1 + move < c and 0 <= col2 + move2 < c:
                if col1 != col2:
                    maximum = max(maximum,
                                  grid[row][col1] + grid[row][col2] + maximumChocolatesUtil(r, c, grid, row + 1,
                                                                                            col1 + move, col2 + move2))
                else:
                    maximum = max(maximum, grid[row][col1] + maximumChocolatesUtil(r, c, grid, row + 1, col1 + move,
                                                                                   col2 + move2))

    return maximum


def maximumChocolates(r, c, grid):
    memo = [[[-1 for i in range(c)] for j in range(c)] for k in range(r)]

    print("Dynamic Programming: ", maximumChocolatesDp(r, c, grid))
    print("Memoization: ",maximumChocolatesMemoization(r, c, grid, 0, 0, c-1, memo))
    print("Recursion:", maximumChocolatesUtil(r, c, grid, 0, 0, c-1))


def main():
    # Define the input matrix and its dimensions
    matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
    n = len(matrix)
    m = len(matrix[0])

    # Call the maximumChocolates function and print the result
    maximumChocolates(n, m, matrix)


if __name__ == "__main__":
    main()
