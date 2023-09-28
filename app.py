import streamlit as st 
from urllib.parse import urlparse
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
import openai
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain, BaseCombineDocumentsChain
from pydantic import Field
import asyncio

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
    result = query_website_tool.run(url,query)
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
    st.markdown("<h2 style='text-align: center; color:red;'>Ingresa la  URL del sitio 👇</h2>",
            unsafe_allow_html=True)
