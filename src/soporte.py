#%%
import pandas as pd
pd.set_option('display.max_columns', None)

# %%
df= pd.read_csv("../ficheros/recursos-humanos.csv", index_col=0)
# %%
df.shape
#%%
df.info()
# %%
df.duplicated().sum()
# %%
df.head(10)
#%%
df[['MaritalDesc', 'MaritalStatusID','MarriedID']]
# %%
columnas_eliminar = ['MarriedID','Sex']
#Employee_Name: separar apellido y nombre
#Gender: 0 Femenino, 1= Masculino
#EmpStatusID: 1, 2, 3 = Active
# 4 = Terminated for Cause
# 5= Voluntarily Terminated
#TermR: 1. No estan y 0. Estan 
#EmploymentStatus: Active, Terminated for Cause,Voluntarily Terminated	
#TermReason: 
#%%
df[['Sex', 'GenderID','Employee_Name'	]].head(20)
# %%
df['EmploymentStatus'].value_counts()
#%%
df[['EmploymentStatus', 'EmpStatusID', 'Employee_Name']].sample(10)
# %%
df['EmpStatusID'].value_counts()
#%%
df[df['Employee_Name'] =='Goyal, Roxana']

# %%
df['TermReason'].value_counts()
#%%
df[['TermReason','EmploymentStatus','Termd', 'EmpStatusID']].sample(20)
# %%
#Data frame correspondiente para cambiar TermReason a Still Employed
df[df['Termd'] == 0.0][df['TermReason']!= 'N/A-StillEmployed']
# %%
