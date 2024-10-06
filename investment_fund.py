# You are managing an investment fund with a very specific target:
# allocating your capital between a specific set of stocks based on their recent performance.
# You want to invest proportionally to the last observed stock return if it's positive,
# or not invest in a stock if the return was negative.
# If no stocks returns were positive, you will not invest in any of them, keeping cash at hand.
# You'll need to adjust your holdings based on the market behavior.
# You'd like to backtest this strategy using historical market data.

# As an example, let's say you want to invest in stocks A and B, and you have 1 million USD to invest.
# On day 0, stock A is worth 100 USD and stock B is worth 200 USD.
# Initially, you don't know the returns of these stocks, so you'll keep your cash un-invested. 

# On day 1 stock A goes up to 115 USD, and stock B goes up to 210 USD.
# This means the return of stock A is 15% and of stock B is 5%.
# You'll allocate 3/4 of your capital (750000 USD) to stock A and 1/4 (250000 USD) to stock B.

# On day 2, stock A goes up to 117.3 USD, and stock B goes down to 199.5 USD.
# This means the return of stock A is 2% and the return of stock B is -5%.
# Your holdings are now worth 765000 USD in stock A and 237500 USD in stock B.
# Given that the return of stock B is negative,
# you'll sell all your positions in it and put everything (1002500 USD) into stock A.

# You're given an N by T array of timeseries of end-of-day stock prices.
# Return an array with two numbers:
# the average daily log return and the standard deviation of log returns,
# assuming you followed the allocation strategy described above.
# Assume that you can trade any number of shares,
# including fractional amounts, at each rebalance time.

import math

def investment_strategy(prices):
    # prices is a 2D list with N rows and T columns,
    # where each row represents a stock's daily closing prices

    N = len(prices)  # Number of stocks
    T = len(prices[0])  # Number of days

    holdings = 1_000_000 # Any number would do actually
    log_returns = [0] # The daily log returns (no investment on day 0)

    # Start calculating from day 1 to the 2nd-last day
    for t in range(1, T-1):
        # Calculate the daily returns for each stock
        returns = [(prices[i][t] - prices[i][t - 1]) / prices[i][t - 1] for i in range(N)]

        # Check if all stocks have negative returns, if so keep the cash uninvested
        if all(ret <= 0 for ret in returns):
            log_returns.append(0)  # No investment, return is 0
            continue

        # If there are positive returns, distribute cash proportionally
        positive_returns = [(i, returns[i]) for i in range(N) if returns[i] > 0]
        total_positive_return = sum(ret for _, ret in positive_returns)

        # Calculate the investment weights based on positive returns
        weights = [(i, ret / total_positive_return) for i, ret in positive_returns]

        # Calculate how much to invest in each stock
        investment = [(i, holdings * weight) for i, weight in weights]
        
        # Calculate the log return (between day t and day t+1)
        next_day = 0
        # Iterate through investment details
        for idx, amount in investment:
            # Allocated amount to this stock * next day's price
            next_day += amount / prices[idx][t] * prices[idx][t+1]
        
        # Calculate the log return
        log_return = math.log(next_day / holdings)
        log_returns.append(log_return)

        # Update holdings to the next day value
        holdings = next_day

    # Calculate the average log return
    avg_log_return = sum(log_returns) / len(log_returns) if log_returns else 0

    # Calculate the standard deviation of the log returns
    if log_returns:
        variance = sum((r - avg_log_return) ** 2 for r in log_returns) / len(log_returns)
        std_log_return = variance ** 0.5
    else:
        std_log_return = 0
    
    return [avg_log_return, std_log_return]

# Example test
prices = [
    [100, 115, 117.3],
    [200, 210, 199.5]
]

result = investment_strategy(prices)
print(f"Average Log Return: {result[0]:.5f}")
print(f"Standard Deviation of Log Return: {result[1]:.5f}")