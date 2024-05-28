def dynamicProgramming(n, m, matrix):
    dp = [[-10 ** 9 for i in range(m)] for j in range(n)]

    for i in range(m):
        dp[0][i] = matrix[0][i]

    for row in range(1, n):
        for col in range(m):
            for move in range(-1, 2):
                if 0 <= col + move < m:
                    dp[row][col] = max(dp[row][col], matrix[row][col] + dp[row - 1][col + move])

    return max(dp[n - 1])


def getMaxPathSumMemoizationUtil(n, m, matrix, row, col, memo):
    if row == n - 1:
        return matrix[row][col]

    maximum = -10 ** 9

    for move in range(-1, 2):
        if 0 <= col + move < m:
            if memo[row][col] == -10 ** 9:
                maximum = max(maximum,
                              matrix[row][col] + getMaxPathSumMemoizationUtil(n, m, matrix, row + 1, col + move, memo))
            else:
                maximum = max(maximum, memo[row][col])
    memo[row][col] = maximum
    return maximum


def getMaxPathSumRecursionUtil(n, m, matrix, row, col):
    #basecase
    if row == n - 1:
        return matrix[row][col]
    maximum = -10 ** 9
    for move in range(-1, 2):
        if m > col + move >= 0:
            maximum = max(maximum, matrix[row][col] + getMaxPathSumRecursionUtil(n, m, matrix, row + 1, col + move))
    return maximum


def getMaxPathSum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    maximum = -10 ** 9
    for i in range(m):
        maximum = max(maximum, getMaxPathSumRecursionUtil(n, m, matrix, 0, i))
    return maximum


def main():
    # Define the input matrix
    matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]

    # Call the getMaxPathSum function and print the result
    print(getMaxPathSum(matrix))


if __name__ == "__main__":
    main()
