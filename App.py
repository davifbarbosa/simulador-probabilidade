# app.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

st.title("🔮 Simulador de Previsão de Vendas")
st.markdown("Cole abaixo seus dados de vendas separadas por vírgula. Exemplo: `32000, 38000, 85000, 18000, ...`")

# Dados de vendas como exemplo preenchido (os seus 23 meses)
exemplo_dados = "22577,72072,31977,38108,85599,18716,28645,19905,13607,21550,17133,18742,34097,24848,21072,36385,45547,16413,21205,30540,19279,21525,15210,32372,26480,39244,18120,20648,41759,17391,8200,11101,47600,43749,24087,27440,21466"

# Área de entrada de dados com exemplo já carregado
input_str = st.text_area("Dados de vendas:", value=exemplo_dados, height=150)

if input_str:
    try:
        # Limpa e converte os dados
        vendas = [float(x.strip().replace(".", "").replace(",", ".")) for x in input_str.split(",")]
        kde = gaussian_kde(vendas)
        x = np.linspace(min(vendas), max(vendas), 1000)
        y = kde(x)
        valor_mais_provavel = x[np.argmax(y)]

        # Mostra resultado
        st.subheader(f"📌 Valor mais provável: **{valor_mais_provavel:,.0f}** unidades")

        # Mostra gráfico
        fig, ax = plt.subplots()
        ax.plot(x, y, color="orange", label="Densidade estimada")
        ax.axvline(valor_mais_provavel, color="red", linestyle="--", label=f"Mais provável: {valor_mais_provavel:,.0f}")
        ax.set_xlabel("Vendas")
        ax.set_ylabel("Densidade")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Erro ao processar os dados: {e}")
