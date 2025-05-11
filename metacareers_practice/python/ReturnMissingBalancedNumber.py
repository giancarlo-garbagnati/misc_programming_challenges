"""
Return Missing Balanced Numbers
A balanced array would be an array in which each element appears the same number of times.
Given an array with n elements, return a dictionary with the key as the element and the value as the count of elements needed to balance the given array.
Signature 
HashMap<Object, Integer> returnMissingBalancedNumbers(Object[] elements)
Input 
Array of mixed elements (integers, strings, etc.)
Output
Object with a mixed key, and an integer value
Examples
elements: ["a", "b", "abc", "c", "a"]
output: {"b":1, "abc":1, "c":1}

elements: [1,3,4,2,1,4,1]
output: {2:2, 3:2, 4:1}

elements: [4,5,11,5,6,11]
output: {4:1,6:1}
"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def return_missing_balanced_numbers(input):
  # Write your code here
  
  array_count = {}
  highest_freq = 0
  
  for e in input:
    if e in array_count:
      array_count[e] += 1
    else:
      array_count[e] = 1
    if array_count[e] > highest_freq:
      highest_freq = array_count[e]
  
  missing_array = {}
  for k,v in array_count.items():
    if v < highest_freq:
      missing_array[k] = highest_freq - v
  
  return missing_array
  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    print(expected)
    print(' Your output: ', end='')
    print(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  
  # Testcase 1 
  input_1 = ['a','b','abc','c','a']
  output_1 = return_missing_balanced_numbers(input_1)
  expected_1 = {'b':1,'abc':1,'c':1}
  check(expected_1, output_1)

  # Testcase 2 
  input_2 = [1,3,4,2,1,4,1]
  output_2 = return_missing_balanced_numbers(input_2)
  expected_2 = {2:2,3:2,4:1}
  check(expected_2, output_2) 
  
  # Testcase 3
  input_3 = [4,5,11,5,6,11]
  output_3 = return_missing_balanced_numbers(input_3)
  expected_3 = {4:1,6:1}
  check(expected_3, output_3)
  
  # Add your own test cases here
  
