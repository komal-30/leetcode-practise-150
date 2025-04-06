
def maxProfit(prices):
        min_val = prices[0]
        max_val = 0
        index_start = 0
        for i in range(1,len(prices)):
            if prices[i] < min_val :
                min_val = prices[i]
                index_start = i
        if index_start != len(prices)-1:
            for j in range(index_start+1,len(prices)):
                if prices[j] > max_val:
                    max_val = prices[j]  
        else:
            return 0
        
        return max_val-min_val
print(maxProfit([7,1,5,3,6,4]))



'''
  min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
        
        return max_profit
        
'''