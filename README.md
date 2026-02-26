# Projeto de Análise de Leads

Este é um projeto de análise de dados de leads com o objetivo de fornecer insights e visualizações para otimização de estratégias de vendas. Ele usa FastAPI para construir uma API que serve dados para um dashboard em **Streamlit**.

## Tecnologias Utilizadas

- **FastAPI**: Framework para construção da API.
- **Streamlit**: Biblioteca para criação do dashboard interativo.
- **Pandas**: Biblioteca para manipulação de dados.
- **Altair**: Biblioteca para visualização de dados.
- **Requests**: Para fazer chamadas HTTP para a API.

## Funcionalidades

- **API (FastAPI)**:
  - Disponibiliza dados sobre leads em vários endpoints:
    - `/leads/sdr`: Dados de leads por SDR.
    - `/leads/origem`: Dados de leads por origem.
    - `/leads/cargo`: Dados de leads por cargo.
    - `/leads/mes`: Dados de leads por mês.

- **Dashboard (Streamlit)**:
  - Exibe gráficos interativos sobre os leads, como:
    - Total de leads e SDRs.
    - Leads por SDR, origem, cargo e mês.
    - Gráficos gerados com Altair.

## Pré-requisitos

Antes de começar, verifique se você tem as seguintes ferramentas instaladas no seu ambiente:

- **Python 3.8+**
- **Git**

Além disso, é necessário instalar algumas dependências, que podem ser feitas com o `pip`.

- **streamlit**
- **pandas**
- **Altair**
- **Numpay**
- **matplotlib**
- **seaborn**
- **uvicorn**
- **fastapi**
- **pydeck**
correção manual
