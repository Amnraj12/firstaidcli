import os 
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image

from groq import Groq

def compare (query, model):
    client = Groq()
    messages = [
        {
            "role": "user", 
            "content": [
                {
                    "type": "text",
                    "text": query
                }
            ]
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,  
        model=model
    )
    return chat_completion.choices[0].message.content

def putting_query_with_image(query, model, encoded_image):
    client = Groq()
    messages = [
        {
            "role": "user", 
            "content": [
                {
                    "type": "text",
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



def putting_query_without_image(query, model):
    client = Groq()
    messages = [
        {
            "role": "user", 
            "content": [
                {
                    "type": "text",
                    "text": query
                }
            ]
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content