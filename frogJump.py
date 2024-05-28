# Problem Statement: Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th
# stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog
# jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means
# the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to
# stair N-1.

def recursion(no_of_stairs, heights):
    if no_of_stairs == 1 or no_of_stairs == 2:
        return 0
    return min(
        abs(heights[no_of_stairs - 1] - heights[no_of_stairs - 2]) + recursion(no_of_stairs - 1, heights),
        abs(heights[no_of_stairs - 1] - heights[no_of_stairs - 3]) + recursion(no_of_stairs - 2, heights)
    )


def tabulation(no_of_stairs, heights):
    dp = [0 for i in range(no_of_stairs + 1)]
    dp[1] = 0
    dp[2] = 0

    for i in range(3, no_of_stairs + 1):
        dp[i] = min(dp[i - 1] + abs(heights[i-1] - heights[i - 2]), dp[i - 2] + abs(heights[i-1] - heights[i - 3]))

    return dp[no_of_stairs]


n = int(input("enter no of stairs: "))
heights_of_stairs = list(map(int, input("enter the heights of n stairs").split()))
print("minimum energy required to reach nth stair recursion : " + str(recursion(n, heights_of_stairs)))
print("minimum energy required to reach nth stair tabulation : " + str(tabulation(n, heights_of_stairs)))
