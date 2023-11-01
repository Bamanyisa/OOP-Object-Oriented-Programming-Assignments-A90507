"""
Task 7
Jane owns a money lending busineess called Save to grow credit that loans out money. 
A given client of this company is given a loan that has to be repaid in a month's time.(30 days) or less days with 10% interest. 
If the client fails to pay at the end of the 30 days, the client is charged a fine of 1% of the loan per day. 
Write a python application taht determines the total amount that is paid by the client to the company after a given number of days.

"""

class Loan:
    def __init__(self, principal, interest_rate=0.10):
        self.principal = principal
        self.interest_rate = interest_rate

    def calculate_total_amount(self, days):
        if days <= 30:
            total_amount = self.principal * (1 + self.interest_rate)
        else:
            extra_days = days - 30
            total_amount = self.principal * (1 + self.interest_rate + (0.01 * extra_days))
        return total_amount

principal = float(input("Enter the loan amount: $"))
days = int(input("Enter the number of days: "))

loan = Loan(principal)

total_amount = loan.calculate_total_amount(days)

print(f"Total amount to be paid after {days} days: ${total_amount:.2f}")
