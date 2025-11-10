def padronizar_email(df):
    df['email'] = df['email'].str.lower().str.strip()
    return df

def remover_duplicatas(df, subset):
    return df.drop_duplicates(subset=subset)

def preencher_categoria(df):
    df['categoria'] = df['categoria'].fillna("Não Informado")
    return df