'''
1) What are my objectives?
    a) Calculate the total number of months

    b) Calculate the total net amount of "Profit/Losses"

    c) Calculate the average change in "Profit/Losses" between months

    d) Calculate the greatest increase in profits (date and amount)

    e) Calculate the greatest decrease in losses (date and amount)

2) What is my dataset?
    two columns, one with months and other with profit or loss

3) What are my variables?
    numMonths = number of number of months
    totalNet = total net amount
    avgChange = change between months (entire period)
    gInc = greatest increase in profits (entire period)
    gDec = greatest decrease in profits (entire period)

4) what are my iterations?
    a) numMonths: loop through every row and count column 1 w/o header

    b) totalNet: loop through every row and sum column 2 w/o header

    c) avgChange: ASK FOR CLARIFICATION
    start at i = 2
    (i-1(month) + i(month))/i = avg1
    then (next month)
    (avg1 + i+1(month)) / i + 1 = avg1

    d)


'''

import csv

file = open('budget_data.csv')
finData = csv.reader(file)
