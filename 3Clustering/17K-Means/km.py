#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:15:44 2024

@author: emir
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler =pd.read_csv('musteriler.csv')

X= veriler.iloc[:,2:4].values

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, init='k-means++')
kmeans.fit(X)

print(kmeans.cluster_centers_)
sonuclar=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=123)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_)
    
plt.plot(range(1,11),sonuclar)