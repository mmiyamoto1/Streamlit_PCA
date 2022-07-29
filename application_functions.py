import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA, LatentDirichletAllocation, FactorAnalysis, TruncatedSVD    
from sklearn.preprocessing import StandardScaler
import numpy as np



# Função para fazer tratamento de numérico vs categórico
def pca_maker(data_import, model):
    # Criando variável para salvar as nvoas listas
    numerical_columns_list = []
    categorical_columns_list = []

    # loop para encontrar as colunas numéricas e salvar na nova lista, caso contrário na outra lista de categóricos
    for i in data_import.columns:
        if data_import[i].dtype == np.dtype("float") or data_import[i].dtype == np.dtype("int"):
            numerical_columns_list.append(data_import[i])
        else:
            categorical_columns_list.append(data_import[i])

    numerical_data = pd.concat(numerical_columns_list, axis=1)
    categorical_data = pd.concat(categorical_columns_list, axis=1)

    # Tratamamento dos nulos convertendo na média do dataset com numpy
    numerical_data = numerical_data.apply(lambda x: x.fillna(np.mean(x)))


    # Padronização com Standardscaler do valores
    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(numerical_data)


    # Criação modelos
    if model == 'TruncatedSVD':
        pca = TruncatedSVD()

    if model == 'FactorAnalysis':
        pca = FactorAnalysis()
    
    if model == 'PCA':
        pca = PCA()


    # Conversão dos dados para valores PCA - fit para adaptar e transform para converter os valores. Como usamos somente um tipo de dado, usamos este método somente.
    pca_data = pca.fit_transform(scaled_values)

    #st.write(np.cumsum(pca.explained_variance_ratio_))

    # Criação dos valores PCA em dataframe
    pca_data = pd.DataFrame(pca_data)

    # Criação de nome para cada coluna - com list comp fazemos a iteração de todas as colunas com nome PCA e adicionamos um número para o cada coluna subsequente.
    new_column_names = ["PCA" + " " + str(i) for i in range(1, len(pca_data.columns) + 1)]
    
    # Colocando os nomes das colunas PCA 1, PCA 2, etc com os nomes original do dataframe. Para isso colocamos os nomes originais em lista para visualizar facilmente e jogamos tudo dentro de um dict. Desta forma fica um valor antigo para um novo. key = Value
    column_mapper = dict(zip(list(pca_data.columns), new_column_names))

    # Renomeando nomes das colunas
    pca_data = pca_data.rename(columns=column_mapper)

    # Salvando nova variável do dados com valores PCA e originais
    output = pd.concat([data_import, pca_data], axis=1)

    # Finalização da função para soltar o output, colunas categóricas em lista e novas colunas
    return output, list(categorical_data.columns), new_column_names