import pandas as pd


class TestClass:
    
    def __init__(self,df):
        self.df = df

    def test_tipo_colunas(self):
        entrada = {col: str(dtype) for col, dtype in self.df.dtypes.items()}

        esperado = {
            'id_usuario': 'object',
            'id_pedido': 'object',
            'valor_venda': 'float64',
            'nome_cliente': 'object',
            'estado': 'object'
        }

        assert entrada == esperado
        return 200
    
    def test_nenhuma_duplicata(self):
        entrada = self.df.duplicated().sum()
        esperado = 0
        
        assert entrada == esperado
        return 200