# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> **Similarities:**
>> Both lists & tuples store a sequence of elements

>> **Differences:**
>> Lists are mutable; Tuples are immutable

>> Tuples may work as keys in dictionaries since they are immutable

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> **Similarities:**
>> Both lists & sets store a sequence of elements

>> **Differences:**
>> Sets cannot contain duplicates; Lists can contain duplicates
>> Sets are unordered; Lists are ordered
>> Sets can use the operations: `union`, `intersection`, `difference`, `symmetric difference`

```python
ex_list = ['m','e','t','i','s']
ex_set = set(['m','e','t','i','s'])

word = ''
for letter in ex_list:
    word += letter
print(word)
>> metis

print('m' in ex_set)
>> True
```

>> Sets are significantly faster when determining if an object is present in the sequence because sets use a hash function to map the data. However, lists are faster when iterating over the values of the sequence.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is essentially an anonymous function that is used to create function expressions in places where `def` is not allowed by Python's syntax.

```python
# Example 1
a = [1, 2, 3]
square = map(lambda x: x**2, a)
list(square)
>> [1, 4, 9]

# Example 2
b = [(3, -2), (1, -1), (2, -3)]
sorted(b)
>> [(1, -1), (2, -3), (3, -2)]
sorted(b, key=lambda x: x[1])
>> [(2, -3), (3, -2), (1, -1)]
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are simply a pythonic way of transforming a list. The capabilities are similar although list comprehension is preferred since it is more readable & usually faster. However, `map` may be faster when calling an already defined function.

```python
# Example 1 - List of odd numbers between 1 & 10
# List Comprehension
odds_squared = [x**2 for x in range(10) if x%2 == 1]
odds_squared
>> [1, 9, 25, 49, 81]
# Map & Filter
odds_squared = map(lambda x: x**2, filter(lambda x: x%2==1, range(10)))
list(odds_squared)
>> [1, 9, 25, 49, 81]

# Example 2 - Set Comprehension (Python 3)
a = [1, 1, 2, 2, 3, 3]
{x*2 for x in a}
>> {2, 4, 6}

# Example 3 - Dictionary Comprehension
a = ['a','b','c','d']
{key: value for (key,value) in zip(a, range(4))}
>> {'a': 0, 'b': 1, 'c': 2, 'd': 3}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

>> See python file for solution

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

>> See python file for solution

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
