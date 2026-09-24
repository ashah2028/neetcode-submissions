class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    

        #bottom up approach (not recursive)
        #dp[i] = min cost to reach step i = OPT(i)
        #2 cases for OPT(i)
                        #i-1: OPT(i-1) + cost[i-1]
                        #i-2L OPT(i-2) + cost[i-2]
            #OPT(i) = min(dp[i-1], dp[i-2])

        #n equal number of steps
        n = len(cost)
        #initalize dp array n+1
        DP = [-1] * (n+1)
        DP[0] = 0
        DP[1] = 0
        
        #for each step (2->n)
        for i in range(2, n + 1):
            #Update DP table with OPT(i)
            DP[i] = min(DP[i-1] + cost[i-1], DP[i-2] + cost[i-2])
        
        #return cost at n
        return DP[n]