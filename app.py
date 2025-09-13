# import os
# from dotenv import load_dotenv
# import chainlit as cl
# import google.generativeai as genai 

# load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-2.0-flash")

# @cl.on_message
# async def message_handler(message: cl.Message):
#     user_input = message.content 
#     response = model.generate_content(user_input)
#     await cl.Message(content=response.text).send()



import os
from dotenv import load_dotenv
import chainlit as cl
import google.generativeai as genai  

# Load environment variables
load_dotenv()

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✨ Choose your Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# 💌 Chat handler
@cl.on_message
async def message_handler(message: cl.Message):
    user_input = message.content.strip()  # It will take the user input 
    response = model.generate_content(user_input)  
    bot_reply = f"💖 BooBot: {response.text}"  
    await cl.Message(content=bot_reply).send() # Reply to the user qns/input
