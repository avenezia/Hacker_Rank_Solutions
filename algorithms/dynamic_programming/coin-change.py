def number_of_ways_to_change(amount, coin_types, coins):
    # Table containing amount + 1 rows with coin_types columns
    table = [[0 for x in range(coin_types)] for x in range(amount +1)]
 
    # In case the amount is 0, there is only one solution: not including any coin.
    for i in range(coin_types):
        table[0][i] = 1
 
    # Filling the rest of the table following a bottom-up approach:
    # outer loop on the ith amount, inner on the jth coin type
    for i in range(1, amount + 1):
        for j in range(coin_types):
            solutions_with_jth_coin = table[i - coins[j]][j] if i - coins[j] >= 0 else 0
            solutions_excluding_jth_coin = table[i][j-1] if j >= 1 else 0
            table[i][j] = solutions_with_jth_coin + solutions_excluding_jth_coin
 
    return table[amount][coin_types-1]

amount_to_change, coin_types = map(int,raw_input().strip().split(' '))
coins = map(int,raw_input().strip().split(' '))
assert len(coins) == coin_types
print number_of_ways_to_change(amount_to_change, coin_types, coins)