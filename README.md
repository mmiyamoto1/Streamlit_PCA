# Streamlit_PCA

Projeto Final Ironhack – DA | FT 
Jun/2022 – Ago/2022
Apoio Técnico – Raiana Rocha


## Objetivo do projeto: 
O projeto em si não foi nenhuma análise de dados, porém a ideia foi de criar algo para facilicar a vida de quem quer analisar um dataset com PCA. A plataforma utilizada foi o streamlit na qual é possível carregar qualquer arquivo CSV e Excel, e o código faz o resto. Já cuidará de tratamentos, fará os cálculos e projetará os gráficos do seu dataset em instantes.
Dataset:
Para fazer o teste no streamlit foi utilizado diversos dataset já prontos que estão disponíveis no github. Porém o intuito é utilizar novos dataset para ver os resultados.

## Sobre PCA: 
O que faz o PCA? 
Como o PCA chega nos resultados?
Como interpretar o PCA?
Informações na apresentação de slides.


## Bibliotecas 
Streamlit
Pandas
Plotly.express
Numpy
Sklearn.decomposition (PCA, LatentDirichletAllocation, FactorAnalysis e Truncated SVD)
Sklearn.preprocessing (StandardScaler)

## Código
Há três arquivos.
O primeiro seria o application.py que possui as linhas para a construção do streamlit. Nele temos a criação das colunas, das caixas interativas, dos gráficos e do dropbox para arquivos.
O segundo seria o application_functions.py que está todo o código com as funções para rodar o PCA. Ele pega o arquivo colocado no streamlit e fará os seguintes tratamentos:
- Separação de categóricos e numéricos
- Conversão dos nulos para a média do dataset usando numpy
- Padronização de valores com o StandardScaler
- Criação e aplicação dos modelos (PCA, Truncated e FactorAnalysis)
- Renomeação de colunas
- Concatenação de dataframes (original e a nova com os valores PCA) para a criação dos plots
E o último arquivo seria um test.ipynb, basicamente um jupyter notebook para fazer os testes do código.


## Conclusão
- Sempre levamos muito mais tempo do que projetamos levar no projeto.
- PCA em si não trará resultados financeiros para nenhuma empresa. Mas é o começo para entendar o que está acontecendo e gastar recurso onde realmente importa. 
- LatentDirichletAllocation não aceita valores negativos e foi excluído do código.
