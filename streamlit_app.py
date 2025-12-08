import streamlit as st
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/estherfba/Pojetinho/refs/heads/main/Biblioteca%20(2).csv")

st.title("Match Literário da Esther")

st.write("Olá! Você já pensou 'nossa, queria tanto ler um livro de __________' mas não sabe nem por onde começar a procurar? Isso é pra você!")

st.write("Nada mais que um projetinho de férias de verão (25/26), fruto da abstinência (voluntária, to bem) de crusader kings/the sims/netflix, espero que seja útil a alguém. Ainda ta na versão betinha kkkk fique a vontade para dar o seu feedback!")

st.write("Sem mais delongas, responda às perguntas abaixo e receba uma recomendação literária personalizada! Obviamente a base de dados se restringe ao meu acervo de livros... daqui uns anos será maior, se Deus quiser.")

st.write("OBS: tenha em vista que, assim como no amor, ao colocar muitos critérios fica mais difícil encontrar uma correspondência. Todavia, obviamente, caso ache é mais certeiro.")

idioma = st.radio(
  "Em qual idioma você quer ler?",
  ["Indiferente", "Português", "Inglês"]
)

tamanho = st.radio(
    "Qual o tamanho do livro (mais ou menos)?",
    ["Curtos (<200 páginas)", "Médios (200–500)", "Longos (>500)"]
)

origem = st.multiselect(
    "Pensou no continente natal do autor? Você pode selecionar vários... (ah, Rússia e Turquia são asiáticas aqui)",
    ["África", "América latina", "América do Norte", "Ásia", "Europa", "Oceania" ]
)

romance = st.radio(
  "O amor romântico é o tema principal?",
  ["Não sei, eis a questão...", "Sim", "Não"]
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

#filtro origem#

#filtro romance#
  if romance != "Não sei, eis a questão...":
    filtro = filtro[filtro["LOVE"] == romance]
  elif idioma != "Sim":
    filtro = filtro[filtro["LOVE"] == "S"]
  elif idioma != "Não":
    filtro = filtro[filtro["LOVE"] == ""]
  
  if filtro.empty:
    st.error("Não encontrei nenhum livro com esses critérios!")
  else:
    livro = filtro.sample(1).iloc[0]

    st.success("MATCH! Sua recomendação é:")
    st.write(livro)

  st.info("Caso queira gerar outra recomendação, clique novamente.")
