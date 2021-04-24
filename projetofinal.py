import streamlit as st
import pandas as pd
from scipy.spatial.distance import cdist

st.sidebar.image('images.jpg', width=None) 
st.sidebar.title ('-PROJETO-')   
st.sidebar.subheader ( "HELP MY HAIR *_foi desenvolvido para te ajudar naquele momento de indecisão diante de tantas opções de produtos para cabelos_*..." )

st.sidebar.subheader ("*_Basta responder as perguntinhas ao lado que lhe mostrarei o produto ideal para seu tipo de cabelo!!_*")

st.sidebar.subheader ("*_Ao final da minha recomendação, clique nas opções e aguarde. Você estará a um passo do seu novo produto queridinho ; D _*")

st.image('images (1).jpg', width=None)

st.title('HELP MY HAIR')
st.subheader('Selecione uma opção')
tipo_cabelo_input = st.selectbox('TIPO DE CABELO',['Oleoso','Seco','Misto'])

def merge(dict1,*dicts):
    for dict2 in dicts:
        dict1.update(dict2)
    return dict1



def tipo_cabelo(tipo):
    resposta = {}
   
    if tipo == 'Oleoso':
        resposta['Oleoso']=[1]
        resposta['Seco']=[0]
        resposta['Misto']=[0]
       
    elif tipo == 'Seco':
        resposta['Oleoso']=[0]
        resposta['Seco']=[1]
        resposta['Misto']=[0]
        
        
    elif tipo == 'Misto':
        resposta['Oleoso']=[0.5]
        resposta['Seco']=[0.5]
        resposta['Misto']=[1]
        
    
    return resposta

genero_input=st.selectbox("OPÇÃO POR GÊNERO? Selecione", ['Feminino', 'Masculino', 'Indiferente'])
def genero(genero):
    resposta = {}
    
    if genero == 'Feminino':
        resposta['Feminino']=[1]
        resposta['Masculino']=[0]
        resposta['Indiferente']=[0]
        
    elif genero == 'Masculino':
        resposta['Feminino']=[0]
        resposta['Masculino']=[1]
        resposta['Indiferente']=[0]
        
    elif genero == 'Indiferente':
        resposta['Feminino']=[0]
        resposta['Masculino']=[0]
        resposta['Indiferente']=[1]
        
    
    return resposta

acao_input=st.selectbox("AÇÃO ESPERADA? Selecione", ["Controlar a queda", "Controlar o volume", "Controle de Caspa", "Definir cachos e crespos", "Reduzir Frizz"])
def acao(acao):
    resposta = {}
    
    if acao == 'Controlar a queda':
        resposta['Controlar a queda']=[1]
        resposta['Controlar o volume']=[0]
        resposta['Controle de Caspa']=[0]
        resposta['Definir cachos e crespos']=[0]
        resposta['Reduzir Frizz']=[0]
        
    elif acao == 'Controlar o volume':
        resposta['Controlar a queda']=[0]
        resposta['Controlar o volume']=[1]
        resposta['Controle de Caspa']=[0]
        resposta['Definir cachos e crespos']=[0]
        resposta['Reduzir Frizz']=[0]

    elif acao == 'Controle de Caspa':
        resposta['Controlar a queda']=[0]
        resposta['Controlar o volume']=[0]
        resposta['Controle de Caspa']=[1]
        resposta['Definir cachos e crespos']=[0]
        resposta['Reduzir Frizz']=[0]

    elif acao == 'Definir cachos e crespos':
        resposta['Controlar a queda']=[0]
        resposta['Controlar o volume']=[0]
        resposta['Controle de Caspa']=[0]
        resposta['Definir cachos e crespos']=[1]
        resposta['Reduzir Frizz']=[0]
        
    elif acao == 'Reduzir Frizz':
        resposta['Controlar a queda']=[0]
        resposta['Controlar o volume']=[0]
        resposta['Controle de Caspa']=[0]
        resposta['Definir cachos e crespos']=[0]
        resposta['Reduzir Frizz']=[1]
        
    
    return resposta

preço_input=st.selectbox("FAIXA DE PREÇO? Selecione", ["Custo Acessivel", "Custo Medio", "Custo Premium"])
def preço(preço):
    resposta = {}
    
    if preço == 'Custo Acessivel':
        resposta['Custo Acessivel']=[1]
        resposta['Custo Medio']=[0]
        resposta['Custo Premium']=[0]
        
    elif preço == 'Custo Medio':
        resposta['Custo Acessivel']=[0]
        resposta['Custo Medio']=[1]
        resposta['Custo Premium']=[0]
        
    elif preço == 'Custo Premium':
        resposta['Custo Acessivel']=[0]
        resposta['Custo Medio']=[0]
        resposta['Custo Premium']=[1]
                
    
    return resposta

vegana_input=st.selectbox("PRODUTO VEGANO? Selecione", ["Sim", "Não", "Indiferente"])
def vegana(vegana):
    resposta = {}
    
    if vegana == 'Sim':
        resposta['vegana']=[1]
               
    elif vegana == 'Não':
        resposta['vegana']=[0]
    
    elif vegana == 'Indiferente':
        resposta['vegana']=[0.5]
         
    
    return resposta



dataframe = pd.read_csv('lully_resumo.csv')
df_index = pd.read_csv('df_index.csv')

apply_button = st.button("Me indique um produto")

if apply_button:

    saida1 = tipo_cabelo(tipo_cabelo_input)
    saida2 = genero(genero_input)
    saida3 = acao(acao_input)
    saida4 = preço(preço_input)
    saida5 = vegana(vegana_input)    

    
    saida_usuario = merge( saida1, saida2 , saida3, saida4 , saida5) 

       
   # input_usuario=pd.DataFrame(saida_usuario, index=[0])
   # st.write(input_usuario)

    input_saida_usuario=pd.DataFrame(saida_usuario)

      
    filtro = pd.DataFrame(cdist(input_saida_usuario,dataframe),columns=df_index).T.reset_index().rename(columns={'index':'nome',0:'distancia'})
    
    resultado=filtro.sort_values(by='distancia').head(3)["nome"]
    
    resultado1=list(filtro.sort_values(by='distancia').head(3)["nome"].values)
    for i in resultado1:
        saida = (i[1])
        saida=saida.replace(' ','+')
        saida=saida.replace('  ','+')
        saida=saida.replace('/','+')
        saida=saida.replace('\n ','+')
        st.markdown( f'[{i[1]}](https://www.google.com/search?q={saida}&sxsrf=ALeKk008wgREXMHFi36ucoa4li1xp11cGQ:1618970357279&source=lnms&tbm=shop&sa=X&ved=2ahUKEwi0h7DIno7wAhWVIbkGHYwKDmEQ_AUoBHoECAEQBg&biw=1920&bih=880)',unsafe_allow_html=True)

        
    



    
