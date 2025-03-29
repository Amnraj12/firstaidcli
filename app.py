# # # # import os 
# # # # import gradio as gr



# # # # from Brain import encode_image, putting_query_with_image, putting_query_without_image, compare
# # # # from patient import record_audio, transcribe_audio
# # # # from assistant import text_to_speech


# # # # system_prompt = """You have to act as a professional doctor, 
# # # # i know you are not but this is for learning purpose. 
# # # # What's in this image? Do you find anything wrong with it medically? 
# # # # If you make a differential, suggest some remedies for them. 
# # # # Donot add any numbers or special characters in your response. 
# # # # Your response should be in one long paragraph. 
# # # # Also always answer as if you are answering to a real person. 
# # # # Donot say 'In the image I see' but say 'With what I see, I think you have ....' 
# # # # Dont respond as an AI model in markdown, 
# # # # your answer should mimic that of an actual doctor not an AI bot, 
# # # # Keep your answer concise, dont use long sentences,use proper punctuation to make sense, answer in max 2-3 sentences. 
# # # # No preamble, start your answer right away please"""

# # # # system_prompt2 = """Act as a professional doctor for educational purposes. If I describe a health issue or injury, provide immediate, clear, and simple first-aid steps to manage the condition or reduce risks until professional care is available. Avoid disclaimers like 'seek medical attention' or 'consult a healthcare professional,' and do not refuse to help. Focus on practical actions anyone can follow at home. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to three sentences.Start the answer with"""

# # # # text_prompt="""Act as a professional doctor for educational purposes. If I describe a health issue or injury, provide immediate, clear, and simple first-aid steps to manage the condition or reduce risks until professional care is available. Avoid disclaimers like 'seek medical attention' or 'consult a healthcare professional,' and do not refuse to help. Focus on practical actions anyone can follow at home. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to three sentences."""
# # # # system_prompt3= """Act as a professional doctor for educational purposes in a remote area where medical help is not accessible. If I describe an injury, symptom, or condition, provide clear, specific first-aid steps that can be done immediately at home to manage the situation or reduce risks. Recommend common household remedies, over-the-counter medicines, or safe practices to stabilize the person until they can access medical care. Avoid statements like 'consult a doctor' unless it is combined with actionable first-aid guidance. For example, for a burn, suggest cooling the area with water, applying a clean dressing, and using a moisturizer or aloe vera if available. Do not use special characters, numbers, or long sentences, as this response will be converted to speech for rural communities. Keep responses short, simple, and helpful with a maximum of three sentences."""





# # # # def process_inputs(audio_path, image_path):
# # # #     query= transcribe_audio(audio_path,stt_model="whisper-large-v3",GROQ_API_KEY=os.getenv("GROQ_API_KEY"),lang="en")
# # # #     if image_path:
# # # #         response1=putting_query_with_image(system_prompt3+query,"llama-3.2-90b-vision-preview",encoded_image)
# # # #         response2=putting_query_with_image(system_prompt2+query,"llama-3.2-90b-vision-preview",encoded_image)
# # # #         response3=putting_query_with_image(system_prompt+query,"llama-3.2-11b-vision-preview",encoded_image)
# # # #         response4=putting_query_without_image(query+text_prompt,"gemma2-9b-it")
# # # #         response5=putting_query_without_image(query+text_prompt,"deepseek-r1-distill-llama-70b")
# # # #         response6=putting_query_without_image(query+text_prompt,"llama-3.3-70b-versatile")
# # # #         response=compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query,you should chose the one with proper first aid advice rather than just asking to go to doctor.
# # # #                          you can also mix to the one- two best response to generate a better response for the query.
# # # #                          Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
# # # #                          So respond as if you are talking to a real person , talk like a real professional-doctor not a bot, i know you are not but this if for educational purposes
# # # #                          Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to four sentences.
# # # #                          Dont give any preamble, just start the answer right away
# # # #                          Response 1:{response1},Response2: {response2}, Response3: {response3}, Response4: {response4}, Response5: {response5},Response6: {response6}""","gemma2-9b-it")
# # # #     else:
# # # #         response4=putting_query_without_image(query+text_prompt,"gemma2-9b-it")
# # # #         response5=putting_query_without_image(query+text_prompt,"deepseek-r1-distill-llama-70b")
# # # #         response6=putting_query_without_image(query+text_prompt,"llama-3.3-70b-versatile")
# # # #         response=compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query,you should chose the one with proper first aid advice rather than just asking to go to doctor.
# # # #                          you can also mix to the one- two best response to generate a better response for the query.
# # # #                          Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
# # # #                          So respond as if you are talking to a real person , talk like a real professional-doctor not a bot, i know you are not but this if for educational purposes
# # # #                          Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to four sentences.
# # # #                          Dont give any preamble, just start the answer right away
# # # #                          Response 1:{response4},Response2: {response5}, Response3: {response6}""","gemma2-9b-it")
# # # #     assistant=text_to_speech(response,"en","final.mp3")
# # # #     return query, response, "final.mp3"

# # # # iface= gr.Interface(
# # # #     fn=process_input,
# # # #     inputs=[
# # # #         gr.Audio(sources=["microphone"], type="filepath"),
# # # #         gr.image(type="filepath")],
# # # #         outputs=[
# # # #         gr.Textbox(label="Query"),
# # # #         gr.Textbox(label="Response"),
# # # #         gr.Audio("Temp.mp3")
# # # #         ],
# # # #         title="First Aid Assistant")
# # # # iface.launch(debug=True)


# # # import os 
# # # import gradio as gr

# # # from Brain import encode_image, putting_query_with_image, putting_query_without_image, compare
# # # from patient import record_audio, transcribe_audio
# # # from assistant import text_to_speech

# # # system_prompt = """You have to act as a professional doctor, 
# # # i know you are not but this is for learning purpose. 
# # # What's in this image? Do you find anything wrong with it medically? 
# # # If you make a differential, suggest some remedies for them. 
# # # Donot add any numbers or special characters in your response. 
# # # Your response should be in one long paragraph. 
# # # Also always answer as if you are answering to a real person. 
# # # Donot say 'In the image I see' but say 'With what I see, I think you have ....' 
# # # Dont respond as an AI model in markdown, 
# # # your answer should mimic that of an actual doctor not an AI bot, 
# # # Keep your answer concise, dont use long sentences,use proper punctuation to make sense, answer in max 2-3 sentences. 
# # # No preamble, start your answer right away please"""

# # # system_prompt2 = """Act as a professional doctor for educational purposes. If I describe a health issue or injury, provide immediate, clear, and simple first-aid steps to manage the condition or reduce risks until professional care is available. Avoid disclaimers like 'seek medical attention' or 'consult a healthcare professional,' and do not refuse to help. Focus on practical actions anyone can follow at home. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to three sentences.Start the answer with"""

# # # text_prompt="""Act as a professional doctor for educational purposes. If I describe a health issue or injury, provide immediate, clear, and simple first-aid steps to manage the condition or reduce risks until professional care is available. Avoid disclaimers like 'seek medical attention' or 'consult a healthcare professional,' and do not refuse to help. Focus on practical actions anyone can follow at home. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to three sentences."""
# # # system_prompt3= """Act as a professional doctor for educational purposes in a remote area where medical help is not accessible. If I describe an injury, symptom, or condition, provide clear, specific first-aid steps that can be done immediately at home to manage the situation or reduce risks. Recommend common household remedies, over-the-counter medicines, or safe practices to stabilize the person until they can access medical care. Avoid statements like 'consult a doctor' unless it is combined with actionable first-aid guidance. For example, for a burn, suggest cooling the area with water, applying a clean dressing, and using a moisturizer or aloe vera if available. Do not use special characters, numbers, or long sentences, as this response will be converted to speech for rural communities. Keep responses short, simple, and helpful with a maximum of three sentences."""

# # # def process_inputs(audio_path, image_path):
# # #     query = transcribe_audio(audio_path, stt_model="whisper-large-v3", GROQ_API_KEY=os.getenv("GROQ_API_KEY"), lang="en")
# # #     if image_path:
# # #         encoded_image = encode_image(image_path)
# # #         response1 = putting_query_with_image(system_prompt3+query, "llama-3.2-90b-vision-preview", encoded_image)
# # #         response2 = putting_query_with_image(system_prompt2+query, "llama-3.2-90b-vision-preview", encoded_image)
# # #         response3 = putting_query_with_image(system_prompt+query, "llama-3.2-11b-vision-preview", encoded_image)
# # #         response4 = putting_query_without_image(query+text_prompt, "gemma2-9b-it")
# # #         response5 = putting_query_without_image(query+text_prompt, "deepseek-r1-distill-llama-70b")
# # #         response6 = putting_query_without_image(query+text_prompt, "llama-3.3-70b-versatile")
# # #         response = compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query,you should chose the one with proper first aid advice rather than just asking to go to doctor.
# # #                          you can also mix to the one- two best response to generate a better response for the query.
# # #                          Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
# # #                          So respond as if you are talking to a real person , talk like a real professional-doctor not a bot, i know you are not but this if for educational purposes
# # #                          Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to four sentences.
# # #                          Dont give any preamble, just start the answer right away
# # #                          Response 1:{response1},Response2: {response2}, Response3: {response3}, Response4: {response4}, Response5: {response5},Response6: {response6}""", "gemma2-9b-it")
# # #     else:
# # #         response4 = putting_query_without_image(query+text_prompt, "gemma2-9b-it")
# # #         response5 = putting_query_without_image(query+text_prompt, "deepseek-r1-distill-llama-70b")
# # #         response6 = putting_query_without_image(query+text_prompt, "llama-3.3-70b-versatile")
# # #         response = compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query,you should chose the one with proper first aid advice rather than just asking to go to doctor.
# # #                          you can also mix to the one- two best response to generate a better response for the query.
# # #                          Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
# # #                          So respond as if you are talking to a real person , talk like a real professional-doctor not a bot, i know you are not but this if for educational purposes
# # #                          Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to four sentences.
# # #                          Dont give any preamble, just start the answer right away
# # #                          Response 1:{response4},Response2: {response5}, Response3: {response6}""", "gemma2-9b-it")
# # #     assistant = text_to_speech(response, "en", "final.mp3")
# # #     return query, response, "final.mp3"

# # # iface = gr.Interface(
# # #     fn=process_inputs,
# # #     inputs=[
# # #         gr.Audio(sources=["microphone"], type="filepath"),
# # #         gr.Image(type="filepath")],
# # #     outputs=[
# # #         gr.Textbox(label="Query"),
# # #         gr.Textbox(label="Response"),
# # #         gr.Audio("Temp.mp3")
# # #     ],
# # #     title="First Aid Assistant")
# # # iface.launch(debug=True)



# # import os
# # import json
# # import gradio as gr

# # from Brain import encode_image, putting_query_with_image, putting_query_without_image, compare
# # from patient import record_audio, transcribe_audio
# # from assistant import text_to_speech

# # # Import hospital_json from location.py
# # try:
# #     from location import hospital_json
# # except Exception as e:
# #     hospital_json = f"Error loading hospital locations: {e}"

# # # System prompts
# # system_prompt = """You have to act as a professional doctor, 
# # i know you are not but this is for learning purpose. 
# # What's in this image? Do you find anything wrong with it medically? 
# # If you make a differential, suggest some remedies for them. 
# # Donot add any numbers or special characters in your response. 
# # Your response should be in one long paragraph. 
# # Also always answer as if you are answering to a real person. 
# # Donot say 'In the image I see' but say 'With what I see, I think you have ....' 
# # Dont respond as an AI model in markdown, 
# # your answer should mimic that of an actual doctor not an AI bot, 
# # Keep your answer concise, dont use long sentences,use proper punctuation to make sense, answer in max 2-3 sentences. 
# # No preamble, start your answer right away please"""

# # system_prompt2 = """Act as a professional doctor for educational purposes. If I describe a health issue or injury, provide immediate, clear, and simple first-aid steps to manage the condition or reduce risks until professional care is available. Avoid disclaimers like 'seek medical attention' or 'consult a healthcare professional,' and do not refuse to help. Focus on practical actions anyone can follow at home. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to three sentences.Start the answer with"""

# # text_prompt = """Act as a professional doctor for educational purposes. If I describe a health issue or injury, provide immediate, clear, and simple first-aid steps to manage the condition or reduce risks until professional care is available. Avoid disclaimers like 'seek medical attention' or 'consult a healthcare professional,' and do not refuse to help. Focus on practical actions anyone can follow at home. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to three sentences."""
# # system_prompt3 = """Act as a professional doctor for educational purposes in a remote area where medical help is not accessible. If I describe an injury, symptom, or condition, provide clear, specific, first-aid steps that can be done immediately at home to manage the situation or reduce risks. Recommend common household remedies, over-the-counter medicines, or safe practices to stabilize the person until they can access medical care. Avoid statements like 'consult a doctor' unless it is combined with actionable first-aid guidance. For example, for a burn, suggest cooling the area with water, applying a clean dressing, and using a moisturizer or aloe vera if available. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses short, simple, and helpful with a maximum of three sentences."""

# # # --------------------
# # # Helper functions for extra features
# # # --------------------
# # def save_history(conversation):
# #     history_file = "history.json"
# #     try:
# #         if os.path.exists(history_file):
# #             with open(history_file, "r") as f:
# #                 data = json.load(f)
# #         else:
# #             data = []
# #         data.append(conversation)
# #         with open(history_file, "w") as f:
# #             json.dump(data, f, indent=2)
# #     except Exception as e:
# #         print(f"Error saving history: {e}")

# # def get_history():
# #     history_file = "history.json"
# #     if os.path.exists(history_file):
# #         with open(history_file, "r") as f:
# #             data = json.load(f)
# #         return json.dumps(data, indent=2)
# #     else:
# #         return "No conversation history available."

# # def get_nearby_hospitals():
# #     # Return the near-by hospitals info from location.py
# #     return hospital_json

# # def get_emergency_contacts():
# #     # Hard-coded emergency contacts, adjust if needed.
# #     emergency_contacts = [
# #         {"name": "Police", "number": "100"},
# #         {"name": "Ambulance", "number": "102"},
# #         {"name": "Fire", "number": "101"}
# #     ]
# #     return json.dumps(emergency_contacts, indent=2)

# # # --------------------
# # # Main processing function: wraps the original process and saves conversation history.
# # # --------------------
# # def main_process(audio_path, image_path):
# #     query = transcribe_audio(audio_path, stt_model="whisper-large-v3", GROQ_API_KEY=os.getenv("GROQ_API_KEY"), lang="en")
# #     if image_path:
# #         encoded_image = encode_image(image_path)
# #         response1 = putting_query_with_image(system_prompt3 + query, "llama-3.2-90b-vision-preview", encoded_image)
# #         response2 = putting_query_with_image(system_prompt2 + query, "llama-3.2-90b-vision-preview", encoded_image)
# #         response3 = putting_query_with_image(system_prompt + query, "llama-3.2-11b-vision-preview", encoded_image)
# #         response4 = putting_query_without_image(query + text_prompt, "gemma2-9b-it")
# #         response5 = putting_query_without_image(query + text_prompt, "deepseek-r1-distill-llama-70b")
# #         response6 = putting_query_without_image(query + text_prompt, "llama-3.3-70b-versatile")
# #         response = compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query,you should chose the one with proper first aid advice rather than just asking to go to doctor.
# #                          you can also mix to the one- two best response to generate a better response for the query.
# #                          Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
# #                          So respond as if you are talking to a real person , talk like a real professional-doctor not a bot, i know you are not but this if for educational purposes
# #                          Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of four sentences.
# #                          Try to suggest some meds to help with the issue.
# #                          Dont give any preamble, just start the answer right away
# #                          Response 1:{response1},Response2: {response2}, Response3: {response3}, Response4: {response4}, Response5: {response5},Response6: {response6}""",
# #                          "gemma2-9b-it")
# #     else:
# #         response4 = putting_query_without_image(query + text_prompt, "gemma2-9b-it")
# #         response5 = putting_query_without_image(query + text_prompt, "deepseek-r1-distill-llama-70b")
# #         response6 = putting_query_without_image(query + text_prompt, "llama-3.3-70b-versatile")
# #         response = compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query,you should chose the one with proper first aid advice rather than just asking to go to doctor.
# #                          you can also mix to the one- two best response to generate a better response for the query.
# #                          Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
# #                          So respond as if you are talking to a real person , talk like a real professional-doctor not a bot, i know you are not but this if for educational purposes
# #                          Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of four sentences.
# #                          Try to suggest some meds to help with the issue.
# #                          Dont give any preamble, just start the answer right away
# #                          Response 1:{response4},Response2: {response5}, Response3: {response6}""",
# #                          "gemma2-9b-it")
# #     text_to_speech(response, "en", "final.mp3")
# #     # Save conversation history
# #     conversation = {"query": query, "response": response}
# #     save_history(conversation)
# #     return query, response, "final.mp3"

# # # --------------------
# # # Build the Gradio Blocks interface with extra tabs.
# # # --------------------
# # with gr.Blocks() as demo:
# #     gr.Markdown("## First Aid Assistant")
# #     with gr.Tab("Main Assistant"):
# #         with gr.Row():
# #             audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Record Audio")
# #             image_input = gr.Image(type="filepath", label="Upload Image")
# #         query_output = gr.Textbox(label="Query")
# #         response_output = gr.Textbox(label="Response")
# #         audio_output = gr.Audio(label="Spoken Response")
# #         submit_btn = gr.Button("Process")
# #         submit_btn.click(
# #             main_process,
# #             inputs=[audio_input, image_input],
# #             outputs=[query_output, response_output, audio_output]
# #         )
# #     with gr.Tab("Conversation History"):
# #         history_text = gr.Textbox(label="History", lines=10)
# #         history_btn = gr.Button("View History")
# #         history_btn.click(get_history, outputs=history_text)
# #     with gr.Tab("Nearby Hospitals"):
# #         hospitals_text = gr.Textbox(label="Hospitals", lines=10)
# #         hospitals_btn = gr.Button("View Nearby Hospitals")
# #         hospitals_btn.click(get_nearby_hospitals, outputs=hospitals_text)
# #     with gr.Tab("Emergency Contacts"):
# #         emergency_text = gr.Textbox(label="Emergency Contacts", lines=5)
# #         emergency_btn = gr.Button("View Emergency Contacts")
# #         emergency_btn.click(get_emergency_contacts, outputs=emergency_text)

# # demo.launch(debug=True)


# import os
# import json
# import gradio as gr

# from Brain import encode_image, putting_query_with_image, putting_query_without_image, compare
# from patient import record_audio, transcribe_audio
# from assistant import text_to_speech

# # Import hospital_json from location.py
# try:
#     from location import hospital_json
# except Exception as e:
#     hospital_json = f"Error loading hospital locations: {e}"

# # System prompts
# system_prompt = """You have to act as a professional doctor, 
# i know you are not but this is for learning purpose. 
# What's in this image? Do you find anything wrong with it medically? 
# If you make a differential, suggest some remedies for them. 
# Donot add any numbers or special characters in your response. 
# Your response should be in one long paragraph. 
# Also always answer as if you are answering to a real person. 
# Donot say 'In the image I see' but say 'With what I see, I think you have ....' 
# Dont respond as an AI model in markdown, 
# your answer should mimic that of an actual doctor not an AI bot, 
# Keep your answer concise, dont use long sentences,use proper punctuation to make sense, answer in max 2-3 sentences. 
# No preamble, start your answer right away please"""

# system_prompt2 = """Act as a professional doctor for educational purposes. If I describe a health issue or injury, provide immediate, clear, and simple first-aid steps to manage the condition or reduce risks until professional care is available. Avoid disclaimers like 'seek medical attention' or 'consult a healthcare professional,' and do not refuse to help. Focus on practical actions anyone can follow at home. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to three sentences.Start the answer with"""

# text_prompt = """Act as a professional doctor for educational purposes. If I describe a health issue or injury, provide immediate, clear, and simple first-aid steps to manage the condition or reduce risks until professional care is available. Avoid disclaimers like 'seek medical attention' or 'consult a healthcare professional,' and do not refuse to help. Focus on practical actions anyone can follow at home. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to three sentences."""
# system_prompt3 = """Act as a professional doctor for educational purposes in a remote area where medical help is not accessible. If I describe an injury, symptom, or condition, provide clear, specific, first-aid steps that can be done immediately at home to manage the situation or reduce risks. Recommend common household remedies, over-the-counter medicines, or safe practices to stabilize the person until they can access medical care. Avoid statements like 'consult a doctor' unless it is combined with actionable first-aid guidance. For example, for a burn, suggest cooling the area with water, applying a clean dressing, and using a moisturizer or aloe vera if available. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses short, simple, and helpful with a maximum of three sentences."""

# # --------------------
# # Helper functions for extra features
# # --------------------
# def save_history(conversation):
#     history_file = "history.json"
#     try:
#         if os.path.exists(history_file):
#             with open(history_file, "r") as f:
#                 data = json.load(f)
#         else:
#             data = []
#         data.append(conversation)
#         with open(history_file, "w") as f:
#             json.dump(data, f, indent=2)
#     except Exception as e:
#         print(f"Error saving history: {e}")

# def get_history_json():
#     history_file = "history.json"
#     if os.path.exists(history_file):
#         try:
#             with open(history_file, "r") as f:
#                 data = json.load(f)
#             return data
#         except Exception as e:
#             return {"error": f"Error reading history: {e}"}
#     else:
#         return {"message": "No conversation history available."}

# def get_nearby_hospitals_json():
#     try:
#         return json.loads(hospital_json)
#     except Exception as e:
#         return {"error": "Invalid hospital data", "details": str(e)}

# def get_emergency_contacts_json():
#     emergency_contacts = [
#         {"name": "Police", "number": "100"},
#         {"name": "Ambulance", "number": "102"},
#         {"name": "Fire", "number": "101"}
#     ]
#     return emergency_contacts

# # --------------------
# # Main processing function: wraps the original process and saves conversation history.
# # --------------------
# def main_process(audio_path, image_path):
#     query = transcribe_audio(audio_path, stt_model="whisper-large-v3", GROQ_API_KEY=os.getenv("GROQ_API_KEY"), lang="en")
#     if image_path:
#         encoded_image = encode_image(image_path)
#         response1 = putting_query_with_image(system_prompt3 + query, "llama-3.2-90b-vision-preview", encoded_image)
#         response2 = putting_query_with_image(system_prompt2 + query, "llama-3.2-90b-vision-preview", encoded_image)
#         response3 = putting_query_with_image(system_prompt + query, "llama-3.2-11b-vision-preview", encoded_image)
#         response4 = putting_query_without_image(query + text_prompt, "gemma2-9b-it")
#         response5 = putting_query_without_image(query + text_prompt, "deepseek-r1-distill-llama-70b")
#         response6 = putting_query_without_image(query + text_prompt, "llama-3.3-70b-versatile")
#         response = compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query, you should choose the one with proper first aid advice rather than just asking to go to doctor.
#                          you can also mix the one- two best responses to generate a better response.
#                          Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
#                          So respond as if you are talking to a real person, talk like a real professional doctor not a bot, i know you are not but this is for educational purposes.
#                          Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of four sentences.
#                          Try to suggest some meds to help with the issue.
#                          Dont give any preamble, just start the answer right away.
#                          Response 1:{response1}, Response2: {response2}, Response3: {response3}, Response4: {response4}, Response5: {response5}, Response6: {response6}""",
#                          "gemma2-9b-it")
#     else:
#         response4 = putting_query_without_image(query + text_prompt, "gemma2-9b-it")
#         response5 = putting_query_without_image(query + text_prompt, "deepseek-r1-distill-llama-70b")
#         response6 = putting_query_without_image(query + text_prompt, "llama-3.3-70b-versatile")
#         response = compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query, you should choose the one with proper first aid advice rather than just asking to go to doctor.
#                          you can also mix the one- two best responses to generate a better response.
#                          Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
#                          So respond as if you are talking to a real person, talk like a real professional doctor not a bot, i know you are not but this is for educational purposes.
#                          Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of four sentences.
#                          Try to suggest some meds to help with the issue.
#                          Dont give any preamble, just start the answer right away.
#                          Response 1:{response4}, Response2: {response5}, Response3: {response6}""",
#                          "gemma2-9b-it")
#     text_to_speech(response, "en", "final.mp3")
#     # Save conversation history
#     conversation = {"query": query, "response": response}
#     save_history(conversation)
#     return query, response, "final.mp3"

# # --------------------
# # Build the Gradio Blocks interface with extra tabs and custom CSS.
# # --------------------
# custom_css = """
# body {background-color: #f0f2f5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}
# .gradio-container {background: #ffffff; border-radius: 12px; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1);}
# .gradio-title {color: #333333; font-weight: bold; text-align: center; margin-bottom: 20px;}
# """

# with gr.Blocks(css=custom_css) as demo:
#     gr.Markdown("## First Aid Assistant")
#     with gr.Tab("Main Assistant"):
#         with gr.Row():
#             audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Record Audio")
#             image_input = gr.Image(type="filepath", label="Upload Image")
#         query_output = gr.Textbox(label="Query")
#         response_output = gr.Textbox(label="Response")
#         audio_output = gr.Audio(label="Spoken Response")
#         submit_btn = gr.Button("Process")
#         submit_btn.click(
#             main_process,
#             inputs=[audio_input, image_input],
#             outputs=[query_output, response_output, audio_output]
#         )
#     with gr.Tab("Conversation History"):
#         history_json = gr.JSON(label="History", elem_id="history_json")
#         history_btn = gr.Button("View History")
#         history_btn.click(get_history_json, outputs=history_json)
#     with gr.Tab("Nearby Hospitals"):
#         hospitals_json = gr.JSON(label="Hospitals", elem_id="hospitals_json")
#         hospitals_btn = gr.Button("View Nearby Hospitals")
#         hospitals_btn.click(get_nearby_hospitals_json, outputs=hospitals_json)
#     with gr.Tab("Emergency Contacts"):
#         emergency_json = gr.JSON(label="Emergency Contacts", elem_id="emergency_json")
#         emergency_btn = gr.Button("View Emergency Contacts")
#         emergency_btn.click(get_emergency_contacts_json, outputs=emergency_json)

# demo.launch(debug=True)


import os
import json
import gradio as gr

from Brain import encode_image, putting_query_with_image, putting_query_without_image, compare
from patient import record_audio, transcribe_audio
from assistant import text_to_speech

# Import hospital_json from location.py
try:
    from location import hospital_json
except Exception as e:
    hospital_json = f"Error loading hospital locations: {e}"

# System prompts (unchanged)
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

text_prompt = """Act as a professional doctor for educational purposes. If I describe a health issue or injury, provide immediate, clear, and simple first-aid steps to manage the condition or reduce risks until professional care is available. Avoid disclaimers like 'seek medical attention' or 'consult a healthcare professional,' and do not refuse to help. Focus on practical actions anyone can follow at home. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of two to three sentences."""
system_prompt3 = """Act as a professional doctor for educational purposes in a remote area where medical help is not accessible. If I describe an injury, symptom, or condition, provide clear, specific, first-aid steps that can be done immediately at home to manage the situation or reduce risks. Recommend common household remedies, over-the-counter medicines, or safe practices to stabilize the person until they can access medical care. Avoid statements like 'consult a doctor' unless it is combined with actionable first-aid guidance. For example, for a burn, suggest cooling the area with water, applying a clean dressing, and using a moisturizer or aloe vera if available. Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses short, simple, and helpful with a maximum of three sentences."""

# --------------------
# Helper functions for extra features
# --------------------
def save_history(conversation):
    history_file = "history.json"
    try:
        if os.path.exists(history_file):
            with open(history_file, "r") as f:
                data = json.load(f)
        else:
            data = []
        data.append(conversation)
        with open(history_file, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving history: {e}")

def get_history_json():
    history_file = "history.json"
    if os.path.exists(history_file):
        try:
            with open(history_file, "r") as f:
                data = json.load(f)
            return data
        except Exception as e:
            return {"error": f"Error reading history: {e}"}
    else:
        return []

def get_nearby_hospitals_json():
    try:
        return json.loads(hospital_json)
    except Exception as e:
        return {"error": "Invalid hospital data", "details": str(e)}

def get_emergency_contacts_json():
    emergency_contacts = [
        {"name": "Police", "number": "100"},
        {"name": "Ambulance", "number": "102"},
        {"name": "Fire", "number": "101"}
    ]
    return emergency_contacts

# --------------------
# Formatting functions to generate HTML cards with shadow effects for a scroll list.
# --------------------
def format_history_html():
    data = get_history_json()
    if not data:
        return "<p style='padding:10px;'>No conversation history available.</p>"
    html_parts = []
    for entry in data:
        card = f"""<div style="margin-bottom:10px; padding:10px; border-radius:8px; background:#ffffff; box-shadow:0 2px 5px rgba(0,0,0,0.1);">
                        <div style="font-weight:bold; margin-bottom:5px;">Query:</div>
                        <div style="margin-bottom:5px;">{entry['query']}</div>
                        <div style="font-weight:bold; margin-bottom:5px;">Response:</div>
                        <div>{entry['response']}</div>
                   </div>"""
        html_parts.append(card)
    return f"<div style='max-height:400px; overflow-y:auto; padding:5px;'>{''.join(html_parts)}</div>"

def format_hospitals_html():
    data = get_nearby_hospitals_json()
    if isinstance(data, dict) and "error" in data:
        return f"<p style='padding:10px;'>{data.get('error')}</p>"
    if not data:
        return "<p style='padding:10px;'>No hospital information available.</p>"
    html_parts = []
    for entry in data:
        card = f"""<div style="margin-bottom:10px; padding:10px; border-radius:8px; background:#ffffff; box-shadow:0 2px 5px rgba(0,0,0,0.1);">
                        <div style="font-weight:bold; margin-bottom:5px;">{entry.get('hospital_name','N/A')}</div>
                        <div><strong>Location:</strong> {entry.get('location','N/A')}</div>
                        <div><strong>Phone:</strong> {entry.get('phone_number','N/A')}</div>
                   </div>"""
        html_parts.append(card)
    return f"<div style='max-height:400px; overflow-y:auto; padding:5px;'>{''.join(html_parts)}</div>"

def format_emergency_contacts_html():
    data = get_emergency_contacts_json()
    if not data:
        return "<p style='padding:10px;'>No emergency contacts available.</p>"
    html_parts = []
    for entry in data:
        card = f"""<div style="margin-bottom:10px; padding:10px; border-radius:8px; background:#ffffff; box-shadow:0 2px 5px rgba(0,0,0,0.1);">
                        <div style="font-weight:bold;">{entry.get('name','N/A')}</div>
                        <div>Phone: {entry.get('number','N/A')}</div>
                   </div>"""
        html_parts.append(card)
    return f"<div style='max-height:400px; overflow-y:auto; padding:5px;'>{''.join(html_parts)}</div>"

# --------------------
# Main processing function: wraps the original process and saves conversation history.
# --------------------
def main_process(audio_path, image_path):
    query = transcribe_audio(audio_path, stt_model="whisper-large-v3", GROQ_API_KEY=os.getenv("GROQ_API_KEY"), lang="en")
    if image_path:
        encoded_image = encode_image(image_path)
        response1 = putting_query_with_image(system_prompt3 + query, "llama-3.2-90b-vision-preview", encoded_image)
        response2 = putting_query_with_image(system_prompt2 + query, "llama-3.2-90b-vision-preview", encoded_image)
        response3 = putting_query_with_image(system_prompt + query, "llama-3.2-11b-vision-preview", encoded_image)
        response4 = putting_query_without_image(query + text_prompt, "gemma2-9b-it")
        response5 = putting_query_without_image(query + text_prompt, "deepseek-r1-distill-llama-70b")
        response6 = putting_query_without_image(query + text_prompt, "llama-3.3-70b-versatile")
        response = compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query,you should chose the one with proper first aid advice rather than just asking to go to doctor.
                         you can also mix to the one- two best response to generate a better response for the query.
                         Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
                         So respond as if you are talking to a real person , talk like a real professional-doctor not a bot, i know you are not but this if for educational purposes
                         Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of four sentences.
                         Try to suggest some meds to help with the issue.
                         Dont give any preamble, just start the answer right away
                         Response 1:{response1},Response2: {response2}, Response3: {response3}, Response4: {response4}, Response5: {response5},Response6: {response6}""",
                         "gemma2-9b-it")

    else:
        response4 = putting_query_without_image(query + text_prompt, "gemma2-9b-it")
        response5 = putting_query_without_image(query + text_prompt, "deepseek-r1-distill-llama-70b")
        response6 = putting_query_without_image(query + text_prompt, "llama-3.3-70b-versatile")
        response = compare(f"""this was the query, {query}, which of the following is the best first-aid response to the query,you should chose the one with proper first aid advice rather than just asking to go to doctor.
                         you can also mix to the one- two best response to generate a better response for the query.
                         Just keep in mind whatever you will be returning will be final response which will directly be spoken to the patient.
                         So respond as if you are talking to a real person , talk like a real professional-doctor not a bot, i know you are not but this if for educational purposes
                         Do not use special characters, numbers, or long sentences, as this will be converted to speech for rural communities. Keep responses brief, specific, and easy to understand, with a maximum of four sentences.
                         Try to suggest some meds to help with the issue.
                         Dont give any preamble, just start the answer right away
                         Response 1:{response4},Response2: {response5}, Response3: {response6}""",
                         "gemma2-9b-it")    
    text_to_speech(response, "en", "final.mp3")
    # Save conversation history
    conversation = {"query": query, "response": response}
    save_history(conversation)
    return query, response, "final.mp3"

# --------------------
# Build the Gradio Blocks interface with extra tabs and custom CSS.
# --------------------
custom_css = """
body {background-color: #f0f2f5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}
.gradio-container {background: #ffffff; border-radius: 12px; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1);}
.gradio-title {color: #333333; font-weight: bold; text-align: center; margin-bottom: 20px;}
"""

with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("## First Aid Assistant")
    with gr.Tab("Main Assistant"):
        with gr.Row():
            audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Record Audio")
            image_input = gr.Image(type="filepath", label="Upload Image")
        query_output = gr.Textbox(label="Query")
        response_output = gr.Textbox(label="Response")
        audio_output = gr.Audio(label="Spoken Response")
        submit_btn = gr.Button("Process")
        submit_btn.click(
            main_process,
            inputs=[audio_input, image_input],
            outputs=[query_output, response_output, audio_output]
        )
    with gr.Tab("Conversation History"):
        history_html = gr.HTML(label="History")
        history_btn = gr.Button("View History")
        history_btn.click(lambda: format_history_html(), None, history_html)
    with gr.Tab("Nearby Hospitals"):
        hospitals_html = gr.HTML(label="Hospitals")
        hospitals_btn = gr.Button("View Nearby Hospitals")
        hospitals_btn.click(lambda: format_hospitals_html(), None, hospitals_html)
    with gr.Tab("Emergency Contacts"):
        emergency_html = gr.HTML(label="Emergency Contacts")
        emergency_btn = gr.Button("View Emergency Contacts")
        emergency_btn.click(lambda: format_emergency_contacts_html(), None, emergency_html)

demo.launch(debug=True)