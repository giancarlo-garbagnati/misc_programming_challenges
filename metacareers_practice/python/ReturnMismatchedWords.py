"""
Return Mismatched Words
Given an input of two strings consisting of english letters (a-z; A-Z) and spaces, complete a function that returns a list containing all the mismatched words (case sensitive) between them.
You can assume that a word is a group of characters delimited by spaces.
A mismatched word is a word that is only in one string but not the other.
Add mismatched words from the first string before you add mismatched words from the second string in the output array.
Signature 
static String[] returnMismatched(String str1, String str2)
Input
str1: a string
str2: a string
Note: You can only expect valid english letters (a-z; A-Z) and spaces.
Output
An array containing all words that do not match between str1 and str2.
Examples
str1: "Firstly this is the first string"
str2: "Next is the second string"
output: ["Firstly", "this", "first", "Next", "second"]

str1: ""
str2: ""
output: []

str1: ""
str2: "This is the second string"
output: ["This","is","the","second","string"]

str1: "This is the first string" 
str2: "This is the second string" 
output: ["first", "second"]

str1: "This is the first string extra" 
str2: "This is the second string" 
output: ["first", "extra", "second"]

str1: "This is the first text" 
str2: "This is the second string" 
output: ["first", "text", "second", "string"]
"""

import math
# Add any extra import statements you may need here
# Add any helper functions you may need here




def return_mismatched_words(str1, str2):
  # Write your code here
  # get symmetric difference of both sets
  tokens1 = set(str1.split())
  tokens2 = set(str2.split())
  
  return list(tokens1 ^ tokens2)
    

"""
"Hi my name is Bob"
"Hello my first name is Bob. How are you?"

Sequence important strings where you'd want some sort of 
alignment algorithm (like for DNA sequencing) would need 
a different solution. For example this example would solve 
differently if order was important.
"Hi my name is Bob. How are you?"
"How are you? Hello my first name is Bob"
Since "How are you?" appears in both strings but in
different order.
"""

    
    
    
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printStringList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printStringList(expected)
    print(' Your output: ', end='')
    printStringList(output)
    print()
  test_case_number += 1
    
if __name__ == "__main__":
  # Testcase 1
  str1 = "Firstly this is the first string"
  str2 = "Next is the second string" 
  output_1 = return_mismatched_words(str1, str2)
  expected_1 = ["Firstly", "this", "first", "Next", "second"]
  check(expected_1, output_1)

  # Testcase 2
  str1 = "This is the first string"
  str2 = "This is the second string" 
  output_2 = return_mismatched_words(str1, str2)
  expected_2 = ["first", "second"]
  check(expected_2, output_2)
  
  # Testcase 3
  str1 = "This is the first string extra"
  str2 = "This is the second string" 
  output_3 = return_mismatched_words(str1, str2)
  expected_3 = ["first", "extra", "second"]
  check(expected_3, output_3)
  
  # Testcase 4
  str1 = "This is the first text"
  str2 = "This is the second string" 
  output_4 = return_mismatched_words(str1, str2)
  expected_4 = ["first", "text", "second", "string"]
  check(expected_4, output_4)
  
  
  # Add your own test cases here
