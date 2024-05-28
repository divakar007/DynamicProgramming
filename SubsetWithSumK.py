def subsetSumToKUtil(n, k, arr, index, currSum):
    if k == currSum:
        return True
    if k < currSum:
        return False
    if index == n:
        return False

    return subsetSumToKUtil(n, k, arr, index + 1, currSum + arr[index]) or subsetSumToKUtil(n, k, arr, index + 1,
                                                                                            currSum)


def subsetSumToKDpUtil(n, k, arr):
    if k == 0:
        return True
    if k > sum(arr):
        return False

    dp = [[False for i in range(k + 1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = True

    if arr[0] <= k:
        dp[0][arr[0]] = True

    for index in range(1, n):
        for cs in range(1, k + 1):
            if cs - arr[index] < 0:
                dp[index][cs] |= dp[index - 1][cs]
            else:
                dp[index][cs] |= (dp[index - 1][cs - arr[index]] | dp[index - 1][cs])

    return dp[n - 1][k]


def subsetSumToK(n, k, arr):
    return subsetSumToKDpUtil(n, k, arr)


def main():
    arr = [1, 2, 3, 4]
    k = 4
    n = len(arr)

    if subsetSumToK(n, k, arr):
        print("Subset with the given target found")
    else:
        print("Subset with the given target not found")


if __name__ == "__main__":
    main()
