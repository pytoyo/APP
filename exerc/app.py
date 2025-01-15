import streamlit as st

# Função para a página inicial
def home():
    st.title("Bem-vindo ao Nosso Site!")
    st.image("https://via.placeholder.com/800x400", caption="Imagem de exemplo para a página inicial")
    st.write("""
    Este é um exemplo de site criado com Streamlit. 
    Explore as outras páginas para saber mais sobre nós e entrar em contato!
    """)

# Função para a página "Sobre Nós"
def sobre_nos():
    st.title("Sobre Nós")
    st.image("https://via.placeholder.com/600x300", caption="Nossa equipe em ação")
    st.write("""
    Somos uma empresa dedicada a fornecer soluções inovadoras. 
    Nossa missão é entregar qualidade e superar as expectativas dos nossos clientes.

    ### Nossa História
    Fundada em 2020, nossa empresa cresceu rapidamente graças ao apoio dos nossos clientes e ao trabalho duro da nossa equipe.

    ### Nossos Valores
    - Excelência
    - Inovação
    - Compromisso com o cliente
    """)

# Função para a página "Contato"
def contato():
    st.title("Contato")
    st.image("https://via.placeholder.com/600x300", caption="Estamos prontos para atender você")
    st.write("""
    Entre em contato conosco pelos seguintes meios:

    - **Email:** contato@exemplo.com
    - **Telefone:** (11) 1234-5678

    Ou visite nosso endereço:
    """)
    # Inserir mapa do Google Maps
    st.map(data=None, zoom=None, use_container_width=True)
    st.write("Endereço: Rua MJ João Soares de Mendonça, 590, Cananéia,SP")

# Configurações do layout
st.sidebar.title("Navegação")

# Menu de navegação
menu = st.sidebar.radio("Ir para:", ["Home", "Sobre Nós", "Endereço"])

# Exibir a página correspondente ao menu selecionado
if menu == "Home":
    home()
elif menu == "Sobre Nós":
    sobre_nos()
elif menu == "Contato":
    contato()
