# tipCalculator.py
#
# Python Bootcamp Day 2 - Tip Calculator
# Usage:
#      Allow friends to split a bill and calculate tip
#
# Marceia Egler Sept 22, 2021

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")
percent_tip = input("What percentage would you like to give? 10, 12, or 15?")
bill_split = input("How many people split the bill?")

total_as_int = int(total_bill)
percent_as_float = 1 + (int(percent_tip)/100)
split_as_int = int(bill_split)

total = (total_as_int * percent_as_float / split_as_int)
total_two_places = round(total, 2)
print(f"Each person should pay ${total_two_places}.")



