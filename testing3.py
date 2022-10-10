# -*- coding: utf-8 -*-
"""KT tasks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Ouqpf0rqOrbBkvM4aF9f2LB-dQfxSY6
"""

import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

from google.colab import drive
drive.mount('/content/drive')

spark = SparkSession.builder.appName('Tasks').getOrCreate()

pd_df = pd.read_excel(r'/content/drive/MyDrive/Colab Notebooks/Financial Sample_kt.xlsx')

type(pd_df)

# converting pandas df to pyspark df
df = spark.createDataFrame(pd_df)

type(df)

df.printSchema()

# 2 replacing column spaces with _

print(df.columns)

# 4 round off units sold

df.select('Units_Sold', F.ceil(F.col('Units_Sold'))).show(2)

# add new column as month number

df = df.withColumn('Month_number', F.month('Date'))
df.show(10)

# remove $ from discounts and add USD

df = df.withColumn(
    'DiscountsNew',
    F.concat(F.col('Discounts'), F.lit(' USD'))
)
df.show(5)

# replace None value with No discount from discount band

df = df.replace('None', 'No Discount', subset='Discount_Band')
df.show(5)

# add new column as gross_sales (unit sale * sale price)

df = df.withColumn('gross_sales', F.col('Units_Sold') * F.col('Sale_Price'))
df.show(4)

# new column year from date

df = df.withColumn('Year', F.year('Date'))
df.show(10)

# sort data based on unit sold

df.sort('Units_Sold').show()



