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
    gIncMonth = month of greatest inc
    gDec = greatest decrease in profits (entire period)
    gDecMonth = month of greatest dec

4) what are my iterations?
    a) numMonths: loop through every row and count column 1 w/o header

    b) totalNet: loop through every row and sum column 2 w/o header

    c) avgChange: next month minus this month,
    then average all the months

    #for next two create list of list (all info)
    d) gInc: start at first month
        set greatest increase to zero (initially)
        if next month is greater than first month:
            set gInc to next month

Steps:
1) first read in the file
2) Month count: plus 1 every read row
3) Total P/L: add all the amounts in column 2
4) Average Monthly Change:
    1) extract all the amounts in column 2 to a list
    2) subtract the 2nd element from the 1st element, add total to new list
    3) take average of new list
'''
import csv

#function definitions
def MonthlyChange(array):
    newArr = []
    for i in range(1,len(array)):
        diff = array[i] - array[i-1]
        newArr.append(diff)

    average = sum(newArr) / len(newArr)
    return average

def GreatestInc(array):
    gInc = 0
    gIncMonth = ""
    for each in array:
        if each[1] > gInc:
            gInc = each[1]
            gIncMonth = each[0]

    return str(gInc) + ' ' + gIncMonth

def GreatestDec(array):
    gDec = 0
    gDecMonth = ""
    for each in array:
        if each[1] < gDec:
            gDec = each[1]
            gDecMonth = each[0]

    return str(gDec) + ' ' + gDecMonth

#open file
bd_csv = 'budget_data.csv'

with open(bd_csv,newline='') as csvfile:
    budget_data = csv.reader(csvfile,delimiter=',')

    budget_header = next(budget_data)

    #variables
    mCount = 0
    netPL = 0
    monthlyPL = []
    changeAmt = 0
    month_PL = []

    for row in budget_data:

        #numMonths
        mCount += 1
        #net Profit/Loss
        netPL += int(row[1])
        #monthly Profit/Loss to list
        monthlyPL.append(int(row[1]))
        #all information
        month_PL.append([row[0],int(row[1])])

    #print(mCount)
    #print(netPL)
    #print(MonthlyChange(monthlyPL)) #ask about floating point formatting
    average_change = MonthlyChange(monthlyPL)
    #print(GreatestInc(month_PL))
    greatest_increase = GreatestInc(month_PL)
    #print(GreatestDec(month_PL))
    greatest_decrease = GreatestDec(month_PL)

    text1 = '''
    Financial Analysis
    ----------------------------
    Total Months: {} Months'''.format(mCount)
    text2 = '''
    Total Profit/Loss: ${} '''.format(netPL)
    text3 = '''
    Average  Change: ${} '''.format(average_change)
    text4 = '''
    Greatest Increase in Profits: ${} '''.format(greatest_increase)
    text5 = '''
    Greatest Decrease in Profits: ${} '''.format(greatest_decrease)

    print(text1)
    print(text2)
    print(text3)
    print(text4)
    print(text5)

    #output file
    output_file = open('financial_results.txt', 'w')

    output_file.write(text1)
    output_file.write(text2)
    output_file.write(text3)
    output_file.write(text4)
    output_file.write(text5)

    output_file.close()
