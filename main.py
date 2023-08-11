import pandas as pd
from test import *
from trata_dados import *

df = pd.read_csv('dados.csv', sep=',')
df = ajusta_tipo(df)
print(TestClass(df).test_tipo_colunas())
df = df.drop_duplicates()
print(TestClass(df).test_nenhuma_duplicata())