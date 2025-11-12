from pipeline_ingestao import carregar_csv, salvar_processado
from correcao_automatica import corrigir_clientes, corrigir_produtos, corrigir_vendas, corrigir_logistica
from great_expectations_setup import setup_great_expectations_context, create_clientes_expectations, create_produtos_expectations, create_vendas_expectations, create_logistica_expectations
import great_expectations as ge

# 1. Ingestão
clientes = carregar_csv("clientes.csv")
produtos = carregar_csv("produtos.csv")
vendas = carregar_csv("vendas.csv")
logistica = carregar_csv("logistica.csv")

# 2. Correções
clientes = corrigir_clientes(clientes)
produtos = corrigir_produtos(produtos)
vendas = corrigir_vendas(vendas)
logistica = corrigir_logistica(logistica)

# 3. Salvando processados
salvar_processado(clientes, "clientes_corrigido.csv")
salvar_processado(produtos, "produtos_corrigido.csv")
salvar_processado(vendas, "vendas_corrigido.csv")
salvar_processado(logistica, "logistica_corrigido.csv")

# 4. Great Expectations
context = setup_great_expectations_context()

# Validações
df_clientes = ge.from_pandas(clientes)
create_clientes_expectations(df_clientes)
df_clientes.validate()

df_produtos = ge.from_pandas(produtos)
create_produtos_expectations(df_produtos)
df_produtos.validate()

df_vendas = ge.from_pandas(vendas)
create_vendas_expectations(df_vendas)
df_vendas.validate()

df_logistica = ge.from_pandas(logistica)
create_logistica_expectations(df_logistica)
df_logistica.validate()

print("\n✅ Pipeline executado com sucesso e dados corrigidos!")
print("Arquivos corrigidos disponíveis em: data/processed/")
