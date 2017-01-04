# Hint:  use Google to find python function

from datetime import datetime

def num_days(d1, d2, format):
	start = datetime.strptime(d1, format)
	end = datetime.strptime(d2, format)
	return (end - start).days

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
format = '%m-%d-%Y'
days = num_days(date_start, date_stop, format)
print(days)


####b)  
date_start = '12312013'  
date_stop = '05282015'  
format = '%m%d%Y'
days = num_days(date_start, date_stop, format)
print(days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
format = '%d-%b-%Y'
days = num_days(date_start, date_stop, format)
print(days)
