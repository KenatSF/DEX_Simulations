const { getValues, swap, getAmountOut } = require('./profits_optimizers/js_optimize_3');
//############################################################                    Reserves

const uni = {
    'name': 'UNISWAP',
    'WETH':480.6258,
    'COTI':6264342.9764
}
const sushi = {
    'name': 'SUSHI',
    'COTI':890456.6928,
    'WETH':67.5926

}    

//############################################################                    Variables

const innocent_swap = 200000;

const dex_a = uni;
const dex_b = sushi;
const x = 'WETH';
const y = 'COTI';



//############################################################                    Simulation
console.log("--------------------------------")
console.log("Amount waited for Innocent");
var innocent_amount_waited = getAmountOut(innocent_swap, dex_a[y], dex_a[x]);
console.log(`Amount In: ${innocent_swap}, ${y} and then amount Out: ${innocent_amount_waited} ${x}`);
console.log(" ");
console.log("Initial reserves:")
console.log(`${dex_a['name']} DEX Reserves ${x}: ${dex_a[x]} Reserves ${y}: ${dex_a[y]}`);
console.log(`${dex_b['name']} DEX Reserves ${x}: ${dex_b[x]} Reserves ${y}: ${dex_b[y]}`);
console.log("--------------------------------")
console.log("INNOCENT SWAP")
var innocent_amount_out = swap(dex_a, y, x, innocent_swap)
console.log(`Swap ${innocent_swap} ${y} for ${innocent_amount_out} ${x}, swapping at: ${dex_a['name']}`);
console.log(" ");
console.log("Reserves:")
console.log(`${dex_a['name']} DEX Reserves ${x}: ${dex_a[x]} Reserves ${y}: ${dex_a[y]}`);
console.log(`${dex_b['name']} DEX Reserves ${x}: ${dex_b[x]} Reserves ${y}: ${dex_b[y]}`);
console.log(" ");
console.log("--------------------------------")
console.log("Flash Loan Swap")
var amount_for_swapping = getValues(dex_a[x], dex_a[y], dex_b[x], dex_b[y], true, false);
console.log(`Flash Loan amount: ${amount_for_swapping}`);
var amount_11 = swap(dex_a, x, y, amount_for_swapping)
console.log(" ");
console.log(`First arbitrage Swap: ${amount_for_swapping} ${x} for ${amount_11} ${y}, swapping at: ${dex_a['name']}`);
console.log(" ");
console.log("Reserves:")
console.log(`${dex_a['name']} DEX Reserves ${x}: ${dex_a[x]} Reserves ${y}: ${dex_a[y]}`);
console.log(`${dex_b['name']} DEX Reserves ${x}: ${dex_b[x]} Reserves ${y}: ${dex_b[y]}`);
var amount_12 = swap(dex_b, y, x, amount_11)
console.log(" ");
console.log(`Second arbitrage Swap: ${amount_11} ${y} for ${amount_12} ${x}, swapping at: ${dex_b['name']}`);
console.log(" ");
console.log("Reserves:")
console.log(`${dex_a['name']} DEX Reserves ${x}: ${dex_a[x]} Reserves ${y}: ${dex_a[y]}`);
console.log(`${dex_b['name']} DEX Reserves ${x}: ${dex_b[x]} Reserves ${y}: ${dex_b[y]}`);
console.log(" ");
console.log("--------------------------------")
console.log("Flash Loan profit")
var flash_profit = amount_12 - (amount_for_swapping + amount_for_swapping * 0.0009)
console.log(`PROFIT in ${x}: ${flash_profit}`);
var price = 3000.96
console.log(`PROFIT in USD: ${flash_profit*price}`);
console.log(" ");
console.log("Final Reserves: ")
console.log(`${dex_a['name']} DEX Reserves ${x}: ${dex_a[x]} Reserves ${y}: ${dex_a[y]}`);
console.log(`${dex_b['name']} DEX Reserves ${x}: ${dex_b[x]} Reserves ${y}: ${dex_b[y]}`);