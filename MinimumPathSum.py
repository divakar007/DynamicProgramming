def minimumSumPathRecursion(n, m, matrix):
    if n == 0 and m == 0:
        return matrix[n][m]
    upsum = float('inf')
    leftsum = float('inf')
    if n > 0:
        upsum = matrix[n][m] + minimumSumPathRecursion(n-1, m, matrix)
    if m > 0:
        leftsum = matrix[n][m] + minimumSumPathRecursion(n, m-1, matrix)

    return min(upsum, leftsum)

def minimumSumPathDp(n,m,matrix):
    dp = [[float('inf') for _ in range(m)] for _ in range(n)]

    #basecase

    dp[0][0] = matrix[0][0]
    for row in range(1, n):
        dp[row][0] = matrix[row][0] + dp[row-1][0]

    for col in range(1, m):
        dp[0][col] = matrix[0][col] + dp[0][col-1]

    for row in range(1, n):
        for col in range(1, m):
            dp[row][col] = matrix[row][col] + min(dp[row-1][col], dp[row][col-1])

    return dp[n-1][m-1]


def main():
    # Example matrix with values representing cell costs.
    matrix = [[5, 9, 6], [11, 5, 2]]
    n = len(matrix)
    m = len(matrix[0])

    # Call the minSumPath function and print the result.
    print("recursion:", minimumSumPathRecursion(n-1, m-1, matrix))
    print("dynamic Programming:", minimumSumPathDp(n,m, matrix))

if __name__ == "__main__":
    main()