class StockHolding:
    def __init__( self, numOfShares, initialStockPrice ):
        self.stockSymbol = 'MRY'
        self.numOfShares = numOfShares
        self.initialStockPrice = initialStockPrice
        
        
    def getSymbol(self):
        return self.stockSymbol 
        
    def getNumOfShares(self):
        return self.numOfShares
        
    def getTotalCost(self, numOfShares, initialStockPrice):
        totalCostofShares = self.numOfShares * self.initialStockPrice
        return totalCostofShares 
    
    def estimateProfit(self, numOfSharesToSell, stockPrice):
        self.numOfSharesToSell = numOfSharesToSell
        self.stockPrice = stockPrice
        potentialProfitOfShares = (self.numOfSharesToSell * self.stockPrice) - (self.initialStockPrice * self.numOfSharesToSell)
        return potentialProfitOfShares
        
    def sellShares(self, numSharesToSell):
        self.numSharesToSell = numSharesToSell
        newSharesAmt = self.numOfShares - self.numSharesToSell
        if newSharesAmt < 0:
            raise ValueError("The number of stocks you have is less than the amount you are trying to sell.")                
        else:
            self.numOfShares = newSharesAmt
            return self.numOfShares
   
def main():
    testStockHolding = StockHolding(100, 100)
    
    print(testStockHolding.getSymbol())
    print(testStockHolding.getNumOfShares())
    print(testStockHolding.getTotalCost(100, 100))
    if testStockHolding.estimateProfit(20, 150) == 1000:
        print('Yay, the estimated profit is $1000')
    if testStockHolding.sellShares(50) == 50:
        print('You are selling 50 shares and should have 50 left')
    testStockHolding.sellShares(51)


main()