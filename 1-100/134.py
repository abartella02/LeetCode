class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        stops = len(gas)
        for i in range(stops):
            j = i
            count = 0
            net_gas = 0
            while j < stops + i:
                net_gas += gas[j % stops] - cost[j % stops]
                if net_gas >= 0:
                    j += 1
                    count += 1
                else:
                    break
                if count == stops:
                    return i
        return -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
sol = Solution()
print(sol.canCompleteCircuit(gas, cost))
