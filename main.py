from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
shop_key = os.getenv("SHOP_KEY")

client = OpenAI(api_key=shop_key, base_url="https://api.shopaikey.com/v1")

# task 1
def call_api(request):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": request}
        ]
    )

    return(response.choices[0].message.content)


print(call_api("Hello! what day is this in vietnam"))