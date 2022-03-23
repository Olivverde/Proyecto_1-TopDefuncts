import pandas as pd

class readDF():

    def __init__(self):
        self.df = self.concat()

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


read = readDF()
df = read.df
print(df.columns())