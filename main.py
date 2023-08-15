import pandas as pd
from test import *
from trata_dados import *

df = pd.read_csv('dados.csv', sep=',')
print(df)