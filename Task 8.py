"""
Task 8
write a complete python program that does the following:
1. asks the user to enter an integer n that is between 1 and 9
2. repeatedly reads n from the user until the supplied value of n is legal
3. prints out a picture of a triangle with n rows, in which the symbol used to print each row is the row's number.

"""

n = int(input("Enter an integer between 1 and 9: "))

while n < 1 or n > 9:
    n = int(input("Please enter a valid integer between 1 and 9: "))

for i in range(1, n + 1):
    print(str(i) * i)
