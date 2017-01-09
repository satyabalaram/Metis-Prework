# # Question 6
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}

for key, value in faculty_dict.items():
    print(key,value)              

# # Question 7
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], 
                  ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], 
                  ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], 
                  ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], 
                  ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }

# Output the Key-Value Pairs in Dict
# Note: Dict does not remember the order of added elements
num = 0
for key, value in professor_dict.items():
    if num < 3:
        print(key,value)
        num+=1

# Output the Key-Value Pairs Based on First Name of Professors
num = 0 
for key in sorted(professor_dict):
    if num < 3:
        print (key, professor_dict[key])
        num+=1

# # Question 8
# Output the Key-Value Pairs Based on Last Name of Professors
num = 0 
for key in sorted(professor_dict,key=lambda x:x[1]):
    if num < 3:
        print (key, professor_dict[key])
        num+=1