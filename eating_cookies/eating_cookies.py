#!/usr/bin/python

import sys

#It takes: number of cookies
#Returns how many ways to eat

#Jar with 10 cookies:
#3 + jar with 7 cookies
#2 + jar with 8 cookies
#1 with jar with 9 cookies

# This problem is very similar to the example Beej did in lecture for fibonacci
def eating_cookies(n, cache={}):

  if n < 0:
    return 0
  elif (n <= 1):
    return 1
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache:
      cache = {i: 0 for i in range(n+1)}
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')