# Please write your bitcoin_converter program in this file.
# Begin by outputting date and time of conversion bitcoin to USD.
# Next, input bitcoin amount.
# Next, conversion of bitcoin to USD.
# Last, output should be USD amount.

# $7,081.11 @ 9:17am 8/29/18

print ('As of 8/29/18 at 9:17 am, bitcoin is currently trading at $7081.11 per bitcoin.')

def BcToUsdConversion():
    usdTo1Bitcoin = 7081.11
    bitcoinAmtInput = input('Enter the bitcoin amount: ')
    usdToBitcoin = float(bitcoinAmtInput) * usdTo1Bitcoin 
    print('That is worth', usdToBitcoin, 'us dollars.')
    
BcToUsdConversion()