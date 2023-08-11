def ajusta_tipo(df):
    df['id_usuario'] = df['id_usuario'].astype(str)
    df['id_pedido'] = df['id_pedido'].astype(str)
    df['valor_venda'] = df['valor_venda'].astype(float)
    df['nome_cliente'] = df['nome_cliente'].astype(str)
    df['estado'] = df['estado'].astype(str)
    
    return df