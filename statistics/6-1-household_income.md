[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)


# Chapter 6 Exercise 6.1


```python
# Import Relevant Libraries
import numpy as np
import density
import hinc
from thinkstats2 import Skewness, PearsonMedianSkewness, Cdf
from hinc2 import InterpolateSample
%matplotlib inline
```


```python
# Import Data
df = hinc.ReadData()

# Preview Data
df.head()

# Make Assumptions on Upper Bound of Highest Range
upper1 = 6 # 1 Million
upper2 = 7 # 10 Million
upper3 = 8 # 100 Million
```


```python
# Create a pseudo-samples for each upper bound
pseudo_sample1 = InterpolateSample(df, log_upper=upper1)
pseudo_sample2 = InterpolateSample(df, log_upper=upper2)
pseudo_sample3 = InterpolateSample(df, log_upper=upper3)

# Since psuedo_sample is expressed in log10, convert sample back
sample_1 = np.power(10, pseudo_sample1)
sample_2 = np.power(10, pseudo_sample2)
sample_3 = np.power(10, pseudo_sample3)

# Compute CDF of each sample
cdf_1 = Cdf(sample_1)
cdf_2 = Cdf(sample_2)
cdf_3 = Cdf(sample_3)
```

```python
# Compute Mean, Median, Standard Deviation, Skewness, & Pearsons Skewness
mean1 = sample_1.mean()
mean2 = sample_2.mean()
mean3 = sample_3.mean()

median1 = cdf_1.Value(0.5)
median2 = cdf_2.Value(0.5)
median3 = cdf_3.Value(0.5)

std1 = sample_1.std()
std2 = sample_2.std()
std3 = sample_3.std()

skew1 = Skewness(sample_1)
skew2 = Skewness(sample_2)
skew3 = Skewness(sample_3)

pearson1 = PearsonMedianSkewness(sample_1)
pearson2 = PearsonMedianSkewness(sample_2)
pearson3 = PearsonMedianSkewness(sample_3)
```


```python
# Compute Fraction of Households with Income Below the Mean
frac1 = cdf_1[mean1]
frac2 = cdf_2[mean2]
frac3 = cdf_2[mean2]
```


```python
# Print Results:
print('Results with Upper Bound of One Million:')
print('Mean:',mean1)
print('Median:',median1)
print('Standard Deviation:',std1)
print('Skewness:',skew1)
print('Pearson Skewness:',pearson1)
print('Fraction of Households with Income Below Mean:',frac1)
print('------------------------------')

print('Results with Upper Bound of Ten Million:')
print('Mean:',mean2)
print('Median:',median2)
print('Standard Deviation:',std2)
print('Skewness:',skew2)
print('Pearson Skewness:',pearson2)
print('Fraction of Households with Income Below Mean:',frac2)
print('------------------------------')

print('Results with Upper Bound of Hundred Million:')
print('Mean:',mean3)
print('Median:',median3)
print('Standard Deviation:',std3)
print('Skewness:',skew3)
print('Pearson Skewness:',pearson3)
print('Fraction of Households with Income Below Mean:',frac3)
```

    Results with Upper Bound of One Million:
    Mean: 74278.7075312
    Median: 51226.4544789
    Standard Deviation: 93946.9299635
    Skewness: 4.94992024443
    Pearson Skewness: 0.736125801914
    Fraction of Households with Income Below Mean: 0.660005879567
    ------------------------------
    Results with Upper Bound of Ten Million:
    Mean: 124267.397222
    Median: 51226.4544789
    Standard Deviation: 559608.501374
    Skewness: 11.6036902675
    Pearson Skewness: 0.391564509277
    Fraction of Households with Income Below Mean: 0.856563066521
    ------------------------------
    Results with Upper Bound of Hundred Million:
    Mean: 457453.487247
    Median: 51226.4544789
    Standard Deviation: 4434938.61283
    Skewness: 14.8924598044
    Pearson Skewness: 0.274790973381
    Fraction of Households with Income Below Mean: 0.856563066521


# Results:

As expected, with a larger upper bound, the mean income increased as it got pulled in the direction of the skew. Likewise, the standard skewness & standard deviation increases since there are more values that would be considered outliers. However, the Pearson Skewness seems to decrease as the upper bound increases, showing that that the Pearson Skewness is not an appropriate indication of skewness in this example.
