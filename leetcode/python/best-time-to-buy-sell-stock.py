
def max_profit(prices):
    buy = prices[0]

    max_profit = 0
    next_day = 1

    for day in range(1, len(prices)):
        profit = prices[day] - buy

        if profit > max_profit:
            max_profit = profit

        if buy > prices[day]:
            buy = prices[day]


    return max_profit

        
nums = [7,1,5,3,6,4]
assert max_profit(nums) == 5

nums = [7,6,4,3,1]
assert max_profit(nums) == 0

nums = [2,4,1]
assert max_profit(nums) == 2
