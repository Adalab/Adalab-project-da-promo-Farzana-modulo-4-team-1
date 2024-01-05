#%%
import pandas as pd
import datetime
pd.set_option('display.max_columns', None)

# %%
df= pd.read_csv("../ficheros/recursos-humanos.csv", index_col=0)
print('Leemos csv')
# %%
def exploracion_dataframe(dataframe):

    print(f"Los duplicados que tenemos en el conjunto de datos son: {dataframe.duplicated().sum()}")
    print("\n ..................... \n")
    # generamos un DataFrame para los valores nulos
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["%_nulos"])
    print(df_nulos[df_nulos["%_nulos"] > 0])
    
    print("\n ..................... \n")
    print(f"Los tipos de las columnas son:")
    print(pd.DataFrame(dataframe.dtypes, columns = ["tipo_dato"]))
    
    
    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    
    for col in dataframe_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valores únicos:")
        print(pd.DataFrame(dataframe[col].value_counts()).head()) 
 
    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas númericas son: ")
    dataframe_numericas = dataframe.select_dtypes(exclude = "O")
    
    for col in dataframe_numericas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valores únicos:")
        print(pd.DataFrame(dataframe[col].value_counts()).head())    
#%%
exploracion_dataframe(df)   
# %%
def columnas_eliminar ():
    columnas_eliminar = ['MarriedID', 'Sex', 'Date_of_Birth', 'Age', 'date', 'PositionID', 'MaritalStatusID','Remuneration']
    df.drop(columnas_eliminar, axis=1, inplace=True)
    
#%%
columnas_eliminar()
print('Llamamos a la función para eliminar columnas')
# %%
df = df.drop(df.index[311:410])
print('Eliminamos los valores nulos desde la fila 311 a la 409')
#%%
def reemplazo_valores(columna):
    mapa = {2.0 : 1.0}
    df[columna] = df[columna].replace(mapa)

    mapa_2 = {3.0 : 1.0}
    df[columna] = df[columna].replace(mapa_2)

    mapa_3 = {4.0 : 2.0}
    df[columna] = df[columna].replace(mapa_3)

    mapa_4 = {5.0 : 3.0}
    df[columna] = df[columna].replace(mapa_4)
#%%
reemplazo_valores('EmpStatusID')
print('Unificamos los valores de la columna para que nos queden 3 categorias')
# %%
def cambio_formato_fecha (columna_1, columna_2, columna_3):

    df[columna_1] = pd.to_datetime(df[columna_1], format='%m/%d/%Y')
    df[columna_2] =pd.to_datetime(df[columna_2],format='%m/%d/%Y' )
    df[columna_3]=pd.to_datetime(pd.to_datetime(df[columna_3],format='%m/%d/%y' ))

# %%
cambio_formato_fecha('DateofHire','DateofTermination','DOB' )
print('Cambiamos el formato de object a fecha en las tres columnas')
#%%
df['DOB'] = df['DOB'].apply(lambda x: x.replace (year=x.year - 100) if x.year > 2000 else x)
print('Arreglamos algunos valores de fechas en la columna DOB')
#Agregamos la columna de Edad
#%%
df['Age'] = 2023 - df['DOB'].dt.year
print('Agregamos la columna Age calculada con la columna DOB')
# %%
#Pasar a int
#EmpID,GenderID, EmpStatusID ,DeptID,Termd, Zip,EmpSatisfaction,SpecialProjectsCount, Absences   
#%%
lista_columnas = ['EmpID','GenderID','EmpStatusID','DeptID','Termd','Zip','EmpSatisfaction', 'Absences']
for columna in lista_columnas:
    df[columna]= df[columna].astype(int)    
print ('Conversión de tipo float a enteros')

#%%
#Employee_Name: separar apellido y nombre
#Separe el apellido del nombre e hice un df nuevo y luego concatene ambos df
df_nombres = df["Employee_Name"].str.split(",", expand=True)
df_nombres.columns = ['Last_name', 'First_name']
df = pd.concat([df, df_nombres], axis=1)
print('Mostramos dataframe con nuevas columnas')
#%%
df.drop('Employee_Name',  axis=1, inplace=True)
print('Eliminamos la columna Employee_Name')
#%%
#reordeno las columnas 
df=df.reindex(['Last_name','First_name','EmpID', 'GenderID', 'EmpStatusID', 'DeptID', 'PerfScoreID',
       'FromDiversityJobFairID', 'Salary', 'Termd', 'Position', 'State', 'Zip',
       'DOB', 'MaritalDesc', 'CitizenDesc', 'HispanicLatino', 'RaceDesc',
       'DateofHire', 'DateofTermination', 'TermReason', 'EmploymentStatus',
       'Department', 'ManagerName', 'ManagerID', 'RecruitmentSource',
       'PerformanceScore', 'EngagementSurvey', 'EmpSatisfaction',
       'SpecialProjectsCount', 'LastPerformanceReview_Date', 'DaysLateLast30',
       'Absences', 'Age'], axis=1)
print('Reordenamos las columnas')

#Gestionar nulos antes de pasar a formato fecha
#LastPerformanceReview_Date 

#Gestionar en nulos antes de pasar a int'SpecialProjectsCount'

#DaysLateLast30  gestionar nulos antes

#Gender: 0 Femenino, 1= Masculino
#TermR: 1. No estan y 0. Estan 
#EmploymentStatus: Active, Terminated for Cause,Voluntarily Terminated	
#TermReason: Cambiar a N/A-StillEmployed si el termd es 0 y EmploymentStatus = Active

# %%
