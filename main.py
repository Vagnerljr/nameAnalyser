import streamlit as st
import requests
import pandas as pd



def getName():
    name = st.text_input('Digite o nome que deseja pesquisar:')
    if name:
        return name
    else:
        st.warning('Digite um nome para começar')
    return name

def fetchData(name):    
    URL_API = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}'    
    response = requests.get(URL_API)
    return response.json()


def main():
    st.title('Descubra quantos nomes existem durante os anos')
    dicNomes = {}     
    name = getName()
    if not name:
        st.stop()
    data = fetchData(name)
       
    for item in data[0]['res']:
            periodo = item['periodo']
            frequencia = item['frequencia']            
            dicNomes[periodo] = frequencia
           
    dfNome = pd.DataFrame(list(dicNomes.items()), columns=["Período", "Frequência"])
    dfNome["Período"] = dfNome["Período"].str.replace(r'[\[\[]', '', regex=True) \
                                     .str.replace(r'[\[\]]', '', regex=True) \
                                     .str.replace(',', ' - ')
    
    infoNome = st.dataframe(dfNome, hide_index=True)

    return infoNome
    

if __name__ == "__main__":
    main()





















    





