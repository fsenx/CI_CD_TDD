import pandas as pd
import unittest
from trata_dados import *


class TestClass(unittest.TestCase):

    def data_test(self):
        df = pd.read_csv('dados.csv', sep=',')
        df = ajusta_tipo(df)
        df = df.drop_duplicates(subset=['id_pedido'])
        
        return df

    def test_tipo_colunas(self):
        entrada = {col: str(dtype) for col, dtype in self.data_test().dtypes.items()}

        esperado = {
            'id_usuario': 'object',
            'id_pedido': 'object',
            'valor_venda': 'float64',
            'nome_cliente': 'object',
            'estado': 'object'
        }

        assert entrada == esperado
        return 200
    
    def test_nao_ha_duplicatas(self):
        entrada = self.data_test().duplicated().sum()
        esperado = 0
        
        assert entrada == esperado
        return 200
    
if __name__ == '__main__':
    unittest.main()