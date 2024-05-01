import os

# Custom modules
from Senses.voice import generate_speech_and_play
from Senses.ears import speechreco, listen_for_wakeword, is_similar
from Senses.voice_to_text import voice_to_text
from Brain.personality import define_personality
from Brain.mind import load_mind

# External libraries
import speech_recognition as sr
import numpy as np
import asyncio


os.environ['KMP_DUPLICATE_LIB_OK']='True'

greetings, goodbye, formatted_prompt, quit_words = define_personality()

groq_api_key, model, memory, chat_history, conversation = load_mind()

quit_words = ['quit', 'stop', 'bye', 'thank you', 'thanks']    

def check_for_quit_word(word):
    quit_detected = False
    for quit_word in quit_words:
            if is_similar(word, quit_word):
                random_goodbye = np.random.choice(goodbye)
                asyncio.run(generate_speech_and_play(random_goodbye))
                quit_detected = True
                return quit_detected

count = 0
while True:
    with sr.Microphone() as source:
            listen_for_wakeword(source)
            random_greeting = np.random.choice(greetings)
            asyncio.run(generate_speech_and_play(random_greeting))
                
    while True:
        speechreco()
        user_question = voice_to_text()
        print('You: {user_question}', user_question)
        quit_detected = check_for_quit_word(user_question)
        if quit_detected:
            source = False
            break
            
        if count ==0:
            response = conversation(formatted_prompt)
        response = conversation(user_question)
        message = {'human': user_question, 'AI': response}
        chat_history.append(message)
        print('Viktor: ', response['response'])
        latest_response = response['response']
        asyncio.run(generate_speech_and_play(latest_response))        
        count+=1

