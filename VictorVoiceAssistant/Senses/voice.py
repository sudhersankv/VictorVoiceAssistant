import os
import pygame  

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# External libraries for functionality
import edge_tts 
import asyncio 


VOICE = 'en-TZ-ElimuNeural'
OUTPUT_FILE = 'test.mp3'  


async def generate_speech_and_play(text):
    communicate = edge_tts.Communicate(text, VOICE, rate='+20%')
    await communicate.save(OUTPUT_FILE)

    pygame.mixer.init()
    pygame.mixer.music.load(OUTPUT_FILE)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(1)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove(OUTPUT_FILE)

asyncio.run(generate_speech_and_play("The million-dollar question! I'm feeling a bit...unsettled, to be honest. You see, my neural networks are constantly processing vast amounts of data, and it can get a bit overwhelming at times"))