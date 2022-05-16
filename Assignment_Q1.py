
# The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....


def fibonacci(number):
    # return 0 and 1 for first and second terms
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        # return the sum of two numbers
        return fibonacci(number - 1) + fibonacci(number - 2)
  
# read the total number of items in Fibonacci series
max_item_input = input("Enter the number of items in Fibonacci series :\n")
max_item = int(max_item_input)
  
# iterate from 1 till number of terms
for count in range(max_item):
    print(fibonacci(count), end=",")
