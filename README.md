# Medical_ChatBot   


## Overview :

Developed a Medical Chatbot aimed at simplifying healthcare information retrieval. Our system efficiently processes PDF files, extracting key medical data and creating text chunks. These chunks are then embedded to build a semantic index in our cloud-hosted Pinecone vector store. When users ask questions, the chatbot converts them into query embeddings and searches the knowledge base for relevant answers. Leveraging advanced ranking algorithms and LLM models like Llama2, enhanced through prompt engineering techniques, the chatbot delivers precise responses, providing users with accurate medical information on demand.


## How to run the code :

1. Clone this repository :
```ini
git clone https://github.com/Louai-AZ/Medical_ChatBot.git
```

2. Create a virtual environment and activate it :
```ini
conda create -n medchatEnv python=3.8 -y ;
conda activate medchatEnv ;
```

3. Install the dependencies : 
```ini
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Pinecone credentials as follows :

```ini
PINECONE_API_KEY = ""
PINECONE_API_ENV = ""
index_name=""
```

5. Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:
llama-2-7b-chat.ggmlv3.q4_0.bin

## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

6. Run :
```ini
python store_index.py
python app.py
```
7. Open up localhost 



## TechStack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone


