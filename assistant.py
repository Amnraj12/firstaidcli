import os

from gtts import gTTS

def text_to_speech_with_gtts(text, language, output_file):
    audioobj=gTTS(text=text,lang=language,slow=False)
    audioobj.save(output_file)

import elevenlabs
from elevenlabs.client import ElevenLabs

def text_to_speech_with_elevenlabs(input_text, language, output_file):
    ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY')
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    response = client.generate(
                                    text=input_text, 
                                     voice="Aria",
                                        output_format="mp3_22050_32",
                                        model="eleven_turbo_v2"
                                     )
    elevenlabs.save(response , output_file)






import subprocess
from pydub import AudioSegment
def text_to_speech(input_text, language, output_file):
    if os.path.exists("response.mp3"):
        os.remove("response.mp3")
        print("Removed existing audio file: response.mp3")
    if language=="kn" or language=="hi":
        text_to_speech_with_gtts(input_text, language, output_file)
        print("created new response.mp3")
        wav_file = "response.wav"
        audio = AudioSegment.from_mp3(output_file)
        audio.export(wav_file, format="wav")
        subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_file}").PlaySync();'])
        
       
  
    elif language=="en":
        text_to_speech_with_elevenlabs(input_text, language, output_file)
        wav_file = "response.wav"
        audio = AudioSegment.from_mp3(output_file)
        audio.export(wav_file, format="wav")
        subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_file}").PlaySync();'])
        
    


