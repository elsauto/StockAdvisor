# StockPrices (aka Maximum Proft)

## Context:
So I was tasked to write an algorithm that when given an array (or list, for this case) it would identify when the stock value is low enough to buy and then, high enough to sell. By doing do, then we would get the "maximum profit" value.

It also looks like this is an exercise that examiners like to throw in a coding interview so, I thought that sharing might help someone along the way.

Finally, this is no real time analysys solution. For that, I can not think of a possible solution that would not include local min/max and/or ML. But then again, this is a logic exercise.
## Possible solution:

The function maxiStockProfit takes an input (e.g.: a daily list of a stock value per hour). It will return the biggest difference between the lowest and the highest value in the list (buying low and selling high).

The algorithm works iterating over a nested for loop. All values in the sequence "i" (the buying points) go over all indexes "j>i", (the selling points). For each buying/selling pair (i,j), we calculate the difference (profit) between the prices at the selling and the buying points. list[j]-list[i].

### Reference output for the 3 three sample lists will be:

* values where buy: $2 and sell $11 --> Max Profit: 9
* values where buy: $9 and sell $10 --> Max Profit: 1
* values where buy: $45 and sell $460 --> Max Profit: 415

[logo]: https://github.com/elsauto/StockPrices/blob/main/images/banner.png "Maximum Profit"

Hope it helps!.
