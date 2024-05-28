def ninjaTrainingRecursion(n, points, last):
    if n == 0:
        maximum = 0
        for i in range(len(points[0])):
            if i != last:
                maximum = max(maximum, points[n][i])
        return maximum

    maximum = 0
    for i in range(len(points[0])):
        if i != last:
            maximum = max(maximum, points[n][i] + ninjaTrainingRecursion(n - 1, points, i))
    return maximum


def memoization(n, points, last, memo):
    if n == 0:
        maximum = 0
        for i in range(len(points[0])):
            if i != last:
                maximum = max(maximum, points[n][i])
        return maximum
    maximum = 0

    for i in range(len(points[0])):
        if i != last:
            if memo[n][i] == 0:
                maximum = max(maximum, points[n][i] + ninjaTrainingRecursion(n - 1, points, i))
            else:
                maximum = max(maximum, points[n][i] + memo[n][i])
    return maximum


def ninjaTrainingDp(n, points) -> int:
    dp = [[-1 for i in range(len(points[0]) + 1)] for i in range(n)]

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0])

    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    dp[day][last] = max(dp[day][last], points[day][task] + dp[day - 1][task])

    return dp[n - 1][3]


def ninjaTraining(n, points):
    recursionMaxi = ninjaTrainingRecursion(n - 1, points, 3)
    memo = [[0 for i in range(len(points[0]))] for j in range(n)]
    memoMaxi = memoization(n - 1, points, 3, memo)
    dp_maximum = ninjaTrainingDp(n, points)

    return memoMaxi


def main():
    # Define the points matrix for each day.
    points = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]

    n = len(points)  # Get the number of days.
    # Call the ninjaTraining function to find the maximum points.
    print(ninjaTraining(n, points))


if __name__ == '__main__':
    main()
