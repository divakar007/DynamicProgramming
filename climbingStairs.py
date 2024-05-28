# Problem Statement: Given a number of stairs. Starting from the 0th stair we need to climb
# to the “Nth” stair. At a time we can climb either one or two steps. We need to return the total number of distinct
# ways to reach from 0th to Nth stair.

def recursion(n):
    if n == 1:
        return 1
    if n > 2:
        return recursion(n - 1) + recursion(n - 2)
    else:
        return recursion(n - 1)


def memoization(n, dp):
    if dp[n] != -1:
        return dp[n]
    if n == 1:
        return 1
    if n > 2:
        dp[n] = memoization(n - 1, dp) + memoization(n - 2, dp)
        return dp[n]
    else:
        dp[n] = memoization(n - 1, dp)
        return dp[n]


def tabulation(n, dp):
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n-1]


no_of_stairs = int(input())
print("no of ways to reach nth stair : recursion - " + str(recursion(no_of_stairs)))
dpm = [-1 for i in range(no_of_stairs + 1)]
print("no of ways to reach nth stair : memoization - " + str(memoization(no_of_stairs, dpm)))
dpt = [0 for _ in range(no_of_stairs + 1)]
print("no of ways to reach nth stair : tabulation - " + str(tabulation(no_of_stairs, dpt)))
