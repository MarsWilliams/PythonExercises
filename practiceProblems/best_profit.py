def best_profit(stock_prices_yesterday):
  lowest_price = stock_prices_yesterday[0]
  final_price = 0
  profits = [ ]
  for i in range(1, len(stock_prices_yesterday)):
  	if stock_prices_yesterday[i] > final_price and stock_prices_yesterday[i] > lowest_price:
  		final_price = stock_prices_yesterday[i]
  		profits.append(final_price - lowest_price)
  	if stock_prices_yesterday[i] < lowest_price:
  		lowest_price = stock_prices_yesterday[i]
  		final_price = 0
  return max(profits)

# //compares two parameters, and if they are not equal, returns an error
def assertEqual(a, b):
    if (a == b):
    	return True
    else:
    	print (" mismatch: " + str(a) + " != " + str(b))

test1 = best_profit([500, 300, 200, 600, 900, 100]);
test2 = best_profit([100, 300, 400, 50, 10, 100]);

print(assertEqual( test1, 700))
print(assertEqual( test2, 300))
