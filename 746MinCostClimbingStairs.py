class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_costs = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            min_costs.append(cost[i] + min(min_costs[i-1], min_costs[i-2]))
        return  min(min_costs[-1], min_costs[-2])
