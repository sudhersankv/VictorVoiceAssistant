import os
# External libraries for core functionality:
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

# Environment variable management
from dotenv import load_dotenv 


def load_mind():
    load_dotenv()
    groq_api_key = os.getenv('GROQ_API_KEY')
    model = 'Llama3-8b-8192'

    conversational_memory_length = 5
    memory = ConversationBufferMemory(k=conversational_memory_length)
    chat_history = []      
    groq_chat = ChatGroq(
        groq_api_key = groq_api_key,
        model_name = model,
    )
    conversation = ConversationChain(
        llm = groq_chat,
        memory = memory
    )
    return groq_api_key, model, memory, chat_history, conversation