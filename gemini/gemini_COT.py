import pandas as pd
import numpy as np

import os
import google.generativeai as genai

df = pd.read_csv('CoQAR_data.csv')
genai.configure(api_key="<YOUR_API_KEY>")  # get api key from: https://makersuite.google.com/app/apikey
model = genai.GenerativeModel('gemini-pro')

generated_responses = []

for index, row in df.iterrows():
    query_text = row['text']
    
    prompt = '''TASK: Answer the QUESTION based on the context below. Keep the answer short and concise.
    CONTEXT: '''+query_text + '''
    QUESTION: '''+row['question'] +'''
    ANSWER: Think step by step from the paragraph.
    '''
 
    response = model.generate_content(prompt)

    if response.candidates and response.candidates[0].content.parts:
        text_content = response.candidates[0].content.parts[0].text
    else:
        text_content = ""
    
    generated_responses.append(text_content)

df['gemi_ans'] = generated_responses

csv='COT_gemini_ans.csv' # keep your desired name
df.to_csv(csv)

