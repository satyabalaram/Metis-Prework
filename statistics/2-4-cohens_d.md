[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> **Exercise 2.4**
Using the variable **totalwgt_lb**, investigate whether first babies are lighter or heavier than others. Compute Cohen's d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

**Solution**

The exercise asks to compare the weight of first babies from other babies. To do so, we must first import the pregnancy data.

```python
# Import relevant libraries
import nsfg
import first
from math import sqrt

# Load Pregnancy Data & Create Dataframes
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

# Alternatively
live, firsts, others = first.MakeFrames()
```

Compute the mean & variance of each dataframe. Compare the mean weight of first & other babies by taking the simple difference. Examine the effect size via Cohen's d & the difference relative to the total mean.

```python
# Compute the Mean
mean_live = live['totalwgt_lb'].mean()
mean_firsts = firsts['totalwgt_lb'].mean()
mean_others = others['totalwgt_lb'].mean()

# Compute the Variance
var_live = live['totalwgt_lb'].var()
var_firsts = firsts['totalwgt_lb'].var()
var_others = others['totalwgt_lb'].var()

# Compute the difference
diff_lb = mean_firsts - mean_others

# Compute the difference relative to the mean
diff_rel = diff_lb / mean_live

# Compute Cohen's d
cohens_d = (diff_lb) / sqrt(var_live)
```
**Results**  
Total Mean: 7.265628457623368  
Firsts Mean: 7.201094430437772  
Others Mean: 7.325855614973262  
Total Variance: 1.9832904288326532  
Firsts Variance: 2.0180273009157768  
Others Variance: 1.9437810258964572  
Difference in Weight: -0.12476118453549034  
Difference Relative to Mean: -0.017171423678372415  
Cohens d: -0.0885903324538168

The difference in the mean weights of first babies & other babies was -0.125 lb or -2 oz. Relative to the total mean, this difference is only 1.7%. Furthermore, the value of Cohen's d shows that the difference in means is 0.09 standard deviations. In comparison to the difference in pregnancy length computed by the author in the text (Difference = 0.078 Weeks, Difference Relative to Mean = 0.2%, Cohen's d = 0.029), the difference in the weights is slightly more significant. However, the difference in the weights of first babies & other babies are small enough to be considered clinically insignificant. 
