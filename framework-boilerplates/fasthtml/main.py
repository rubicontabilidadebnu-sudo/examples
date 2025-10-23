# arquivo: grafico_barras.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título da página
st.set_page_config(page_title="Barras Verdes Interativas", layout="centered")
st.title("📊 Controle de Barras - DT, MRL, ADM")

# Entradas numéricas
st.sidebar.header("Preencha os valores")
dt = st.sidebar.slider("DT", 0, 7, 0)
mrl = st.sidebar.slider("MRL", 0, 5, 0)
adm = st.sidebar.slider("ADM", 0, 8, 0)

# Cria DataFrame
dados = pd.DataFrame({
    "Categoria": ["DT", "MRL", "ADM"],
    "Valor": [dt, mrl, adm]
})

# Cria o gráfico
fig, ax = plt.subplots(figsize=(5, 5))
barras = ax.bar(dados["Categoria"], dados["Valor"], color="green")
ax.set_ylim(0, 8)
ax.set_ylabel("Nível")
ax.set_title("Preenchimento em Tempo Real")

# Adiciona os números no topo das barras
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2, altura + 0.1,
            f"{int(altura)}", ha="center", va="bottom", fontsize=12, fontweight="bold")

# Mostra o gráfico
st.pyplot(fig)
