#!/usr/bin/env python
# coding: utf-8
import pandas as pd


df = pd.read_csv('data/NEON.D17.SJER.DP1.10058.001.div_1m2Data.2019-04.basic.20200921T132904Z.csv')
df_1 = df.dropna(subset=['scientificName'], axis=0)

cols_to_keep = ['uid', 'namedLocation', 'domainID', 'siteID', 'decimalLatitude', 'decimalLongitude', 'elevation',
               'plotID', 'subplotID', 'endDate', 'divDataType', 'taxonID', 'scientificName', 'taxonRank', 'family',
               'percentCover', 'heightPlantOver300cm']
df_2 = pd.DataFrame(data=df_1, columns=cols_to_keep)

df_3 = df_2.copy()
df_3['decimalLatitude'] = df_3['decimalLatitude'].round(2)

df_4 = df_3.copy()
df_4['decimalLongitude'] = df_4['decimalLongitude'].round(2)

df_4.to_csv('data/test_output.csv', index=False)

