import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def carregar_dados(caminho):
    try:
        df = pd.read_csv(caminho)
        logging.info(f"Carregado com sucesso: {caminho}")
        return df
    except Exception as e:
        logging.error(f"Erro ao carregar {caminho}: {e}")
        return pd.DataFrame()

clientes = carregar_dados('../data/raw/clientes.csv')
produtos = carregar_dados('../data/raw/produtos.csv')
vendas = carregar_dados('../data/raw/vendas.csv')
logistica = carregar_dados('../data/raw/logistica.csv')