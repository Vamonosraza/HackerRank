
# Task 
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird


#!/bin/python3

import math
import os
import random
import re
import sys

n=20

# if __name__ == '__main__':
#     n = int(input().strip())

n=5

if n%2 == 0 and n < 6 or n>20:
    print("Not weird")
else:
    print("Weird")

print(n)