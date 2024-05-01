import os
# faster whisper model provides better inference speeds than whisper
from faster_whisper import WhisperModel

def voice_to_text():
    
    model = WhisperModel('small', device = 'cpu', compute_type = 'int8')
    segments,_ = model.transcribe('Temp1.wav')
    text = ''.join(segment.text for segment in segments)
    final_result = text
    os.remove('Temp1.wav')
    return final_result
