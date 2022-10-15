#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    counter = 0
    patron = "SOS"
    x = re.findall('...', s)
    result = [[*word] for word in x if  word != patron]
    for singleList in result:
        if singleList[0] != 'S':
            counter += 1
        if singleList[1] != 'O':
            counter += 1
        if singleList[2] != 'S':
            counter += 1
        print(singleList)
            
            
    return counter
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()


# A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
# Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of the SOS message have been changed by radiation.
# Example
# The original message was SOSSOS. Two of the message's characters were changed in transit.
# Function Description
# Complete the marsExploration function in the editor below.
# marsExploration has the following parameter(s):
# string s: the string as received on Earth
# Returns
# int: the number of letters changed during transmission
# Input Format
# There is one line of input: a single string, .
# Constraints
#  will contain only uppercase English letters, ascii[A-Z].
# Explanation
# Sample 0
#  = SOSSPSSQSSOR, and signal length . Sami sent  SOS messages (i.e.: ).
# Expected signal: SOSSOSSOSSOS
# Recieved signal: SOSSPSSQSSOR
# We print the number of changed letters, which is .
# Sample 1

#  = SOSSOT, and signal length . Sami sent  SOS messages (i.e.: ).

# Expected Signal: SOSSOS
# Received Signal: SOSSOT

# We print the number of changed letters, which is .