def minSubsetSumDifference(arr, n):
    target = sum(arr)
    dp = [[False for i in range(target + 1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = True

    if arr[0] <= target:
        dp[0][arr[0]] = True

    for index in range(1, n):
        for cs in range(1, target + 1):
            if target - arr[index] < 0:
                dp[index][cs] |= dp[index - 1][cs]
            else:
                dp[index][cs] = (dp[index - 1][cs - arr[index]] | dp[index - 1][cs])

    minimum = 10 ** 9 + 7
    for currsum in range(1, target + 1):
        if dp[n - 1][currsum] and dp[n - 1][target - currsum]:
            minimum = min(minimum, abs(target - 2 * currsum))
    return minimum


def main():
    arr = [1, 2, 3, 4]
    n = len(arr)

    # Find and print the minimum absolute difference between two subsets.
    print("The minimum absolute difference is:", minSubsetSumDifference(arr, n))


if __name__ == "__main__":
    main()
