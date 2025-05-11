"""
Fill in the Blanks
Given an array containing null values fill in the null values with most recent non-null value in the array.
Signature
integer[] returnFilledArray(integer[] input_lst)
Input
Array of integers and/or null values
Output
Array of integers and/or null values
Examples
input:  [1,null,2,3,null,null,5,null]
output: [1, 1, 2, 3, 3, 3, 5, 5]

input: [null,8,null]
output: [null, 8, 8]

input: [1,null,2]
output: [1,1,2]

input: [5,null,null]
output: [5,5,5]

input: [1,null,2,3,null,null,5,null]
output: [1,1,2,3,3,3,5,5]
"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def fill_in_the_blanks(input_lst):
  # Write your code here
  
  for i, val in enumerate(input_lst):
    if i == 0:
      last = val
    elif val is None:
      input_lst[i] = last
    else:
      last = val
  
  return input_lst

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
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":

  # Testcase 1
  input_lst_1 = [1,None,2,3,None,None,5,None]
  output_1 = fill_in_the_blanks(input_lst_1)
  expected_1 = [1, 1, 2, 3, 3, 3, 5, 5]
  check(expected_1, output_1)
  

  # Testcase 2
  input_lst_2 = [None, 8, None]
  output_2 = fill_in_the_blanks(input_lst_2)
  expected_2 = [None, 8, 8]
  check(expected_2, output_2)


  # Testcase 3
  input_lst_3 = [1,None,2]
  output_3 = fill_in_the_blanks(input_lst_3)
  expected_3 = [1, 1, 2]
  check(expected_3, output_3)
  

  # Testcase 4
  input_lst_4 = [5, None, None]
  output_4 = fill_in_the_blanks(input_lst_4)
  expected_4 = [5, 5, 5]
  check(expected_4, output_4)
  
  # Add your own test cases here
  
