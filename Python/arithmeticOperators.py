# #Task 
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example 
 

# Print the following:
# 8
# -2
# 15

if __name__ == '__main__':
    # if name == 'something' : print("something") else: print("nothing")
    # only prints out if the file name is '__main__' (True), otherwise it is False
    a = int(input())
    b = int(input())
      
    print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))

    Python format() function has been introduced for handling complex string formatting more efficiently. This method of the built-in string class provides functionality for complex variable substitutions and value formatting. This new formatting technique is regarded as more elegant. The general syntax of format() method is string.format(var1, var2,…)