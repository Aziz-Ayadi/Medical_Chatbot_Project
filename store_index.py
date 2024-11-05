from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from dotenv import load_dotenv
import os
from pinecone import Pinecone, ServerlessSpec  
from langchain_pinecone import PineconeVectorStore



load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
index_name = os.environ.get('index_name')


extracted_data = load_pdf("./data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()



pc = Pinecone(api_key=PINECONE_API_KEY,environment=PINECONE_API_ENV)  

if index_name not in pc.list_indexes().names():
    print(index_name , " Does not exist !") 
    pc.create_index(
        name=index_name,
        dimension=384,
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-west-2'
        )
    )
    
index = pc.Index(index_name) 

vectorstore = PineconeVectorStore(
    index=index,
    pinecone_api_key = PINECONE_API_KEY,
    embedding=embeddings,
    index_name=index_name
)

docsearch = vectorstore.add_texts(texts=[t.page_content for t in text_chunks])