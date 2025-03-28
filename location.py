import os
import asyncio
from groq import Groq
from geopy.geocoders import Nominatim

import requests

def get_location():
    try:
        # Use an API to fetch location based on IP address
        response = requests.get("https://ipinfo.io")
        data = response.json()
        
        # Extract latitude and longitude from the location
        location = data.get("loc", "").split(",")
        latitude = location[0] if len(location) > 0 else "Unknown"
        longitude = location[1] if len(location) > 1 else "Unknown"
        
        return latitude, longitude
    except Exception as e:
        print(f"Error fetching location: {e}")
        return None, None

latitude, longitude = get_location()
if latitude and longitude:
    print(f"Your location:\nLatitude: {latitude}\nLongitude: {longitude}")
else:
    print("Unable to fetch location.")

location=latitude+","+longitude
query1= """Hey can you go search web and give me the Name of hospital, their phone numbers, and location.
MY location is: """

query2="""
give the list in a form of json file, No preamble , no follow up texts just give the information in json format
the format should be like this 

[
  {
    "hospital_name": "City General Hospital",
    "location": "MG Road, Bengaluru",
    "phone_number": "+91 80 1234 5678"
  },
  {
    "hospital_name": "Greenfield Specialty Clinic",
    "location": "Whitefield, Bengaluru",
    "phone_number": "+91 80 8765 4321"
  },
  {
    "hospital_name": "Sunrise Multi-Specialty Hospital",
    "location": "Koramangala, Bengaluru",
    "phone_number": "+91 80 2345 6789"
  }
]
Give the details of 10 nearest hospitals to my location, start with the nearest first and then the next nearest and so on.

"""
final_query=query1+location+query2

# print(final_query)
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
def location_query(query,model):
    client= Groq()
    messages=[
        {"role": "user", 
         "content": [
        {
            "type" : "text",
            "text": query


        },
    ]
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content

hospital_json=location_query(final_query,"gemma2-9b-it")
print(hospital_json)