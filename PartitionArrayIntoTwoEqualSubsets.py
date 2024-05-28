def canPartition(n, arr):
    # Write your code here.
    if sum(arr) % 2 == 1:
        return False
    target = sum(arr) // 2
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

    return dp[n - 1][target]


def main():
    arr = [2, 3, 3, 3, 4, 5]
    n = len(arr)

    # Check if the array can be partitioned into two equal subsets and print the result.
    if canPartition(n, arr):
        print("The Array can be partitioned into two equal subsets")
    else:
        print("The Array cannot be partitioned into two equal subsets")


if __name__ == "__main__":
    main()
