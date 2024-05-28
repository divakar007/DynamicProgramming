MOD = 10 ** 9 + 7


def mazeObstacles(n, m, maze):
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        if maze[0][i] != -1:
            dp[0][i] = 1
        else:
            break
    for j in range(m):
        if maze[j][0] != -1:
            dp[j][0] = 1
        else:
            break

    for i in range(1, m):
        for j in range(1, n):
            if maze[i][j] != -1:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
    return dp[m - 1][n - 1]


def main():
    # Example maze with 0s representing open paths and -1 representing obstacles.
    maze = [[0, 0, 0],
            [0, -1, 0],
            [0, 0, 0]]
    n = len(maze)
    m = len(maze[0])

    # Call the mazeObstacles function and print the result.
    print(mazeObstacles(n, m, maze))


if __name__ == "__main__":
    main()
