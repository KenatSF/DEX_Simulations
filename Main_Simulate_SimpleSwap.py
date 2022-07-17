#   Note: For my future my self: X = {WETH, DAI, USDC, USDT} and Y = {any other token} we are looking for the optimal X
#  Swapping    X   for     Y
from profits_optimizers import optimize_3_2 as dexo3
import time
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
    'SPOOL': 439666.3311, 'DAI': 1723320.4409
}
sushi = {
    'name': 'SUSHI',
    'DAI': 0.0, 'SPOOL': 0.0

}

quick = {
    'name': 'QUICKSWAP',
    'MNEP': 59011, 'MATIC':767
}

############################################################                    Variables

innocent_swap = 300000

dex_a = uni
dex_b = sushi
dex_c = quick

x = 'MNEP'
y = 'MATIC'




############################################################                    Simulation
print("--------------------------------")
#print("Amount waited for 1 simple {}".format())
innocent_amount_waited = getAmountOut(innocent_swap, dex_c[x], dex_c[y])
print("Amount In: {} {} and then amount Out: {} {}".format(innocent_swap, x, innocent_amount_waited, y))
print(" ")
print("Initial reserves:")
#print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
#print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_c['name'], x, dex_c[x], y,dex_c[y]))
print("--------------------------------")
print("INNOCENT SWAP")
innocent_amount_out = swap(dex_c, x, y, innocent_swap)
print("Swap: {} {} for {} {}, swapping at: {}".format(innocent_swap, x, innocent_amount_out, y, dex_c['name']))
print(" ")
print("Reserves: ")
#print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_a['name'], x, dex_a[x], y,dex_a[y]))
#print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_b['name'], x, dex_b[x], y,dex_b[y]))
print("{} DEX Reserves {}: {} Reserves {}: {}".format(dex_c['name'], x, dex_c[x], y,dex_c[y]))

end = time.time()
print("Tiempo de ejecución: {}".format(end - start))