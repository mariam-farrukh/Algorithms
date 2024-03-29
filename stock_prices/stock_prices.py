#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_prof = -max(prices)
  #Can't change the prices array because you need if for the if statement later, so use copy()
  arr = prices.copy()
  for x in range(len(prices)):
    #Take the first value out of the array
    arr.pop(0)
    for i in arr:
      # It goes through the array, and sets the max profit each time. If the max profit is bigger for a different point, then the max profit will be set again, otherwise it goes through the loop again without setting it.
      if i - prices[x] > max_prof:
        max_prof = i - prices[x]
  return max_prof

  ## Other way of doing this after understaning what was being asked
    # current_min_price_so_far = prices[0]
    # max_profit_so_far = prices[1] - prices[0]

    # for i in range(1, len(prices)):
    #     if prices[i] < current_min_price_so_far:
    #         current_min_price_so_far = prices[i]
    #     elif prices[i] - current_min_price_so_far > max_profit_so_far:
    #         max_profit_so_far = prices[i] - current_min_price_so_far
    # return max_profit_so_far

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))