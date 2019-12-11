#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  list_of_plays = []
  possible_moves = ['rock', 'paper', 'scissors']

  def rps_plays(moves, n):
    if n > 0:
      # will loop through and add the possible move to the moves that are done each time.
      for i in range(len(possible_moves)):
        rps_plays(moves + [possible_moves[i]], n-1)
    elif n == 0:
      # This will append whatever moves they want set to n = 0
      return list_of_plays.append(moves)

  if n > 0:
    rps_plays([], n)
    return list_of_plays
  elif n == 0:
    return [[]]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')