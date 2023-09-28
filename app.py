import streamlit as st 
from urllib.parse import urlparse
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
import openai
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain, BaseCombineDocumentsChain
from pydantic import Field
import asyncio
from web_page_qatool import WebpageQATool
load_dotenv("token.env")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

@st.cache_resource
def get_url_name(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

def run_llm(url,query):
    llm = ChatOpenAI(temperature=0.5)
    query_website_tool = WebpageQATool(qa_chain=load_qa_with_sources_chain(llm))
    result = query_website_tool._run(url,query)
    return result

st.markdown("<h1 style='text-align: center; color: green;'>Traer infomacion  de la  Web 🦜 </h1>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: green;'>Desarrollado por <a href='https://github.com/AIAnytime'>AI Anytime with ❤️ </a></h3>",
            unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color:red;'>Ingresa la  URL del sitio 👇</h2>",
            unsafe_allow_html=True)

input_url = st.text_input("Ingresa URL")

if len(input_url)>0:
    url_name = get_url_name(input_url)
    st.info("Your URL is")
    st.write(url_name)
    st.markdown("<h2 style='text-align: center; color:green;'>Ingresa tu pregunta 👇</h2>",
            unsafe_allow_html=True)
    your_query = st.text_area("Enter your query")
    if st.button("Get answer"):
        if len(your_query)>0:
            st.info("Tu pregunta es " + your_query)
            final_answer = run_llm(input_url,your_query)
            st.write(final_answer)
    
