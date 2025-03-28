import os 
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
#converter
import base64
# image_path="images.jpeg"
def encode_image(image_path):
    image_file= open(image_path, "rb")
    encoded_image= base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image
# encoded_image=encode_image(image_path)
#groq
# model = "llama-3.2-90b-vision-preview"
# query = "My hand got burnt, what should I do?"
from groq import Groq
def putting_query_with_image(query,model,encoded_image):
    client = Groq()
    messages=[
        {"role": "user", 
         "content": [
        {
            "type" : "text",
            "text": query


        },
        {
        "type": "image_url",
        "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}
    }
    ]
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content












# client = Groq()
# messages=[
#     {"role": "user", 
#      "content": [
#     {
#         "type" : "text",
#         "text": query


#     },
#     {
#     "type": "image_url",
#     "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}
# }
# ]
#     }
# ]

# chat_completion = client.chat.completions.create(
#     messages=messages,
#     model=model
# )
# print(chat_completion.choices[0].message.content)