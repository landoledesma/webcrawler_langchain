import streamlit as st 
from urllib.parse import urlparse
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
import openai
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain, BaseCombineDocumentsChain
from langchain.tools.base import BaseTool
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pydantic import Field
import asyncio
from langchain.docstore.document import Document
import requests

load_dotenv("token.env")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

@st.cache_resource
def get_url_name(url):
    parsed_url = urlparse(url)
    return parsed_url

st.markdown("<h1 style='text-align: center; color: green;'>Traer infomacion  de la  Web 🦜 </h1>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: green;'>Desarrollado por <a href='https://github.com/AIAnytime'>AI Anytime with ❤️ </a></h3>",
            unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color:red;'>Ingresa la  URL del sitio 👇</h2>",
            unsafe_allow_html=True)

input_url = st.text_input("Ingresa URL")

if len(input_url)>0:
    pass