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
columnas_eliminar = ['MarriedID', 'Sex', 'Date_of_Birth', 'Age', 'date', 'PositionID', 'MaritalStatusID']

df.drop(columnas_eliminar, axis=1, inplace=True)

#Employee_Name: separar apellido y nombre
#Gender: 0 Femenino, 1= Masculino
#TermR: 1. No estan y 0. Estan 
#EmploymentStatus: Active, Terminated for Cause,Voluntarily Terminated	
#TermReason: Cambiar a N/A-StillEmployed si el termd es 0 y EmploymentStatus = Active

# %%
df = df.drop(df.index[311:409])

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
#%%
mapa = {2.0 : 1.0}
df['EmpStatusID'] = df['EmpStatusID'].replace(mapa)

mapa_2 = {3.0 : 1.0}
df['EmpStatusID'] = df['EmpStatusID'].replace(mapa_2)

mapa_3 = {4.0 : 2.0}
df['EmpStatusID'] = df['EmpStatusID'].replace(mapa_3)

mapa_4 = {5.0 : 3.0}
df['EmpStatusID'] = df['EmpStatusID'].replace(mapa_4)

# %%
# BOD - fecha

df[['DateofHire', 'DateofTermination']] = pd.to_datetime(df[['DateofHire', 'DateofTermination']], format='%m/%d/%Y')

fecha_datetime = datetime.strptime(fecha_string, '%m/%d/%Y')