import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import sklearn.preprocessing
import sklearn.cluster as cluster
import pyclustertend 

class readDF():

    def __init__(self):
        auxDf = self.concat()
        self.df = self.dfGrooming(auxDf)

        print(self.df.columns)


    def concat(self):
        df2009 =pd.read_spss('defunciones/2009-defunciones.sav')
        df2010 =pd.read_spss('defunciones/2010-defunciones.sav')
        df2011 =pd.read_spss('defunciones/2011-defunciones.sav')
        df2012 =pd.read_spss('defunciones/2012-defunciones.sav')
        df2013 =pd.read_spss('defunciones/2013-defunciones.sav')
        df2014 =pd.read_spss('defunciones/2014-defunciones.sav')
        df2015 =pd.read_spss('defunciones/2015-defunciones.sav')
        df2016 =pd.read_spss('defunciones/2016-defunciones.sav')
        df2017 =pd.read_spss('defunciones/2017-defunciones.sav')
        df2018 =pd.read_spss('defunciones/2018-defunciones.sav')
        df2019 =pd.read_spss('defunciones/2019-defunciones.sav')
        df2020 =pd.read_spss('defunciones/2020-defunciones.sav')

        df09To20 = df2009.append(
            [
            df2010, df2011, df2012,
            df2013, df2014, df2015,
            df2016, df2017, df2018,
            df2019, df2020
            ])
        
        return df09To20
    
    def dfGrooming(self, df):
        # Limpieza de año de registro de defuncion 
        df['Añoreg'] = df['Añoreg'].astype(int).astype(str)
        df['Añoreg'] = df['Añoreg'].apply(
            lambda x: '2009' if x == '9' 
            else ('2010' if (x == '10') else x))

        # Limpieza de Edad del difunto 
        df['Edadif'] = df['Edadif'].apply(
            lambda x: -1 if x == 'Ignorado' else x)
        df['Edadif'] = df['Edadif'].astype(int)
        
        # Limpieza de asistencia del difunto 
        df['Asist'] = df['Asist'].apply(
            lambda x: 'Médica' if x == 'Médico' else x)
        return df

    def defuntsPerYear(self, df):
        df = df.groupby(df['Añoreg']).size()
        ax = df.plot.bar()
        plt.show()
    
    def defuntsPerDepto(self, df):
        df = df.groupby(df['Depocu']).size().sort_values(ascending=False)
        ax = df.plot.bar()
        plt.show()
    
    def genderDefunts(self, df):
        df = df.groupby(df['Sexo']).size()
        ax = df.plot.bar()
        plt.show()
    
    def ageDist(self, df):
        df = df.groupby(df['Edadif']).size().sort_index()
        df.plot(color='red')
        df.plot.bar()
        plt.locator_params(axis='x', nbins=12)
        plt.show()
    
    def asistances(self, df):
        df = df.groupby(df['Asist']).size()
        df.plot.bar(color=[
            'green','orange', 'pink',
            'red', 'blue', 'yellow'
         ])
        plt.show()

    def defuntsProfs(self, df):
        df = df.groupby(df['Ocudif']).size().sort_values(ascending=False).head(10)
        print(df)
        plt.xticks(rotation = 90)
        df.plot.bar()
        plt.show()
    
    def ocupCauses_1(self, df):
        df = df[df['Ocudif'] == 'Oficios domésticos no remunerados']
        df = df.groupby(df['Caudef']).size().sort_values(ascending=False).head(10)
        df.plot.bar()
        plt.show()
    
    def ocupCauses_2(self, df):
        df = df[df['Ocudif'] == 'Peones de explotaciones agrícolas']
        df = df.groupby(df['Caudef']).size().sort_values(ascending=False).head(10)
        df.plot.bar()
        plt.show()
    
    def ocupCauses_3(self, df):
        df = df[df['Ocudif'] == 'Infante (Sin ocupación)']
        df = df.groupby(df['Caudef']).size().sort_values(ascending=False).head(10)
        df.plot.bar()
        plt.show()

    def ocupCauses_Estudiantes(self, df):
        df = df[df['Ocudif'] == 'Estudiante']
        df = df.groupby(df['Caudef']).size().sort_values(ascending=False).head(10)
        df.plot.bar()
        plt.show()
  

    def var_summary(self, df):
        df = self.df
        quall = ['Depreg', 'Mupreg', 'Mesreg', 'Depocu', 'Mupocu', 'Areag', 'Sexo', 'Mesocu', 'Perdif', 'Getdif', 'Ecidif', 'Escodif', 'Ocudif', 'Dnadif', 'Mnadif', 'Nacdif', 'Dredif', 'Mredif', 'Caudef', 'Asist', 'Ocur', 'Cerdef',  'mupreg', 'mupocu', 'añoocu', 'mnadif', 'Pnadif', 'Predif', 'Puedif', 'Ciuodif', 'caudef.descrip']
        quant = ['Añoreg', 'Diaocu', 'Añoocu', 'Edadif']
        # df = df.pop(cuantitativas)
        df.drop(quall, axis='columns', inplace=True)
        print(df.describe())
        
    def histogram_quant_var(self, df):
        df = self.df
        
        x = df['Añoreg'].dropna()
        x.astype(int)
        df = df.sort_values('Añoreg', ascending=False)
        plt.hist(x, color='#ACFA58', alpha=0.5,  bins=20, rwidth=0.9)
        plt.title('Distribución del año de registro')
        plt.xlabel('Año de registro')
        plt.show()
    
        x = df['Diaocu'].dropna()
        x.astype(int)
        df = df.sort_values('Diaocu', ascending=False)
        plt.hist(x, color='#ACFA58', alpha=0.5,  bins=20, rwidth=0.9)
        plt.title('Distribución del dia de ocurrencia')
        plt.xlabel('Dia de ocurrencia')
        plt.show()
       
        df.drop(df[df['Edadif'] == 'Ignorado'].index, inplace = True)
        x = df['Edadif'].dropna()
        x.astype(int)
        df = df.sort_values('Edadif', ascending=False)
        plt.hist(x, color='#ACFA58', alpha=0.5,  bins=20, rwidth=0.9)
        plt.title('Distribución de la edad del difunto (a)')
        plt.xlabel('Edad del difunto (a)')
        plt.show()
        
    def freq_table(self, df, var):
        df = self.df
        #quall = ['Depreg', 'Mupreg', 'Mesreg', 'Depocu', 'Mupocu', 'Areag', 'Sexo', 'Mesocu', 'Perdif', 'Getdif', 'Ecidif', 'Escodif', 'Ocudif', 'Dnadif', 'Mnadif', 'Nacdif', 'Dredif', 'Mredif', 'Caudef', 'Asist', 'Ocur', 'Cerdef']
        df = pd.value_counts(df[var])
        
        df = pd.DataFrame(df)
        df.columns = ['Frequency']

        df['Relative Frequency %'] = 100 * df['Frequency'] / len(df)
        
        cumulative = [ ]
        cumulative_value = 0

        for i in df['Relative Frequency %'].values:
            cumulative_value = cumulative_value + i
            cumulative.append(cumulative_value)

        df['Cumulative Frequency %'] = cumulative
        print(df)

    def codo(self, x):
        numeroClusters = range(1,11)
        wcss = []
        for i in numeroClusters:
            kmeans = cluster.KMeans(n_clusters=i)
            kmeans.fit(x)
            wcss.append(kmeans.inertia_)

        plt.plot(numeroClusters, wcss)
        plt.xlabel("Número de clusters")
        plt.ylabel("Score")
        plt.title("Gráfico de Codo")
        plt.show()

    def clustering(self, df, k = 2, k_select_tools = False):
        #   La gran mayoría son numéricas pero se las tuvo que tratar como si lo fueran para que haya más de
        #   una variable numérica con la cual trabajar. Se eligieron la que se cree pueden servir para agrupar.
        #   Toma la edad, el mes de ocurrencia, la asistencia recibida, el lugar de ocurrencia, la escolaridad,
        #   el estado civil, el depto de ocurrencia y el depto de residencia.
        df = df.filter(items=['Edadif', 'Mesocu', 'Asist', 'Ocur', 'Escodif', 'Ecidif', 
        'Depocu', 'Dredif'])                    

        df.drop(df[df['Edadif'] == 'Ignorado'].index, inplace = True)       #remover ignorados
        df.drop(df[df['Asist'] == 'Ignorado'].index, inplace = True)        #remover ignorados
        df.drop(df[df['Ocur'] == 'Ignorado'].index, inplace = True)         #remover ignorados
        df.drop(df[df['Escodif'] == 'Ignorado'].index, inplace = True)      #remover ignorados
        df.drop(df[df['Ecidif'] == 'Ignorado'].index, inplace = True)       #remover ignorados
        df.drop(df[df['Depocu'] == 'Ignorado'].index, inplace = True)       #remover ignorados
        df.drop(df[df['Dredif'] == 'Ignorado'].index, inplace = True)       #remover ignorados
        df.drop(df[df['Edadif'] < 18].index, inplace = True)                #remover menores de edad

        df = df.dropna()    #quitar NAs                                   

        x = np.array(df['Edadif', 'Mesocu', 'Asist', 'Ocur', 'Escodif', 'Ecidif', 'Depocu', 'Dredif'])
        #               0          1         2        3       4          5         6         7
        norm_x = sklearn.preprocessing.scale(x)
        
        if (k_select_tools):
            print(pyclustertend.hopkins(x,len(x)))
            pyclustertend.vat(norm_x)
            self.codo(norm_x)
        else:
            y = KMeans(n_clusters = k, random_state=0).fit_predict(x)
            
            #¿Los grupos presentan una diferencia entre el lugar de ocurrencia y la asistencia recibida?
            plt.subplot(221)
            plt.scatter(x[:, 3], x[:, 2], c=y)
            plt.title('Lugar de ocurrencia vs Asistencia recibida')

            #¿Los trabajos requieren que gente de diferentes grupos viajen?
            plt.subplot(222)
            plt.scatter(x[:, 6], x[:, 7], c=y)
            plt.title('Departameto de ocurrencia vs Departamento de residencia')

            #¿Clase social de los grupos?
            plt.subplot(223)
            plt.scatter(x[:, 5], x[:, 0], c=y)
            plt.title('Escolaridad vs Edad')

            #¿Los grupos presentan diferencia entre las épocas del año y el lugar de ocurrencia?
            plt.subplot(224)
            plt.scatter(x[:, 1], x[:, 3], c=y)
            plt.title('Mes de ocurrencia vs Lugar de ocurrencia')
            
            plt.show()

        


        

read = readDF()
df = read.df
#quall = ['Depreg', 'Mupreg', 'Mesreg', 'Depocu', 'Mupocu', 'Areag', 'Sexo', 'Mesocu', 'Perdif', 'Getdif', 'Ecidif', 'Escodif', 'Ocudif', 'Dnadif', 'Mnadif', 'Nacdif', 'Dredif', 'Mredif', 'Caudef', 'Asist', 'Ocur', 'Cerdef']
        
#read.defuntsPerYear(df)
#read.defuntsPerDepto(df)
#read.genderDefunts(df)
#read.ageDist(df)
#read.asistances(df)
#read.defuntsProfs(df)
#read.ocupCauses_1(df)
#read.ocupCauses_2(df)
#read.ocupCauses_3(df)
read.ocupCauses_Estudiantes(df)
#read.freq_table(df, 'Cerdef')

#correr primero así para sacar codos y la cantidad de clusters
#read.clustering(df, k_select_tools=True)
#luego correr con clusters
#read.clustering(df, k=x)

