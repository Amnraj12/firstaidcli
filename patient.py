import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def record_audio(file_path,timeout=20,phrase_time_limit=None):
    r=sr.Recognizer()
    try:
     with sr.Microphone() as source:
        logging.info("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source,duration=1)
        logging.info("Recording...")
        audio = r.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
        logging.info("Got it! Now to recognize it...") 
        wav=audio.get_wav_data()
        audio=AudioSegment.from_wav(BytesIO(wav))
        audio.export(file_path,format="mp3",bitrate="128k")
        logging.info(f"Saved audio to {file_path}")
    except Exception as e:
        logging.error(f"Error recording audio: {e}")
        return False
# audio_path="patient_audio.mp3"   

# record_audio(file_path=audio_path)


from groq import Groq
# GROQ_API_KEY=os.getenv("GROQ_API_KEY")
# stt_model="whisper-large-v3"
def transcribe_audio(audio_path,stt_model,GROQ_API_KEY,lang):    
    client=Groq(api_key=GROQ_API_KEY)
    audio_file=open(audio_path,"rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file = audio_file,
        language=lang
    )
    return(transcription.text)