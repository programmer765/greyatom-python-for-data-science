# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 




# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = pd.DataFrame(bank)
banks.drop(['Loan_ID'],inplace=True,axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode()
print(bank_mode)
print(banks.head(12))
banks = banks.fillna(bank_mode)
banks['Self_Employed'] = banks['Self_Employed'].fillna('No')
banks['Gender'] = banks['Gender'].fillna('Male') 
banks['Dependents'] = banks['Dependents'].fillna('0')
banks['LoanAmount'] = banks['LoanAmount'].fillna('120.0')
banks['Credit_History'] = banks['Credit_History'].fillna('1.0')
banks['Loan_Amount_Term'] = banks['Loan_Amount_Term'].fillna('360.0')
banks['Married'] = banks['Married'].fillna('Yes')
print(banks.isnull().sum())
banks.isnull()
#print(banks.head(12))
#code ends here


# --------------
# Code starts here
avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here

loan_approved_se = len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])
print(loan_approved_se)
loan_approved_nse = len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])
print(loan_approved_nse)
percentage_se = (loan_approved_se/614)*100
percentage_nse = (loan_approved_nse/614)*100
print(percentage_se,percentage_nse)
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
print(loan_term)
big_loan_term = len(loan_term[loan_term >= 25])
print(big_loan_term)


# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
mean_values = loan_groupby.mean()

# code ends here


