"""
Task 4
Write a Fraction class to represent rational numbers like 1/2 and -3/8.

"""

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


fraction1 = Fraction(1, 2)
fraction2 = Fraction(-3, 8)

print("Fraction 1:", fraction1)
print("Fraction 2:", fraction2)

