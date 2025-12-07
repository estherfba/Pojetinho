import streamlit as st
import pandas as pd

df = pd.read_csv("Biblioteca.csv")

st.title("Match literário da Esther")
st.write("Olá, queridos! Esse é um projetinho de férias de verão, espero que funcione (estamos na versão betinha kkk). Fique a vontade para dar o seu feedback :)")
st.write("Responda às perguntas abaixo e receba uma recomendação literária personalizada! Obviamente a base de dados se restringe ao meu acervo de livros... daqui uns anos será maior, eu espero.")

idioma = st.radio(
  "Escolha o idioma:",
  ["Indiferente", "Português", "Inglês"]
)

filtro = df.copy()
if idioma != "Indiferente":
  filtro = filtro[filtro["IDIOMA"] == idioma]
