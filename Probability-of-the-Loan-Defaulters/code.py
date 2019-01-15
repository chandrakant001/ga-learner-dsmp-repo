# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
df1 =len(df)
p_a=(len(df[df['fico']>700]))/df1
print(round(p_a,2))
p_b=(len(df[df['purpose']=='debt_consolidation']))/df1
print(round(p_b,2))
a_b=len(df[(df['purpose']=='debt_consolidation')&(df['fico']>700)])
print(a_b)
p_a_b =a_b / df1
print(round(p_a_b,2))
result = (p_a_b == p_a)
print(result)

# code ends here


# --------------
# code starts here
df1 = len(df)
prob_lp =len(df[df['paid.back.loan'] == 'Yes'])/df1
print(round(prob_lp,2))
prob_cs = len(df[df['credit.policy'] == 'Yes'])/df1
print(prob_cs)
new_df =len(df[df['paid.back.loan']== 'Yes'])
a_b = len(df[(df['paid.back.loan'] == 'Yes')&(df['credit.policy']=='Yes')])
print(a_b)
prob_pd_cs =a_b/new_df
bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)


# code ends here


# --------------
# code starts here
df1 = df[df['paid.back.loan']== 'No']
df1.plot.bar()
plt.show()


# code ends here


# --------------
# code starts here
inst_median =df['installment'].median()
inst_mean =df['installment'].mean()
df['installment'].plot.hist()
df['log.annual.inc'].plot.hist()




# code ends here


