import streamlit as st

from dotenv import load_dotenv
import os 
load_dotenv()

from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate,load_prompt

model=ChatOpenAI(model='gpt-4-turbo')

st.title('Summarize your research paper')


paper_input=st.selectbox("select research paper Name",["Attention is All you need","BERT:pre training of deep bidirectional transformers","GPT-3:Language models are few sho learners","Diffusion Models beat GANs on image synthesis"])

col1,col2=st.columns(2)

with col1:
   select_type=st.selectbox("Select Explanation you want:",['Beginer-Friendly','code-oriented','Mathmetical','Technical'])
   
with col2:
    
    dsc=st.radio("describe style you want:",['short (1-2) paragraphs','Medium (3-5) paragraphs','Long (details) paragraph'])
    


st.slider("variation you want from previous response",0,2,0)



template=load_prompt('template.json')
     

if st.button('summary'):
    chain=template| model
    
    result=chain.invoke(
        
           {
         "paper_input":paper_input,
         "select_type":select_type,
         "dsc":dsc
        }
        
    )
    
 
    
    
    st.write(result.content)