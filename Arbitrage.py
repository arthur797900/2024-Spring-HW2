# Define the provided liquidity dictionary
liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

# The initial amount of token B
initial_tokenB_no_fee = 5

# Define the trading path as given in the problem statement
trade_path_no_fee = [("tokenB", "tokenA"), ("tokenA", "tokenD"), ("tokenD", "tokenC"), ("tokenC", "tokenB")]


# Function to calculate the amount received after a trade given the liquidity pools without considering fees
def get_trade_output_no_fee(input_amount, input_reserve, output_reserve):
    numerator = input_amount * output_reserve
    denominator = input_reserve + input_amount
    output_amount = numerator / denominator
    return output_amount


# Calculate the final amount of token B after completing the trade path without considering fees
current_amount_no_fee = initial_tokenB_no_fee
for trade in trade_path_no_fee:
    input_token, output_token = trade
    if (input_token, output_token) in liquidity:
        input_reserve, output_reserve = liquidity[(input_token, output_token)]
    elif (output_token, input_token) in liquidity:  # Reverse pair
        output_reserve, input_reserve = liquidity[(output_token, input_token)]
    else:
        raise ValueError(f"No liquidity pool found for pair: {input_token}-{output_token}")

    current_amount_no_fee = get_trade_output_no_fee(current_amount_no_fee, input_reserve, output_reserve)

# Convert the trade path to a string representation
trade_path_str = "->".join([trade[0] for trade in trade_path_no_fee]) + "->" + trade_path_no_fee[-1][1]

# Print the path and the final balance
print(f"path: {trade_path_str}, tokenB balance={current_amount_no_fee}")
