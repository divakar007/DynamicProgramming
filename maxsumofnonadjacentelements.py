def maxSumOfNonAdjacentElements(arr, index):
    if index >= len(arr):
        return 0
    return max(arr[index]+maxSumOfNonAdjacentElements(arr, index+2), maxSumOfNonAdjacentElements(arr, index+1))


def memoization(arr, index, memo):
    if index >= len(arr):
        return 0
    if memo[index] != -1:
        return memo[index]
    prev = arr[index] + memoization(arr, index+2, memo)
    next = memoization(arr, index+1, memo)

    memo[index] = max(prev, next)
    return memo[index]


def dynamicProgramming(arr):
    dp = [0 for _ in range(len(arr)+1)]
    dp[1] = arr[0]

    for i in range(2, len(arr)+1):
        dp[i] = max(arr[i-1]+dp[i-2], dp[i-1])
    print(dp)
    return dp[len(arr)]

arr1 = [2, 1, 4, 9]
memo = [-1] * len(arr1)
print(maxSumOfNonAdjacentElements(arr1, 0))
print(memoization(arr1, 0, memo))
print(dynamicProgramming(arr1))
