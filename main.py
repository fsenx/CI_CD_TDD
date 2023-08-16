import pandas as pd
from test import *
from trata_dados import *

def run(request=None):
  df = pd.read_csv('dados.csv', sep=',')
  print(len(df))
  return "200"

if __name__ == '__main__':
    run()
