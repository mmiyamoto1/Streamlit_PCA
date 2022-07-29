import streamlit as st
import pandas as pd
import plotly.express as px
from application_functions import pca_maker
import numpy as np

# Configuração das colunas
st.set_page_config(layout="wide")
scatter_column, settings_column = st.columns((4, 1))

scatter_column.title("Análise Multidimensional")

settings_column.title("Ajustes")

# Caixa para colocar o arquivo
uploaded_file = settings_column.file_uploader("Selecione um arquivo CSV")

if uploaded_file is not None:
    data_import = pd.read_csv(uploaded_file)

    # Box para seleção de modelo
    lista_modelos = ['TruncatedSVD', 'FactorAnalysis', 'PCA']
    modelo = settings_column.selectbox("Selecione o modelo", options = lista_modelos)

    # Aplicação da função de tratamento e conversão de dados
    pca_data, cat_cols, pca_cols = pca_maker(data_import, modelo)


    # Caixa para selecionar a variável - criamos variaveis para deixar o plot interativo na parte de criação do plot abaixo
    categorical_variable = settings_column.selectbox("Variável Categórica para definir a cor", options = cat_cols)
    categorical_variable_2 = settings_column.selectbox("Variável Label", options = cat_cols)

    # Variaveis PCAs
    pca_1 = 'PCA 1'
    pca_2 = 'PCA 2'

    # Criação do plot - Usaremos o plotly express, pois ele é mais rápido para rodar do que matplotlib e também tem o feature para interagir com o hover.
    scatter_column.plotly_chart(px.scatter(data_frame=pca_data, x=pca_1, y=pca_2,
    color=categorical_variable, template="simple_white", height=700,
    hover_data = [categorical_variable_2]), use_container_width=True)

else:
    scatter_column.header("Selecione um arquivo CSV")