# # Question 5

# Import Relevant Data
from advanced_python_regex import email_list
import csv
import pandas as pd

# Preview Data
print(email_list)

# Write Data to CSV File
file = open('email.csv', 'w')
writer = csv.writer(file)
for email in email_list:
    writer.writerow([email])