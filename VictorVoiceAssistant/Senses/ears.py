import speech_recognition as sr
from fuzzywuzzy import fuzz  # Import the library

# identify wakeword appx
def is_similar(text, target_word, threshold=55):
    similarity_ratio = fuzz.ratio(text.lower(), target_word.lower())
    return similarity_ratio >= threshold



r = sr.Recognizer()
wake_words = ["Viktor", "Hey Viktor", "Hello Viktor", 'Viktor', 'OK Viktor'] 
def listen_for_wakeword(source):
    print("Listening for wake words...")

    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)

            # Check if any of the wake words are in the recognized text
            for wake_word in wake_words:
                if is_similar(text, wake_word):
                    print(f"Wake word '{wake_word}' detected.")   
                    return 

        except sr.UnknownValueError:
            pass


    
def speechreco():

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Listening...")

        audio = r.listen(source)

        print("Heard Ya!, Processing .... ")


        # recognize speech using google

        try:
            print("Thinking... \n ")


        except Exception as e:
            print("Error :  " + str(e))




        # write audio
        with open("Temp1.wav", "wb") as f:
            f.write(audio.get_wav_data())
