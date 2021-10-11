#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:31:24 2021

@author: firat
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veriler = pd.read_csv('~/Pictures/veriler.csv')



yas = veriler.iloc[:,1:4].values
ulke = veriler.iloc[:,0:1].values

from sklearn import preprocessing
#ulkeleri sayıya çeviriyor. Böylece kolonlara eklenebiliyor
le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])

#print(ulke)
#sayı olarak gelen ulkeler kolonlara ekleniyor. 1 veya 0 olarak işliyor satırları
ohe = preprocessing.OneHotEncoder()

ulke = ohe.fit_transform(ulke).toarray()


c = veriler.iloc[:,-1:].values

from sklearn import preprocessing
#ulkeleri sayıya çeviriyor. Böylece kolonlara eklenebiliyor
le = preprocessing.LabelEncoder()

c[:,0] = le.fit_transform(veriler.iloc[:,-1])

#print(ulke)
#sayı olarak gelen ulkeler kolonlara ekleniyor. 1 veya 0 olarak işliyor satırları
ohe = preprocessing.OneHotEncoder()

c = ohe.fit_transform(c).toarray()
print(c)


#print(ulke)

#kolona eklenen ulkelere isim veriliyor sonuc şeklinde dataframe oluşturuluyor
sonuc = pd.DataFrame(data=ulke , index  = range(22) , columns = ['fr','tr','us'])
#print(sonuc)


sonuc2 = pd.DataFrame(data=yas, index = range(22),columns=['boy','kilo','yas'])

cinsiyet = veriler.iloc[:,-1].values

sonuc3 = pd.DataFrame(data=c[:,:1], index = range(22), columns=['cinsiyet'])

#concat ile dataframeler birleştiriliyor.
s = pd.concat([sonuc,sonuc2], axis=1)
#print(s)

s2 = pd.concat([s,sonuc3], axis = 1)

#print(s2)


from sklearn.model_selection import train_test_split
#test datası test ve train datası olarak ayrılıyor. s dataframe kullanılarak sonuc3 dataframe tahminleniyor
x_train , x_test , y_train, y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)


#verilerin ölçülendirilmesi yapılıyor. sayısal değerler benzer yapıya çevriliyor.
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()


X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)