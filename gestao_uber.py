# IMPORTANDO AS BIBLIOTECAS NECESSÁRIA PARA O CÓDIGO:
import pandas as pd
import numpy as np
import streamlit as st
import datetime
from datetime import timedelta
import openpyxl
import plotly.express as px

# CONFIGURAÇÃO DA PÁGINA:
st.set_page_config(page_title='GESTÃO UBER & 99', layout='wide')

# ACESSANDO A PLANILHA E CRIANDO UM DATAFRAME PARA CONTROLE DO APLICATIVO:
df = pd.read_excel(r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Gestão Ganhos Uber\CONTROLE GANHOS UBER - 99 - PARTICULAR.xlsx",
                   header=2, sheet_name='PLANILHA CADASTRO')

# HEADER PARA NOME DO APLICATIVO:
# TÍTULO E MARCAÇÃO PARA DIVISÃO DE DADOS:
st.header('Desempenho no App', divider='rainbow')

# SIDEBAR PARA NOME:
with st.sidebar:
    # TÍTULO E MARCAÇÃO PARA DIVISÃO DE DADOS:
    st.sidebar.header('Dados de Cadastro', divider='rainbow')

# INPUT DE DATAS:
with st.container():
    st.sidebar.date_input('Selecione a Data Inicial: ',
                          format='DD/MM/YYYY')
    st.sidebar.date_input('Selecione a Data Final: ',
                          format='DD/MM/YYYY', value=datetime.date.today())
    st.header('Tabela de Dados Uber e 99')
    st.dataframe(df[1:])

# VARIÁVEIS DE CONTROLE DO PROGRAMA:
custo_seguro = np.sum(df['CUSTO DIÁRIO SEGURO'])
km_inicial = df['KM INICIAL'].min()
ultimo_km = df['KM FINAL'].max()
km_rodado = ultimo_km - km_inicial
faturamento = np.sum(df['TOTAL LUCRO DIA'])
lucro = np.sum(df['LUCRO LÍQUIDO'])
despesas_combustivel = np.sum(df['GASTO COMBUSTÍVEL'])
despesas_lanches = np.sum(df['GASTO LANCHE'])
total_corridas_uber = np.sum(df['TOTAL CORRIDAS UBER'])
total_corridas_99 = np.sum(df['TOTAL CORRIDAS 99'])
lucro_uber = np.sum(df['LUCRO UBER'])
lucro_99 = np.sum(df['LUCRO 99'])
despesas_geral = (despesas_combustivel + custo_seguro + despesas_lanches)
litragem_combustivel = np.sum(df['LITRAGEM ABASTECIMENTO'])
media_consumo = np.mean(df['MÉDIA CONSUMO KM/L'])

# VARIÁVEIS DE GRÁFICOS:
df_controle = df[['TOTAL LUCRO DIA', 'GASTO COMBUSTÍVEL', 'LUCRO LÍQUIDO']]
df_media = df[['KM RODADO', 'LITRAGEM ABASTECIMENTO', 'MÉDIA CONSUMO KM/L']]
df_lucro_por_aplicativo = df[['LUCRO UBER', 'LUCRO 99']]
df_corridas_por_aplicativo = df[['TOTAL CORRIDAS UBER', 'TOTAL CORRIDAS 99']]

# ADICIONANDO CONTAINER PARA GRÁFICOS:
with st.container():
    st.header('', divider='rainbow')  # MARCAÇÃO PARA DIVISÃO DE DADOS:
    st.subheader('Controle de Faturamentos e Custos')
    st.bar_chart(df_controle)
    st.header('', divider='rainbow')  # MARCAÇÃO PARA DIVISÃO DE DADOS:
    st.subheader('Controle de Quilometragem e Consumo do Veículo')
    st.bar_chart(df_media)
    st.header('', divider='rainbow')  # MARCAÇÃO PARA DIVISÃO DE DADOS:
    st.subheader('Lucro Por Aplicativo')
    st.bar_chart(df_lucro_por_aplicativo)
    st.header('', divider='rainbow')  # MARCAÇÃO PARA DIVISÃO DE DADOS:
    st.subheader('Corridas Por Aplicativo')
    st.bar_chart(df_corridas_por_aplicativo)
    st.header('', divider='rainbow')  # MARCAÇÃO PARA DIVISÃO DE DADOS:

# ADICIONANDO CONTAINER PARA 2 COLUNAS:
with st.container():
    col1, col2 = st.columns(2)
    col1.subheader('Tabela de Controle de faturamentos e Custos')
    col1.dataframe(df_controle)
    col2.subheader('Tabela Controle de Quilometragem e Consumo do Veículo')
    col2.dataframe(df_media)

# ADICIONANDO CONTAINER PARA 2 COLUNAS:
with st.container():
    st.header('', divider='rainbow')  # MARCAÇÃO PARA DIVISÃO DE DADOS:
    col3, col4 = st.columns(2)
    col3.subheader('Tabela Lucro Por Aplicativos')
    col3.dataframe(df_lucro_por_aplicativo)
    col4.subheader('Tabela Corridas Por Aplicativos')
    col4.dataframe(df_corridas_por_aplicativo)

# CRIANDO UMA SIDEBAR PARA A TELA INICIAL:
with st.sidebar:
    # TÍTULO E MARCAÇÃO PARA DIVISÃO DE DADOS:
    st.header('Dados de Controle', divider='rainbow')
    st.write(f'Total Litros Combustível: :orange[{
             litragem_combustivel:.3f}]')
    st.write(f'Km Rodado: :violet[{km_rodado:.0f}]')
    st.write(
        f'Total Corridas Uber: :blue-background[{total_corridas_uber:.0f}]')
    st.write(f'Total Corridas 99: :blue-background[{total_corridas_99:.0f}]')
    st.write(f'Despesas com Combustível: :red[R$ {despesas_combustivel:.2f}]')
    st.write(f'Despesa Geral: :red[R$ {despesas_geral:.2f}]')
    st.write(f'Lucro Uber: :green[R$ {lucro_uber:.2f}]')
    st.write(f'Lucro 99: :green[R$ {lucro_99:.2f}]')
    st.write(f'Lucro Bruto: :green[R$ {faturamento:.2f}]')
    st.write(f'Lucro Líquido: :green[R$ {lucro:.2f}]')
    st.write(f'Média Consumo: :blue[{media_consumo:.2f} Km/l]')
    st.header('', divider='rainbow')  # MARCAÇÃO PARA DIVISÃO DE DADOS:

st.header('', divider='rainbow')  # MARCAÇÃO PARA DIVISÃO DE DADOS:
