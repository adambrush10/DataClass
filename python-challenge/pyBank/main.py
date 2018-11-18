

import pandas as pd
import numpy as np

file = ("/Users/Brush/PycharmProjects/python-challenge/pyBank/Homeworks_HW03-Python_PyBank_Resources_budget_data.csv")

PYbank_pd = pd.read_csv(file)


#print(PYbank_pd)

# total number of months in the dataset

month_count = PYbank_pd['Date'].count()

# total net amount of "Profit/Losses" over the entire period
sum_count = PYbank_pd['Profit/Losses'].sum()

# average change in "Profit/Losses" between months over the entire period

Profit_Losses = PYbank_pd['Profit/Losses']

x = 0
y = 1
change_list = []

while x < 85:
    month1 = PYbank_pd.iloc[x, 1]
    # print(month1)

    month2 = PYbank_pd.iloc[y, 1]
    # print(month2)
    x += 1
    y += 1
    # print(month2 - month1)
    change = month2 - month1
    change_list.append(change)
#print(change_list)

# print(sum(change_list))
# print(len(change_list))

avg = sum(change_list) / len(change_list)

# print(avg)







# greatest increase in profits (date and amount) over the entire period

max = max(change_list)
min = min(change_list)

# greatest decrease in losses (date and amount) over the entire period


file = open(“financial_analysis.txt”, ”w”)

file.write("hey ")

print('Financial Analysis')
print('-------------------------------')
print(f'Total Months : {month_count}')
print(f'Net Profit   : {sum_count}')
print(f'Average Change: {avg}')
print(f'Greatest Increase in Profits: {max}')
print(f'Greatest Decrease in Profits: {min}')


