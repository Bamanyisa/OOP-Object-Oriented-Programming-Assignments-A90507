"""
Task 3
Write a procedural python program that calculates the average of numbers between 1 to 50 and display the results. 
Rewrite the program and convert it into an object-oriented version.

"""
# Procedural Program

total = 0
count = 0
for num in range(1, 51):
    total += num
    count += 1

average = total / count
print("Procedural Average:", average)

#Object-Oriented Program

class NumberCalculator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def calculate_average(self):
        total = sum(range(self.start, self.end + 1))
        count = self.end - self.start + 1
        return total / count

calculator = NumberCalculator(1, 50)
average = calculator.calculate_average()
print("Object-Oriented Average:", average)
