#!/usr/bin/python3
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import base64
from langchain_core.messages import HumanMessage

# load environment variables--> API keys from the 
load_dotenv()

# the llm setup---> take note of the model_name that has vision
api_key=os.getenv("GROQ_API_KEY")

llm=ChatGroq(
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="qwen/qwen3.6-27b"
)

# first step is to convert the image to base64
# We will send it to the API in this format
def encode_image(image):
    # open the image in binary and encode it
    with open(image, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
# Call the function to send encoded image data to LLM
def describe_image(image):
    # get encoded image data
    encoded_image=encode_image(image)

    # Prepare prompt
    message= HumanMessage(
        content=[
            {
                "type":"text",
                "text":"Describe this Image. Be brief"
            },
            {
                "type":"image_url",
                # fetching image locally. If not local use: 'url':'https:<url_for_iamge>'
                "image_url":{
                    "url":f"data:image/png;base64,{encoded_image}"
                }
            }
        ]
    )

    # call our LLM passing the above prompt with our encoded image data
    result=llm.invoke([message])

    # get the content part. Thats what we care about to be returned
    result=result.content

    # Remove reasoning section--> we want to reduce the amount of text returned--> reducing token 
    if "</think>" in result:
        result = result.split("</think>", 1)[1].strip()

    return result


# --------Not A must to add this: Is for testing if function Works-----------
print("[+] Starting description......")
# Make sure image is inthe same directory as vision.py . If not use the filepath below
response=describe_image("my_quiz.png")

print(f"\nImage Data: {response}")

"""
=================This is the result I got=======================
cmd>> python vision.py
[+] Starting description......

Image Data: The image displays a text-based "Python Quick Quiz" containing three questions. The text is shown twice: once at the top and again in a zoomed-in view below. The questions are:

1.  Define Python in one line
2.  Difference between variable and constant in one line
3.  Write code to get input from the user and add the two numbers

"""