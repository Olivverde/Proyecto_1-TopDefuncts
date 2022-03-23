import pandas as pd
import matplotlib.pyplot as plt

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
        
        return df

    def defuntsPerYear(self, df):
        df = df.groupby(df['Añoreg']).size()
        ax = df.plot.bar()
        plt.show()
    
    def defuntsPerDepto(self, df):
        df = df.groupby(df['Depocu']).size().sort_values(ascending=False)
        ax = df.plot.bar()
        plt.show()
        



read = readDF()
df = read.df
#read.defuntsPerYear(df)
read.defuntsPerDepto(df)