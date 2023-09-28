from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain, BaseCombineDocumentsChain
from langchain.tools.base import BaseTool
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import requests

class WebpageQATool(BaseTool):
    name = "query_webpage"
    description = "Busca una pagina web y devuelve la informacion relevante a la pregunta Usa bullet points para listar la respuesta"
    qa_chain : BaseCombineDocumentsChain

    def _run(self,url:str,question:str) -> str:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500,
        chunk_overlap  = 20,
        length_function = len,)

        response = requests.get(url)
        page_content = response.text
        print(page_content)
        docs = [Document(page_content=page_content,metadata={"source":url})]
        web_docs = text_splitter.split_documents(docs)
        results = []
        for i in range(0,len(web_docs),4):
            input_docs = web_docs[i:i+4]
            window_result = self.qa_chain({"input_documents":input_docs,"question":question},
                                          return_only_outputs=True)
            results.append(f'Response from window {i} - {window_result}')
        results_docs = [Document(page_content="\n".join(results),metadata={"source":url})]
        print(results_docs)
        return self.qa_chain({"input_documents":results_docs,"question":question},
                             return_only_outputs=True)

    async def _arun(self,url:str,question:str)->str:
        raise NotImplementedError