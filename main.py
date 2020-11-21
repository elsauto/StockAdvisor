# stock price x hr.
# [10, 2, 9, 4, 5, 6, 11, 1]
# [9, 10, 9, 8, 7, 6, 5, 4]

sampleStockList = [10, 2, 9, 4, 5, 6, 11, 1]
sampleStockList_2 = [9, 10, 9, 8, 7, 6, 5, 4]
sampleStockList_3 = [45, 460, 63, 66, 89, 45, 44]


def maxStockProfit(list):
    #
    profit = 0
    buyVal = 0
    sellVal = 0

    for i in range(len(list)):
        partialList = (list[i+1:])
        #
        for stock in partialList:
            #
            transaction = stock - list[i]
            #
            if transaction > profit:
                profit = transaction
                buyVal = list[i]
                sellVal = stock
    print(str('values where buy: ${} and sell ${} --> Max Profit: {}'.format(buyVal, sellVal, profit)))


maxStockProfit(sampleStockList)
maxStockProfit(sampleStockList_2)
maxStockProfit(sampleStockList_3)
