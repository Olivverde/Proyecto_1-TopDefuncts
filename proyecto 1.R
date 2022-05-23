getwd()
setwd("D:/UVG/2022/Semestre 1 2022/Mineria de datos/Proyecto 1/BD")
library(haven)

library(ggplot2)
library (dplyr)


library(caret)
library(e1071)

df2009 <- read_sav("2009-defunciones.sav")
df2010 <- read_sav("2010-defunciones.sav")
df2011 <- read_sav("2011-defunciones.sav")
df2012 <- read_sav("2012-defunciones.sav")
df2013 <- read_sav("2013-defunciones.sav")
df2014 <- read_sav("2014-defunciones.sav")
df2015 <- read_sav("2015-defunciones.sav")
df2016 <- read_sav("2016-defunciones.sav")
df2017 <- read_sav("2017-defunciones.sav")
df2018 <- read_sav("2018-defunciones.sav")
df2019 <- read_sav("2019-defunciones.sav")
df2020 <- read_sav("2020-defunciones.sav")

#head(df2009)
#df2009

#df2009[setdiff(names(df2010), names (df2009))] <- NA
#df_union <- rbind(df2009, df2010)

#table(df2020['Ecidif'])


porcentaje<-0.7
datos<-df2009
set.seed(123)


corte <- sample(nrow(datos),nrow(datos)*porcentaje)
df_train<-datos[corte,]
df_test<-datos[-corte,]






df_train_filtered<-df_train[,c(1,3,4,8,16,12)]
df_train_filtered
df_test_filtered<-df_test[,c(1,3,4,8,16,12)]
df_test_filtered
df_test_filtered$Ocudif <- as.factor(df_test_filtered$Ocudif)
df_train_filtered$Ocudif <- as.factor(df_train_filtered$Ocudif)

#df_train_filtered$Ocudif

##modelos
#modelosvm <- svm(Edadif~., data = df_train_filtered, type= "C-classification" , kernel = 'linear')

modelosvm$index

little<- head()

modeloSVM_L<-svm(Edadif~., data=df_train_filtered, cost=2^5, kernel="linear") 
prediccionL<-predict(modeloSVM_L,newdata=df_test_filtered[,1:6])
confusionMatrix(df_test_filtered$Edadif[1:21513],prediccionL)
summary(prediccionL)
prediccionL
df_test_filtered
modeloSVM_L
plot(prediccionL, df_test_filtered$Edadif[1:21513] , type = "p", main = "Accuracy")
