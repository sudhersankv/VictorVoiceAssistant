**VictorVoiceAssistant**

A powerful voice assistant built using the cutting-edge LLM Llama 3 8B and Groq's inference engine for lightning-fast responses.

**Key Features**

* **Wake Word Detection:** Reliably detects your custom wake word to initiate interactions. Fuzzy string matching (fuzzywuzzy) is used for flexibility.
* **High-Speed Speech Transcription:** Employs Faster Whisper for accurate and rapid speech-to-text conversion.
* **Blazing Fast LLM Inference:** Leverages Groq's LPU™ Inference Engine for state-of-the-art performance with the Llama 3 8B model.
* **Natural Voice Responses:** Provides smooth and human-like text-to-speech (TTS) output.
* **Quit Word Functionality:** Gracefully ends interactions with a predefined quit word.
* **Customizable Greetings and Goodbyes:** Personalize your assistant with tailored responses for wake words and quit words.

**Main Modules**

* **Speech Recognition:** Captures and stores audio input for processing.
* **Wake Word Identification:** Employs basic transcription along with fuzzy matching (fuzzywuzzy) to identify your chosen wake word.
* **Faster Whisper:**  Handles speech-to-text conversion for interactions after the wake word.
* **Groq LPU™ Inference Engine:** Powers the Llama 3 8B LLM for super-fast responses.
* **Edge TTS:** Converts text responses into natural-sounding speech.

**Getting Started**

1. **Install Dependencies:**
   ```bash
   pip install requirements.txt
2. **Set up Groq LPU™ Inference Engine:**

   *  Groq : https://groq.com
   *  Obtain a Groq API Key: Sign up for a Groq account and get your API key.
   *  Configure your project to use Groq: Set up the necessary environment variables or configuration files to connect to the Groq LPU™ Inference Engine. 

3. **Configure Wake Word and Quit Word:**
   *  Edit settings within the project.
  
4. **Run the Assistant:**
   ```bash
   python app.py 


