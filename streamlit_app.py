import streamlit as st
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/estherfba/Pojetinho/refs/heads/main/Biblioteca.csv")

st.title("Match literário da Esther")
st.subtitle("Olá, queridos! Você já pensou 'nossa, queria tanto ler um livro de __________' mas não sabe nem por onde começar a procurar? Esse link é pra você! É um projetinho de férias de verão - fruto da abstinência (voluntária, to bem) de crusader kings/the sims/netflix - que espero ser útil a alguém. Ainda ta na versão betinha kkkk fique a vontade para dar o seu feedback!")

st.write("Responda às perguntas abaixo e receba uma recomendação literária personalizada! Obviamente a base de dados se restringe ao meu acervo de livros... daqui uns anos será maior, se Deus quiser.")
st.write("OBS: tenha em vista que, assim como no amor, se colocar muito critério fica difícil encontrar um match. Todavia, obviamente, caso ache é mais certeiro")

idioma = st.radio(
  "Escolha o idioma:",
  ["Indiferente", "Português", "Inglês"]
)

filtro = df.copy()
if idioma != "Indiferente":
  filtro = filtro[filtro["IDIOMA"] == idioma]
