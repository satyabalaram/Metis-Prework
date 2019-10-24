# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.this is test

import pandas as pd

def min_diff():
	df = pd.read_csv('football.csv')
	df['Goal Differential'] = abs(df['Goals'] - df['Goals Allowed'])
	print(df.loc[df['Goal Differential'].idxmin()]['Team'])

min_diff()
