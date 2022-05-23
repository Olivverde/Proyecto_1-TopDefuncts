from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd






df2013 =pd.read_spss('defunciones/2013-defunciones.sav')
df2014 =pd.read_spss('defunciones/2014-defunciones.sav')
df2015 =pd.read_spss('defunciones/2015-defunciones.sav')
df2016 =pd.read_spss('defunciones/2016-defunciones.sav')
df2017 =pd.read_spss('defunciones/2017-defunciones.sav')
df2018 =pd.read_spss('defunciones/2018-defunciones.sav')
df2019 =pd.read_spss('defunciones/2019-defunciones.sav')
df2020 =pd.read_spss('defunciones/2020-defunciones.sav')


df2013['Escodif'].map({'IGNORADO':'99', 'NEOG':'97'})
df2019['Escodif'].map({'97':'98', })

df = df2013.append([df2014, df2015, df2016, df2017, df2018, df2019, df2020])
df.drop(df[df['Edadif'] == 'Ignorado'].index, inplace = True)
pd.to_numeric(df['Edadif'])
#Limpieza y selccion de columnas
df = df.loc[(df['Edadif'] >= 15) & (df['Edadif'] != 999) & (df['Ecidif'] != 'Ignorado') 
    & (df['Escodif'] != 'Ignorado') & (df['Ocur'] != 'Ignorado'), 
    ['Ciuodif', 'Depocu', 'Mesocu', 'Edadif', 'Ecidif', 'Escodif', 'Asist', 'Ocur']]

print(df)

X = df[['Ecidif','Escodif','Mesocu','Depocu']]
Y= df['Edadif']

X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)

clf = svm.SVC()
clf.fit(X,Y)