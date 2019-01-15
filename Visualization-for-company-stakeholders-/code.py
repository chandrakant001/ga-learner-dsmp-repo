# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv(path)
loan_status =data['Loan_Status'].value_counts()
print(loan_status)
plt.plot(loan_status)
plt.show()

#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
print(property_and_loan)
plt.plot(property_and_loan)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
plt.plot(education_and_loan)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here

graduate=data[data['Education'] == 'Graduate']
not_graduate=data[data['Education'] == 'Not Graduate']
graduate.plot(kind='density',label='Graduate')
not_graduate.plot(kind='density',label='Not Graduate')









#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(20,10))
applicantincome=data[['ApplicantIncome','LoanAmount']]
applicantincome.plot(kind='scatter',x='ApplicantIncome',y='LoanAmount',ax=ax_1)
ax_1.set_title('Applicant Income')
coapplicantincome=data[['CoapplicantIncome','LoanAmount']]
coapplicantincome.plot(kind='scatter',x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
ax_2.set_title('Coapplicant Income')
data['TotalIncome']=data['CoapplicantIncome']+data['ApplicantIncome']
totalincome=data[['TotalIncome','LoanAmount']]
totalincome.plot(kind='scatter',x='TotalIncome',y='LoanAmount',ax=ax_3)
ax_3.set_title('Total Income')


