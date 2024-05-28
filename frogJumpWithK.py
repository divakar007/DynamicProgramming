# Problem statement
# There is an array of heights corresponding to 'n' stones. You have to reach from stone 1 to stone ‘n’.
# From stone 'i', it is possible to reach stones 'i'+1, ‘i’+2… ‘i’+'k' , and the cost incurred will be | Height[
# i]-Height[j] |, where 'j' is the landing stone.
#
# Return the minimum possible total cost incurred in reaching the stone ‘n’.
#
# Example:
# For 'n' = 3 , 'k' = 1, height = {2, 5, 2}.
#
# Answer is 6.
# Initially, we are present at stone 1 having height 2. We can only reach stone 2 as ‘k’ is 1. So, cost incurred is
# |2-5| = 3. Now, we are present at stone 2, we can only reach stone 3 as ‘k’ is 1. So, cost incurred is |5-2| = 3.
# So, the total cost is 6.


def recursion(no_of_stairs, heights, k):
    if no_of_stairs <= k:
        return 0
    minimum = 2 ** 32 - 1

    for i in range(k):
        minimum = min(minimum,
                      abs(heights[no_of_stairs - 1] - heights[no_of_stairs - i - 2]) + recursion(no_of_stairs - 1 - i,
                                                                                                 heights, k))

    return minimum


def tabulation(no_of_stairs, heights, k):
    dp = [2 ** 32 - 1 for i in range(no_of_stairs + 1)]

    for i in range(k + 1):
        dp[i] = 0
    for j in range(k + 1, no_of_stairs+1):
        minimum = 2 ** 32 - 1
        for i in range(k):
            minimum = min(minimum, abs(heights[j - 1] - heights[j - i - 2]) + dp[j - 1 - i])

        dp[j] = minimum
    return dp[no_of_stairs]


n = int(input("enter the number of stairs : "))
heights_of_stairs = list(map(int, input("enter the heights of the stairs: ").split()))
k = int(input("enter the k Value: "))
print("minimum energy required to reach nth stair: recursion -  " + str(recursion(n, heights_of_stairs, k)))
print("minimum energy required to reach nth stair: tabulation -  " + str(tabulation(n, heights_of_stairs, k)))
