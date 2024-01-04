#%%
import pandas as pd
import datetime
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
df = df.drop(df.index[311:410])
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
df['DateofHire'] = pd.to_datetime(df['DateofHire'], format='%m/%d/%Y')
#%%
df['DateofTermination'] =pd.to_datetime(df['DateofTermination'],format='%m/%d/%Y' )

# %%
df['DOB']=pd.to_datetime(pd.to_datetime(df['DOB'],format='%m/%d/%y' ))

#%%
#Agregamos la columna de Edad
df['Age'] = 2023 - df['DOB'].dt.year
# %%
#Codigo para calcular la fecha correcta en DOB
df['DOB'] = df['DOB'].apply(lambda x: x.replace (year=x.year - 100) if x.year > 2000 else x)
# %%
