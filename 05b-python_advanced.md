## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference.

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

---

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> **Solution:**  
Number of Unique Degrees: 8  
Frequency of Each Degree: {'BSED': 1, 'SCD': 6, 'MD': 1, 'MPH': 2, 'MA': 1, 'PHD': 31, 'MS': 2, 'JD': 1}

```python
# Import Relevant Libraries
import pandas as pd
import re

# Import Data
df = pd.read_csv('faculty.csv')

# Preview Data
df.head()

# Create a Dictionary of Degrees & Counts
data = df[' degree']
count = {}
for degrees in data:
    for degree in degrees.split():
        word = re.sub(r'\.','',degree)
        if re.match("^[A-Za-z]*$", word):
            count[word.upper()] = count.get(word.upper(),0) +1

# Number of Unique Degrees
print('Number of Unique Degrees:',len(count.keys()))

# Frequency of Each Degree
print('Frequency of Each Degree:',count)
```


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> **Solution**  
Number of Unique Titles: 3  
Frequency of Each Title: {'Associate Professor': 12, 'Assistant Professor': 12, 'Professor': 13}

```python
# Create a Dictionary of Degrees & Counts
titles = df[' title']
find = re.compile(r"(\w+ \w+|\w+) (of|is)")
title_count = {}
for title in titles:
    name = re.search(find, title).group(1)
    title_count[name] = title_count.get(name,0) + 1

# Number of Unique Title
print('Number of Unique Titles:',len(title_count.keys()))

# Frequency of Each Title
print('Frequency of Each Title:',title_count)    
```


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> **Solution**  
['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']

```python
# Create a List of Email Addresses
emails = df[' email']
email_list = emails.tolist()
print(email_list)
```


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> **Solution**  
Number of Unique Domains: 4  
List of Unique Domains: {'upenn.edu', 'cceb.med.upenn.edu', 'email.chop.edu', 'mail.med.upenn.edu'}

```python
# Create a List of Each Email Domain
find = re.compile(r"([^@]*)$")
domains = []
for email in emails:
    domains.append(re.search(find, email).group(0))

# Number of Unique Title
print('Number of Unique Domains:',len(set(domains)))

# Filter the List for Unique Domains
print('List of Unique Domains:',set(domains))
```

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

>> See Python Code or iPython Notebook for Solution

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

>> **Solution**  
Ellenberg [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']]  
Li [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]

```python
for key, value in faculty_dict.items():
    print(key,value)
```

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>> **Solution**  
('Hongzhe', 'Li') ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']  
('Jonas', 'Ellenberg') ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']  
('Mingyao', 'Li') ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu']

```python
# Output the Key-Value Pairs Based on First Name of Professors
num = 0
for key in sorted(professor_dict):
    if num < 3:
        print (key, professor_dict[key])
        num+=1
```

####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>> **Solution**  
('Susan', 'Ellenberg') ['Ph.D.', 'Professor', 'sellenbe@upenn.edu']  
('Jonas', 'Ellenberg') ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']  
('Hongzhe', 'Li') ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']

```python
# Output the Key-Value Pairs Based on Last Name of Professors
num = 0
for key in sorted(professor_dict,key=lambda x:x[1]):
    if num < 3:
        print (key, professor_dict[key])
        num+=1
```

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

---

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)
