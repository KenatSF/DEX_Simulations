import time



#   Note: For my future my self: X = {WETH, DAI, USDC, USDT} and Y = {any other token} we are looking for the optimal X
#  Swapping    Y   for     X


start = time.time()
############################################################                    Useful functions
def getAmountOut(amountIn, reserveIn, reserveOut):  # This function does the same as its contrapart in uniswap contract
    amountInWithFee = amountIn * 997
    numerator = amountInWithFee * reserveOut
    denominator = reserveIn * 1000 + amountInWithFee
    amountOut = numerator / denominator

    return amountOut

def swap(router, _tokenIn, _tokenOut, amount):
    amountOut = getAmountOut(amount, router[_tokenIn], router[_tokenOut])
    router[_tokenIn] = router[_tokenIn] + amount
    router[_tokenOut] = router[_tokenOut] - amountOut
    return amountOut
############################################################                    Reserves

uni = {
    'name': 'UNI  ',
    'WETH':111.1419,
    'RLC':79638.8285
}
sushi = {
    'name': 'SUSHI',
    'WETH':225.3851,
    'RLC':159290.0025
}


############################################################                    Variables

initial_amount = 29.021057042672970103


innocent_swap = 1772.984136

dex_a = uni
dex_b = sushi
x = 'WETH'
y = 'RLC'


#uni = ideal_1
#sushi = ideal_2
############################################################                    Simulation
#   Note: For my future my self: X = {WETH, DAI, USDC, USDT} and Y = {any other token} we are looking for the optimal X
print("--------------------------------")
print("Amount waited for Innocent")
innocent_amount_waited = getAmountOut(innocent_swap, dex_a[y], dex_a[x])                                             #  Swapping    Y   for     X
print("Amount In: {} {} and then amount Out: {} {}, swapping at: {}".format( innocent_swap, y, innocent_amount_waited, x, dex_a['name']))
print(" ")
print("Initial reserves:")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))

print("--------------------------------")
print("FIRST PART OF FRONT-RUNNING")
amount_01 = swap(dex_b, x, y, initial_amount)
print(" ")
print("First arbitrage Swap: {} {} for {} {}, swapping at: {}".format(initial_amount, x, amount_01, y, dex_b['name']))
print(" ")
print("Reserves")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))
amount_02 = swap(dex_a, y, x, amount_01)
print(" ")
print("Second arbitrage Swap: {} {} for {} {}, swapping at: {}".format(amount_01, y, amount_02, x, dex_a['name']))
print(" ")
print("Reserves")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))

print("--------------------------------")
print("INNOCENT SWAP")
innocent_amount_out = swap(dex_a, y, x, innocent_swap)
print("Swap: {} {} for {} {}, swapping at: {}".format(innocent_swap, y, innocent_amount_out, x, dex_a['name']))
print(" ")
print("Reserves")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))

print("--------------------------------")
print("SECOND PART OF FRONT-RUNNING")
amount_second_front_running = amount_02
amount_11 = swap(dex_a, x, y, amount_second_front_running)
print(" ")
print("First arbitrage Swap: {} {} for {} {}, swapping at: {}".format(amount_second_front_running, x, amount_11, y, dex_a['name']))
print(" ")
print("Reserves")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))
amount_12 = swap(dex_b, y, x, amount_11)
print(" ")
print("Second arbitrage Swap: {} {} for {} {}, swapping at: {}".format(amount_11, y, amount_12, x, dex_b['name']))
print(" ")
print("Reserves")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))
print("--------------------------------")
print("PROFITS:")
final_amount = amount_12
profit = final_amount - initial_amount
print("Initial amount: {}".format(initial_amount))
print("Final amount: {}".format(final_amount))
price_in_usd = 3225.30
print("PROFIT in {}: {}".format(x, profit))
print("PROFIT in USD: {}".format(profit*price_in_usd))
print("Slippage gotten: {} %".format(((innocent_amount_out/innocent_amount_waited)*(-1)+1)*100))
print(" ")
print("Final Reserves")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))