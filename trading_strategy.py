# You are running a systematic trading strategy that suggests that you should hold n shares of a stock.
# Currently, you have k shares in your portfolio, and during the day,
# you know you will perform at most m buy or sell transactions, each for 1 share.
# How many distinct sequences of buy and sell transactions are there
# that achieve the desired position of n shares starting from k shares?

# For example in the case of n=2, k=1, there are 4 distinct sequences satisfying the requirements:
# 1) buy
# 2) buy, sell, buy
# 3) buy, buy, sell
# 4) sell, buy, buy


def WaysOfAchievingDesiredPosition(n, k, m):
    # Write your code here
    if k + m < n or k - m > n:
        return 0
    
    # number of sequences to achieve [k-m to k+m (shares of stock)]
    # after performing [0 to m (number of transactions)]
    offset, maxshare = k-m, 2*m+1
    dp = [[0] * maxshare for _ in range(m+1)]

    # having k shares of stocks after 0 transactions
    dp[0][k-offset] = 1

    # 1 to m transactions
    for i in range(1, m+1):
        # k-m to k+m shares of stock
        for j in range(maxshare):
            if j > 0:
                # can be achieved through buying
                dp[i][j] += dp[i-1][j-1]
            if j < maxshare-1:
                # can be achieve through selling
                dp[i][j] += dp[i-1][j+1]
    
    # maximum m steps (sum of 0-m steps)
    return sum(dp[i][n-offset] for i in range(m+1))
    

if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    m = int(input().strip())

    result = WaysOfAchievingDesiredPosition(n, k, m)
    print(str(result))