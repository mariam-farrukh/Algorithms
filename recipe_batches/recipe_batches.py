#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # similar to rps, need to set up possible batches, but don't know what will be in the batches, so this would be like the list of plays.
  # initialize possible batches
  possible_batches = []

  for item in recipe:
    # This means if we don't have the ingredient, then we just can't make the recipe
    # Need this step to pass the one at the bottom of this page where the recipe calls for more butter then what the user has.
    if item not in ingredients:
      return 0
    #If the ingredient exists, divide it by the amount needed in the recipe. If greater than 0, then we determine what is needed for the batches
    if ingredients[item] // recipe[item] > 0:
      # divide them to find the amount we need for the recipe
      possible_batches.append(ingredients[item] // recipe[item])
      # print(possible_batches)
    else:
      # Only happens when there is not enough ingredients for the recipe.
      return 0
  # print(possible_batches)
  # Need to find min value in the array to find out how many batches can be made. It is limited by the group with lowest supply of ingredients for the recipe.
  return min(possible_batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))