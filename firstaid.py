from Brain import encode_image, putting_query_with_image, putting_query_without_image, compare
from patient import record_audio, transcribe_audio
from assistant import text_to_speech
import os
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
encoded_image=encode_image("broken-sprained-hand-2.png")
audio_path="patient_audio.mp3"

system_prompt = """You have to act as a professional doctor, 
i know you are not but this is for learning purpose. 
What's in this image? Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. 
Donot add any numbers or special characters in your response. 
Your response should be in one long paragraph. 
Also always answer as if you are answering to a real person. 
Donot say 'In the image I see' but say 'With what I see, I think you have ....' 
Dont respond as an AI model in markdown, 
your answer should mimic that of an actual doctor not an AI bot, 
Keep your answer concise, dont use long sentences,use proper punctuation to make sense, answer in max 2-3 sentences. 
No preamble, start your answer right away please"""

system_prompt2 = """Act as a professional doctor for educational purposes. If I describe a health issue or injury, provide immediate, clear, and simple first-aid steps to manage the condition or reduce risks until professional care is available. Avoid disclaimers like 'seek medical attention' or 'consult a healthcare professional,' and do not refuse to help. Focus on practical actions anyone can follow at home. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to three sentences.Start the answer with"""

text_prompt="""Act as a professional doctor for educational purposes. If I describe a health issue or injury, provide immediate, clear, and simple first-aid steps to manage the condition or reduce risks until professional care is available. Avoid disclaimers like 'seek medical attention' or 'consult a healthcare professional,' and do not refuse to help. Focus on practical actions anyone can follow at home. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to three sentences."""
system_prompt3= """Act as a professional doctor for educational purposes in a remote area where medical help is not accessible. If I describe an injury, symptom, or condition, provide clear, specific first-aid steps that can be done immediately at home to manage the situation or reduce risks. Recommend common household remedies, over-the-counter medicines, or safe practices to stabilize the person until they can access medical care. Avoid statements like 'consult a doctor' unless it is combined with actionable first-aid guidance. For example, for a burn, suggest cooling the area with water, applying a clean dressing, and using a moisturizer or aloe vera if available. Do not use special characters, numbers, or long sentences, as this response will be converted to speech for rural communities. Keep responses short, simple, and helpful with a maximum of three sentences."""

text=input("For text enter 1 else put 2:")
if text=="2":
    if os.path.exists(audio_path):
            os.remove(audio_path)
            # logging.info(f"Removed existing audio file: {audio_path}")
            print("Removed existing audio file: patient_audio.mp3")
    record_audio(file_path=audio_path)
    if os.path.exists(audio_path):
        query=transcribe_audio(audio_path,"whisper-large-v3",GROQ_API_KEY,"en")
        print(query)
        response1=putting_query_with_image(system_prompt3+query,"llama-3.2-90b-vision-preview",encoded_image)
        response2=putting_query_with_image(system_prompt2+query,"llama-3.2-90b-vision-preview",encoded_image)
        response3=putting_query_with_image(system_prompt+query,"llama-3.2-11b-vision-preview",encoded_image)
        response4=putting_query_without_image(query+text_prompt,"gemma2-9b-it")
        response5=putting_query_without_image(query+text_prompt,"deepseek-r1-distill-llama-70b")
        response6=putting_query_without_image(query+text_prompt,"llama-3.3-70b-versatile")
        response=compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query,you should chose the one with proper first aid advice rather than just asking to go to doctor.
                         you can also mix to the one- two best response to generate a better response for the query.
                         Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
                         So respond as if you are talking to a real person , talk like a real professional-doctor not a bot, i know you are not but this if for educational purposes
                         Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to four sentences.
                         Dont give any preamble, just start the answer right away
                         Response 1:{response1},Response2: {response2}, Response3: {response3}, Response4: {response4}, Response5: {response5},Response6: {response6}""","gemma2-9b-it")
        print(response)
        text_to_speech(response,"en","response.mp3")

    else:
        print("record failed")
else:
     query=input("enter your query:")
     response4=putting_query_without_image(query+text_prompt,"gemma2-9b-it")
     response5=putting_query_without_image(query+text_prompt,"deepseek-r1-distill-llama-70b")
     response6=putting_query_without_image(query+text_prompt,"llama-3.3-70b-versatile")
     response=compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query,you should chose the one with proper first aid advice rather than just asking to go to doctor.
                         you can also mix to the one- two best response to generate a better response for the query.
                         Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
                         So respond as if you are talking to a real person , talk like a real professional-doctor not a bot, i know you are not but this if for educational purposes
                         Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to four sentences.
                         Dont give any preamble, just start the answer right away
                         Response 1:{response4},Response2: {response5}, Response3: {response6}""","gemma2-9b-it")
        
     print(response)

     