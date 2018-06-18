'''
1) What are my objectives?
    a) calculate total number of votes cast
    b) list of all candidates w/ percentage votes and total votes
    c) winner of the election (based on total votes)

2) What is my dataset? Voter ID, County, Candidate

3) What are my variables?

4) What are my iterations?
'''

import csv

#function definitions
def CandidateVotes(array):
    cCount = 0
    kCount = 0
    lCount = 0
    oCount = 0

    for each in array:
        if each == "Correy":
            cCount += 1
        elif each == "Khan":
            kCount += 1
        elif each == "Li":
            lCount += 1
        else:
            oCount += 1

    return [cCount, kCount, lCount, oCount]

def CandidatePercentage(sumVotes, CanVotes):
    percentages = []
    for each in CanVotes:
        percentages.append(round(each/sumVotes*100,2))
    return percentages

#takes in finalArray [[name, votes, %]]
def ElectionWinner(array):
    votes = 0
    winner = ""
    for each in array:
        if each[1] > votes:
            votes = each[1]
            winner = each[0]
    return winner

def Formatting(array):
    formArr = []
    for each in array:
        formArr.append(each[0] + ":" + " " + str(each[2]) + "%" + " " + "(" + str(each[1]) + ")")
    return formArr

#open file
file = 'election_data.csv'

with open(file, newline='') as csvfile:

    vResults = csv.reader(csvfile,delimiter=',')

    header = next(vResults)

    #variables
    vCount = 0
    candidates = []
    u_candidates = []

    for row in vResults:

        #total votes
        vCount += 1
        #all candidates
        candidates.append(row[2])

    #array of unique candidates sorted
    u_candidates = sorted(list(set(candidates)))
    #array of votes sorted by candidate (same order as u_candidates)
    u_votes = CandidateVotes(candidates)
    #array of percentages sorted by candidate(same order as u_candidates)
    u_percents = CandidatePercentage(vCount, u_votes)
    #combo array of all by candidate
    finalList = [list(each) for each in zip(u_candidates, u_votes, u_percents)]
    #winner of election by votes
    eWinner = ElectionWinner(finalList)

    text1 = '''Election Results
-------------------------
Total Votes: {} '''.format(vCount)
    text2 = '''-------------------------'''
    text3 = Formatting(finalList)
    text4 = '''-------------------------'''
    text5 = '''Winner: {} '''.format(eWinner)

    print(text1)
    print(text2)
    print(text3[0])
    print(text3[1])
    print(text3[2])
    print(text3[3])
    print(text4)
    print(text5)

    #output file
    output_file = open('Election_Results.txt', 'w')

    output_file.write(text1)
    output_file.write(text2)
    output_file.write(text3[0])
    output_file.write(text3[1])
    output_file.write(text3[2])
    output_file.write(text3[3])
    output_file.write(text4)
    output_file.write(text5)

    output_file.close()
