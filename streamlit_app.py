import streamlit as st
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/estherfba/Pojetinho/refs/heads/main/Biblioteca%20-%20Dados%20(1).csv")

st.title("Match Literário da Esther :) ")

st.image(
  "https://i.pinimg.com/736x/2d/f4/5a/2df45abebdbfee797e1502c5509d5370.jpg",
  use_column_width=True
)

st.markdown("""
### Já pensou 'nossa, queria tanto ler um livro de __________' e travou? Isso é pra você! 

Responda às perguntas e receba uma recomendação literária.

Nada mais que um projetinho de férias de verão 25/26, fruto da abstinência (voluntária, to bem) de crusader kings/the sims/netflix, espero que seja útil a alguém. Ainda ta na versão betinha kkkk fique a vontade para dar o seu feedback!

OBS: tenha em vista que, assim como no amor, colocar muitos critérios dificulta o processo. Todavia, caso ache é mais certeiro.
""")

idioma = st.radio(
  "Em qual idioma você quer ler?",
  ["Indiferente", "Português", "Inglês"]
)


st.image("https://i.pinimg.com/1200x/f2/69/85/f26985561563a70723451899a1be681a.jpg")

tamanho = st.radio(
    "Qual o tamanho do livro?",
    ["Curto (<200 páginas)", "Médio (200–500)", "Longo (>500)", "Indiferente"]
)


st.image("https://i.pinimg.com/1200x/8b/9d/a7/8b9da7de3e56d0978a08d9a43ac1cf9f.jpg")

origem = st.multiselect(
    "Pensou no continente natal do autor? Você pode selecionar vários... (ah, Rússia e Turquia são asiáticas aqui)",
    ["África", "América latina", "América do Norte", "Ásia", "Europa", "Oceania" ]
)


st.image("https://i.pinimg.com/736x/5d/2d/e6/5d2de6b91231c9435d701fdbf88935c3.jpg")

romance = st.radio(
  "O amor romântico é o tema principal?",
  ["Não sei, eis a questão...", "Sim", "Não"]
)

st.image("https://i.pinimg.com/736x/cf/16/d8/cf16d850dcdedc7a295e87e0516ab03d.jpg")

tempo = st.radio(
  "Você prefere histórias:",
  ["Ambientadas no passado (<1900)", "No mundo contemporâneo (licença poética)", "Futuristas", "Tanto faz"]
)

st.image("https://i.pinimg.com/736x/fc/6f/d8/fc6fd80d7bfd04aa80023bc0cefa6eb8.jpg")


religiao = st.radio(
  "Tá procurando um livro religioso?",
  ["Não pensei nisso ainda", "Sim", "Não"]
)

classico = st.radio(
  "Sua futura leitura é considerada um clássico da literatura nacional/mundial?",
  ["Indiferente", "Sim", "Não"]
)


st.image("https://i.pinimg.com/736x/fb/41/fd/fb41fdd7fca3128bd234e8077ffb465a.jpg")

pensamento = st.radio(
  "Você quer um livro que:",
  ["Dê pra ler com o cérebro desligado", "Faça refletir um pouco", "Exija atenção total", "Não sei"]
)


st.image("https://i.pinimg.com/1200x/a8/3e/41/a83e416a7fb0d74e522a2296860e0742.jpg")

critica = st.radio(
  "A história tem um quê de crítica social? Nem que seja velada, assim, no off (salve salve turma do pagode)",
  ["Não sei dizer", "Sim", "Não"]
)


st.write ("A base de dados se restringe ao meu acervo de livros... daqui uns anos será maior, se Deus quiser.")

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

#filtro origem colocar global tamebm?????#
  if origem:
    filtro = filtro[filtro["GEOGRAFIA"].isin(origem)]

#filtro romance#
  if romance == "Sim":
    filtro = filtro[filtro["LOVE"] == "S"]
  elif romance == "Não":
    filtro = filtro[filtro["LOVE"] == "N"]

#filtro tempo#
  if tempo == "Ambientadas no passado (<1900)":
    filtro = filtro[filtro["TEMPO"] == "P"]
  elif tempo == "No mundo contemporâneo (licença poética)":
    filtro = filtro[filtro["TEMPO"] == "C"]
  elif tempo == "Futurista":
    filtro = filtro[filtro["TEMPO"] == "F"]
  
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

#filtro pensamento#
  if pensamento == "Dê pra ler com o cérebro desligado":
    filtro = filtro[filtro["PENSAMENTO"] == "D"]
  elif pensamento == "Faça refletir um pouco":
    filtro = filtro[filtro["PENSAMENTO"] == "P"]
  elif pensamento == "Exija atenção total":
    filtro = filtro[filtro["PENSAMENTO"] == "T"]
    
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
<style>
@keyframes fadeUp {{
  from {{
    opacity: 0;
    transform: translateY(15px);
  }}
  to {{
    opacity: 1;
    transform: translateY(0);
  }}
}}

.book-card {{
  animation: fadeUp 0.6s ease-out;
}}
</style>

<div class="book-card" style="
    border:1px solid #ddd;
    border-radius:14px;
    padding:20px;
    background-color:#f9f9f9;
    color:#1F2937;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
">
  <h3>📖 {livro['TÍTULO']}</h3>
  <p><b>Autor:</b> {livro['AUTOR']}</p>
  <p><b>Tema:</b> {livro['GERAL']}</p>
  <p><b>Subtema:</b> {livro['PARTICULAR']}</p>
  <p><b>País:</b> {livro['PAIS']}</p>
  <p><b>Século:</b> {livro['SECULO']}</p>
  <p><b>Ano da edição:</b> {livro['ANO']}</p>
  <p><b>Páginas:</b> {livro['PÁG']}</p>
</div>
""", unsafe_allow_html=True)

  st.info("Caso queira gerar outra recomendação, clique novamente.")
