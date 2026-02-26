import streamlit as st
import pandas as pd
import requests
import altair as alt
import os

# URL da API FastAPI
API_URL = os.getenv("API_URL")

# Título do Dashboard
st.title("Dashboard SDR - Leads")

# Função para buscar dados da API
def get_data(endpoint):
    try:
        response = requests.get(f"{API_URL}/{endpoint}")
        response.raise_for_status()  # Levanta um erro se a resposta não for OK (200)
        return pd.DataFrame(response.json())  # Converte a resposta JSON para DataFrame
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar dados de {endpoint}: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio se houver erro

# Carregar dados das APIs
df_sdr = get_data("leads/sdr")
df_origem = get_data("leads/origem")
df_cargo = get_data("leads/cargo")
df_mes = get_data("leads/mes")

# Verifique se os DataFrames foram carregados corretamente
if df_sdr.empty or df_origem.empty or df_cargo.empty or df_mes.empty:
    st.warning("Não foi possível carregar os dados. Verifique a API.")

else:
    # Métricas gerais
    st.subheader("Resumo Geral")
    col1, col2 = st.columns(2)
    col1.metric("Total de Leads", df_sdr["total_leads"].sum())
    col2.metric("Número de SDRs", df_sdr["sdr_owner"].nunique())

    # Leads por SDR 
    st.header("Leads por SDR")
    chart_sdr = alt.Chart(df_sdr).mark_bar().encode(
        x="sdr_owner:N",
        y="total_leads:Q",
        tooltip=["sdr_owner", "total_leads"]
    )
    st.altair_chart(chart_sdr, use_container_width=True)

    # Leads por Origem 
    st.header("Leads por Origem")
    chart_origem = alt.Chart(df_origem).mark_bar().encode(
        x="origem:N",
        y="total_leads:Q",
        tooltip=["origem", "total_leads"]
    )
    st.altair_chart(chart_origem, use_container_width=True)

    # Leads por Cargo 
    st.header("Leads por Cargo")
    chart_cargo = alt.Chart(df_cargo).mark_bar().encode(
        x="cargo:N",
        y="total_leads:Q",
        tooltip=["cargo", "total_leads"]
    )
    st.altair_chart(chart_cargo, use_container_width=True)

    # Leads por Mês 
    st.header("Leads por Mês")
    chart_mes = alt.Chart(df_mes).mark_line(point=True).encode(
        x="mes_criacao:N",
        y="total_leads:Q",
        tooltip=["mes_criacao", "total_leads"]
    )
    st.altair_chart(chart_mes, use_container_width=True)
