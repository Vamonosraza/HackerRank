# Task 
# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i[square].
# Example 

# The list of non-negative integers that are less than  n=3 is [0,1,2]. Print the square of each number on a separate line.

if __name__ == '__main__':
    n = int(input())
    for i in range (0,n,):
        print(i**2)
# -------------------------

# Build a Function

# #Task
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to 
# complete the is_leap function.


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year %4 == 0 and (year%100 != 0 or year % 400==0):
        return True
    return leap

year = int(input())
print(is_leap(2000))

# For the learners: you should know that doing something like the setup for this challenge inclines you to do is a bad practice. Never do the following:
# def f():
# 	if condition:
#     	return True
#     else:
#     	return False
# This is just dumb. You are returning a boolean, so why even use if blocks in the first place? The correct what of doing this would be:
# def f():
# 	return condition
# Because this already evaluates as a boolean.
# So in this challenge, forget about ifs and elses, and that leap variable, and just do the following:
# def is_leap(year):
#     return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
# --------------------------  