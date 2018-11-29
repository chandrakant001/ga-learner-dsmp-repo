# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)

booleans = []
for length in loan_term:
     if length>=25:
         booleans.append(True)
     else:
          booleans.append(False)

big_loan = pd.Series(booleans)          
big_loan_ = banks[big_loan] 
big_loan_term = len(big_loan_['Loan_Amount_Term'])
print(big_loan_term)



# code ends here


# --------------
# code ends here
loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)




# code ends here



# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank=pd.DataFrame(pd.read_csv(path))
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)
# code ends here


# --------------
# Code starts here
avg_loan_amount= banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)

print(avg_loan_amount)
print(bank)

# code ends here



# --------------
# code starts here
banks = bank.drop('Loan_ID',axis=1)
null=bank.isnull().sum()
print(null)

bank_mode = banks.mode()
banks = banks.fillna(value='bank_mode')
print(banks)


#code ends here


# --------------
# code starts here
loan_approved =banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_se = len(loan_approved[['Self_Employed','Loan_Status']]) 
print(loan_approved_se)
Loan_Status = 614
percentage_se = (loan_approved_se/Loan_Status)*100
print(percentage_se)

loan_unapproved = banks[(banks['Self_Employed'] == 'No' ) & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = len(loan_unapproved[['Self_Employed','Loan_Status']])
Loan_Status =  614
percentage_nse = (loan_approved_nse/Loan_Status)*100
print(percentage_nse)

# code ends here


