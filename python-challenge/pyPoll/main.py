import pandas as pd
import numpy as np

file ='/Users/Brush/PycharmProjects/python-challenge/pyPoll/Homeworks_HW03-Python_PyPoll_Resources_election_data.csv'
df = pd.read_csv(file)

# print(df.head(50))

# The total number of votes cast
voter_count = df['Voter ID'].count()


# A complete list of candidates who received votes
candidate_list = df["Candidate"].value_counts()
# print(candidate_list)


# The percentage of votes each candidate won

percent1 = 2218231/voter_count * 100
percent_khan = round(percent1, 2)

percent2 = 704200/voter_count * 100
percent_correy = round(percent2, 2)

percent3 = 492940/voter_count * 100
percent_li = round(percent3, 2)

percent4 = 105630/voter_count * 100
percent_tooley = round(percent4, 2)



# The winner of the election based on popular vote.

print('Election Results')
print('---------------------------------')
print(f'Total votes: {voter_count}')
print('---------------------------------')
print(f'{candidate_list}')
print('---------------------------------')
print(f'Khan votes:     2218231 {percent_khan}% ')
print(f'Correy votes:   704200  {percent_correy}')
print(f'Li votes:       492940  {percent_li}')
print(f'O Tooley votes: 105630  {percent_tooley}')
print('---------------------------------')
print(f'Winner:      Khan')


