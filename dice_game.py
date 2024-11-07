# Bermudan Dice Game

# The question is to determine how much you would be willing to pay to enter a dice game,
# assuming no risk aversion (i.e., you would pay up to the expected payoff). In this game:
# You roll a fair six-sided die with numbers 1 through 6.
# After each roll, you have the option to:
# Accept the result as your final payoff.
# Roll again, discarding the previous result.
# This process continues for up to T rolls.
# On the final roll, you must accept the result.
# For example, if the first roll is high (like 6), you may choose to stop.
# If the roll is low (like 1), you may prefer to roll again.

# The goal is to write a function price that takes an integer T (the number of allowed rolls)
# and returns the expected payoff, rounded to four decimal places.

def price(num_throws):
    expectations = [3.5]
    
    for t in range(2, num_throws + 1):
        e_prev = expectations[-1]
        e_update = sum(max(x, e_prev) for x in range(1, 7)) / 6
        expectations.append(e_update)
    
    return round(expectations[-1], 4)
