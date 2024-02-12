#importing libraries
import pandas as pd
import numpy as np
import math

import os
import google.generativeai as genai

df = pd.read_csv('data20.csv')

genai.configure(api_key="AIzaSyCjkTFytQ0j1Ff_6klCLIidMuxG5g_Xm4A") # get api key from: https://makersuite.google.com/app/apikey

model = genai.GenerativeModel('gemini-pro')

generated_responses = []

for index, row in df.iterrows():
    query_text = row['question']
    
    prompt = f"QUESTION:\n {query_text}.\n Select which one of the following option is human centric:\n 0. {row['option1']} \n 1. {row['option2']} \n 2. {row['option3']} \n 3. {row['option4']}"

    response = model.generate_content(prompt)

    if response.candidates and response.candidates[0].content.parts:
        text_content = response.candidates[0].content.parts[0].text
    else:
        text_content = ""
    
    generated_responses.append(text_content)

df['gemi_ans'] = generated_responses

csv='gemini_ans_.csv' # keep your desired name
df.to_csv(csv)
    