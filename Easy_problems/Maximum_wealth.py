
def maximumWealth(accounts: list[list[int]]) -> int:
        wealth_list = []
        for customer in accounts:
            wealth = 0
            for money in customer:
                wealth += money
            wealth_list.append(wealth)
        return max(wealth_list)

