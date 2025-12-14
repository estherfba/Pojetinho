import streamlit as st
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/estherfba/Pojetinho/refs/heads/main/Bibliotecanova.csv")

st.title("Match Literário da Esther :) ")

st.markdown("""
### Já pensou 'nossa, queria tanto ler um livro de __________' e travou? Isso é pra você! 

Responda às perguntas e receba uma recomendação literária personalizada.

Nada mais que um projetinho de férias de verão 25/26, fruto da abstinência (voluntária, to bem) de crusader kings/the sims/netflix, espero que seja útil a alguém. Ainda ta na versão betinha kkkk fique a vontade para dar o seu feedback!

OBS: tenha em vista que, assim como no amor, ao colocar muitos critérios fica mais difícil encontrar uma correspondência. Todavia, obviamente, caso ache é mais certeiro.
""")

idioma = st.radio(
  "Em qual idioma você quer ler?",
  ["Indiferente", "Português", "Inglês"]
)

tamanho = st.radio(
    "Qual o tamanho do livro?",
    ["Curto (<200 páginas)", "Médio (200–500)", "Longo (>500)"]
)

origem = st.multiselect(
    "Pensou no continente natal do autor? Você pode selecionar vários... (ah, Rússia e Turquia são asiáticas aqui)",
    ["África", "América latina", "América do Norte", "Ásia", "Europa", "Oceania" ]
)

romance = st.radio(
  "O amor romântico é o tema principal?",
  ["Não sei, eis a questão...", "Sim", "Não"]
)

religiao = st.radio(
  "Tá procurando um livro religioso?",
  ["Não pensei nisso ainda", "Sim", "Não"]
)

classico = st.radio(
  "Sua futura leitura é considerada um clássico da literatura nacional/mundial?",
  ["Indiferente", "Sim", "Não"]
)

critica = st.radio(
  "A história tem um quê de crítica social? Nem que seja velada, assim, no off (salve salve turma do pagode)",
  ["Não sei dizer", "Sim", "Não"]
)


st.write ("Obviamente a base de dados se restringe ao meu acervo de livros... daqui uns anos será maior, se Deus quiser.")

if st.button("Indicar livro"):

  filtro = df.copy()

  #filtro idioma#
  if idioma != "Português":
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
  if origem:
    filtro = filtro[filtro["GEOGRAFIA"].isin(origem)]

#filtro romance#
  if romance == "Sim":
    filtro = filtro[filtro["LOVE"] == "S"]
  elif romance == "Não":
    filtro = filtro[filtro["LOVE"] == "N"]

#filtro religiao#
  if religiao == "Sim":
    filtro = filtro[filtro["REL"] == "S"]
  elif religiao == "Não":
    filtro = filtro[filtro["REL"] == "N"]

#filtro classico#
  if classico == "Sim":
    filtro = filtro[filtro["CLÁSSICO"] == "S"]
  elif classico == "Não":
    filtro = filtro[filtro["CLÁSSICO"] == "N"]

#filtro critica#
  if critica == "Sim":
    filtro = filtro[filtro["CRÍTICA"] == "S"]
  elif critica == "Não":
    filtro = filtro[filtro["CRÍTICA"] == "N"]
  
  if filtro.empty:
    st.error("Não encontrei nenhum livro com esses critérios!")
  else:
    livro = filtro.sample(1).iloc[0]

    st.success("MATCH! Sua recomendação é:")
    st.markdown(f"""
<div style="
    border:1px solid #ddd;
    border-radius:10px;
    padding:20px;
    background-color:#f9f9f9;
    color:#1F2937;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
">
<h3>📖 {livro['TÍTULO']}</h3>
<p><b>Autor:</b> {livro['AUTOR']}</p>
<p><b>Tema:</b> {livro['GERAL']}</p>
<p><b>Páginas:</b> {livro['PÁG']}</p>
</div>
""", unsafe_allow_html=True)

  st.info("Caso queira gerar outra recomendação, clique novamente.")
