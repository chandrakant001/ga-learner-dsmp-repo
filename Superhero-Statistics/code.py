# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data =pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-', 'Agender',inplace=True)
gender_count = data['Gender'].value_counts()
print(gender_count)
plt.plot(gender_count)
plt.show()



# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
alignment.plot.pie(label='Character Alignment')





# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
sc = sc_df.cov()
sc_covariance = 617.49
print(sc_covariance)
sc_strength = data['Strength'].std()
sc_combat = data['Combat'].std()
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)
ic_df = data[['Intelligence','Combat']]
ic = ic_df.cov()
ic_covariance =853.42
ic_intelligence = data['Intelligence'].std()
ic_combat = data['Combat'].std()
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


# --------------
#Code starts here
total_high =data['Total'].quantile(0.99)
print(total_high)
super_best=data[data['Total'] > total_high]
super_best_names =list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig,(ax_1, ax_2, ax_3)=plt.subplots(1,3, figsize=(30,10))

data['Intelligence'].plot(kind='box', ax=ax_1,title='Intelligence')

data['Speed'].plot(kind='box', ax=ax_2,title='Speed')

data['Power'].plot(kind='box', ax=ax_3,title='Power')

 


