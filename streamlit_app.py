import streamlit as st
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/estherfba/Pojetinho/refs/heads/main/Biblioteca.csv")

st.title("Match literário da Esther")
st.write("Olá, queridos! Você já pensou 'nossa, queria tanto ler um livro de __________' mas não sabe nem por onde começar a procurar? Esse link é pra você! É um projetinho de férias de verão - fruto da abstinência (voluntária, to bem) de crusader kings/the sims/netflix - que espero ser útil a alguém. Ainda ta na versão betinha kkkk fique a vontade para dar o seu feedback!")

st.write("Responda às perguntas abaixo e receba uma recomendação literária personalizada! Obviamente a base de dados se restringe ao meu acervo de livros... daqui uns anos será maior, se Deus quiser.")
st.write("OBS: tenha em vista que, assim como no amor, se colocar muito critério fica difícil encontrar um match. Todavia, obviamente, caso ache é mais certeiro.")

idioma = st.radio(
  "Em qual idioma você quer ler?",
  ["Indiferente", "Português", "Inglês"]
)

tamanho = st.radio(
    "Qual o tamanho (mais ou menos)?",
    ["Curtos (<200 páginas)", "Médios (200–500)", "Longos (>500)"]
)

origem = st.multiselect(
    "Pensou no continente natal do autor? Você pode selecionar vários (Rússia e Turquia são asiáticas aqui)",
    ["África", "América latina", "América do Norte", "Ásia", "Europa", "Oceania" ]
)


if st.button("Indicar livro"):

  filtro = df.copy()

  #filtro idioma#
  if idioma != "Indiferente":
    filtro = filtro[filtro["IDIOMA"] == idioma]
  elif idioma != "Português":
    filtro = filtro[filtro["IDIOMA"] == "Português"]
  elif idioma != "Inglês":
    filtro = filtro[filtro["IDIOMA"] == "Inglês"]

  #filtro tamanho#
  if tamanho == "Curtos (<200 páginas)":
      filtro = filtro[filtro["PÁG"] < 200]
  elif tamanho == "Médios (200–500)":
      filtro = filtro[(filtro["PÁG"] >= 200) & (filtro["PÁG"] <= 500)]
  elif tamanho == "Longos (>500)":
      filtro = filtro[filtro["PÁG"] > 500]

  if filtro.empty:
    st.error("Não encontrei nenhum livro com esses critérios!")
  else:
    livro = filtro.sample(1).iloc[0]

    st.success("MATCH! Sua recomendação é:")
    st.write(livro)

  st.info("Caso queira gerar outra recomendação, clique novamente.")
