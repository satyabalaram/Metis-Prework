# Import Relevant Libraries
import pandas as pd
import re

# Import Data
df = pd.read_csv('faculty.csv')

# Preview Data
print(df.head())

# # Question 1
# Create a Dictionary of Degrees & Counts
def get_degrees(dataframe):
	data = df[' degree']
	count = {}
	for degrees in data:
	    for degree in degrees.split():
	        word = re.sub(r'\.','',degree)
	        if re.match("^[A-Za-z]*$", word):
	            count[word.upper()] = count.get(word.upper(),0) +1
	return count

# Number of Unique Degrees
count = get_degrees(df)
print('Number of Unique Degrees:',len(count.keys()))

# Frequency of Each Degree
print('Frequency of Each Degree:',count)


# # Question 2
# Create a Dictionary of Titles & Counts
def get_titles(dataframe):
	titles = df[' title']
	find = re.compile(r"(\w+ \w+|\w+) (of|is)")
	title_count = {}
	for title in titles:
	    name = re.search(find, title).group(1)
	    title_count[name] = title_count.get(name,0) + 1
	return title_count
    
# Number of Unique Title
title_count = get_titles(df)
print('Number of Unique Titles:',len(title_count.keys()))

# Frequency of Each Title
print('Frequency of Each Title:',title_count)    


# # Question 3
# Create a List of Email Addresses
def get_emails(dataframe):
	emails = df[' email']
	email_list = emails.tolist()
	return email_list
# Print Email List
email_list = get_emails(df)
print(email_list)


# # Question 4
# Create a List of Each Email Domain & Filter the List for Unique Domains
def get_domains(emails):
	find = re.compile(r"([^@]*)$")
	domains = []
	for email in emails:
	    domains.append(re.search(find, email).group(0))
	return set(domains)
# Print List of Unique Email Domains
domains = get_domains(email_list)
print('Number of Unique Domains:',len(domains))
# Print List of Unique Email Domains
print('List of Unique Domains:',domains)

