# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(path)
plt.hist('Rating')
data = data[data['Rating']<= 5]
print(data)
plt.hist('Rating')



#Code starts here


#Code ends here


# --------------
# code starts here

total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())
missing_data =pd.concat([total_null,percent_null],axis=1, keys=['Total','Percent'])
print(missing_data)

data =data.dropna()
total_null_1 = data.isnull().sum()
percent_null_1 = (total_null/data.isnull().count())
missing_data_1 =pd.concat([total_null_1,percent_null_1],axis=1, keys=['Total','Percent'])
print(missing_data_1)

# code ends here


# --------------
import seaborn as sns
#Code starts here
a=sns.catplot(x="Category",y="Rating",data=data, kind="box" , height = 10) 
plt.xticks(rotation=90)

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt
#Code starts here


data['Installs'] = data['Installs'].str.replace('+'  ,'')
data['Installs'] = data['Installs'].str.replace(','  ,'')
data['Installs'] = data['Installs'].astype(int)
le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
le2 = pd.get_dummies(data['Installs'])
sns.regplot(x="Installs", y="Rating" , data=data)
plt.title('Rating vs Installs [RegPlot]')
#Code ends here



# --------------
#Code starts here
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt
#Code starts here


data['Price'] = data['Price'].str.replace('$'  ,'')

data['Price'] = data['Price'].astype(float)
le = LabelEncoder()
data['Price'] = le.fit_transform(data['Price'])
le2 = pd.get_dummies(data['Price'])
sns.regplot(x="Price", y="Rating" , data=data)
plt.title('Rating vs Price [RegPlot]')


#Code ends here


# --------------

#Code starts he
data['Genres'].unique()
data['Genres']=data.Genres.str.split(";", expand = True)
gr_mean =data.groupby('Genres',as_index=False)['Rating'].mean().sort_values(['Rating'])

print(gr_mean)
#Code ends here


# --------------
from datetime import datetime
#Code starts here
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = max(data['Last Updated'])
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title('Rating vs Last Updated [RegPlot]')
#Code ends here


