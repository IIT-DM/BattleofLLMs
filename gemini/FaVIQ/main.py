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
    
    prompt = f"QUESTION:\n {query_text}.\n "

    response = model.generate_content(prompt)

    if response.candidates and response.candidates[0].content.parts:
        text_content = response.candidates[0].content.parts[0].text
    else:
        text_content = ""
    
    generated_responses.append(text_content)

df['gemi_ans'] = generated_responses

csv='gemini_ans_faviq.csv' # keep your desired name
df.to_csv(csv)
    