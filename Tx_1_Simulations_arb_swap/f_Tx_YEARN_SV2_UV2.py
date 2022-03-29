from profits_optimizers import optimize_3_2 as dexo3
import time

#   Note: For my future my self: X = {WETH, DAI, USDC, USDT} and Y = {any other token} we are looking for the optimal X
#   Swapping    X   for     Y

start = time.time()
############################################################                    Useful functions
def getAmountOut(amountIn, reserveIn, reserveOut):  # This function does the same as its contrapart in uniswap contract
    amountInWithFee = amountIn * 0.997
    numerator = amountInWithFee * reserveOut
    denominator = reserveIn * 1 + amountInWithFee
    amountOut = numerator / denominator

    return amountOut
def swap(router, _tokenIn, _tokenOut, amount):
    amountOut = getAmountOut(amount, router[_tokenIn], router[_tokenOut])
    router[_tokenIn] = router[_tokenIn] + amount
    router[_tokenOut] = router[_tokenOut] - amountOut
    return amountOut
############################################################                    Reserves

uni = {
    'name': 'UNISWAP',
    'YEARN':57.7848,
    'WETH':430.0693
}
sushi = {
    'name': 'SUSHI',
    'YEARN':2545.5225,
    'WETH':18797.1696

}

############################################################                    Variables
innocent_swap = 15.5

dex_a = uni
dex_b = sushi
x = 'WETH'
y = 'YEARN'

psvar = dexo3.get_values(dex_a[x], dex_a[y], dex_b[x], dex_b[y], innocent_swap, 10000)

#flash_loan = psvar[1]
flash_loan = 1



############################################################                    Simulation
#   Note: For my future my self: X = {WETH, DAI, USDC, USDT} and Y = {any other token} we are looking for the optimal X
print("--------------------------------")
print("Amount waited for Innocent")
innocent_amount_waited = getAmountOut(innocent_swap, dex_a[x], dex_a[y])                                            #   Swapping    X   for     Y
print("Amount In: {} {} and then amount Out: {} {}, swapping at: {}".format( innocent_swap, x, innocent_amount_waited, y, dex_a['name']))
print(" ")
print("Initial reserves:")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))
print("--------------------------------")
print("INNOCENT SWAP")
innocent_amount_out = swap(dex_a, x, y, innocent_swap)
print("Swap: {} {} for {} {}, swapping at: {} ".format(innocent_swap, x, innocent_amount_out, y, dex_a['name']))
print(" ")
print("Reserves")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))
print("--------------------------------")
print("Flash Loan Swap")
amount_for_swapping = flash_loan
print("Flash Loan amount: {}".format(amount_for_swapping))
amount_11 = swap(dex_b, x, y, amount_for_swapping)
print(" ")
print("First arbitrage Swap: {} {} for {} {}, swapping at: {}".format(amount_for_swapping, x, amount_11, y, dex_b['name']))
print(" ")
print("Reserves")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))
amount_12 = swap(dex_a, y, x, amount_11)
print(" ")
print("Second arbitrage Swap: {} {} for {} {}, swapping at: {}".format(amount_11, y, amount_12, x, dex_a['name']))
print(" ")
print("Reserves")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))
print("--------------------------------")
print("Flash Loan profit")
flash_profit = amount_12 - (amount_for_swapping + amount_for_swapping * 0.0009)
print("PROFIT in {}: {}".format(x, flash_profit))
price = 3311.12
print("PROFIT in USD: {}".format(flash_profit*price))
print(" ")
print("Final Reserves")
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))
print("ps: -------------------------------")
#print(psvar)
print("Tenemos los siguientes valores; p1:  {}       &       p2:  {}".format(psvar[0], psvar[1]))
end = time.time()
print("Tiempo de ejecución: {}".format(end - start))










