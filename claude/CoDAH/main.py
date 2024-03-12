#importing libraries
import pandas as pd
import numpy as np
import math
import anthropic
import os

df = pd.read_csv('CoDAH_data.csv')

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="<API_KEY>",
)

generated_responses = []

for index, row in df.iterrows():
    query_text = row['question']
    
    prompt = f"QUESTION:\n {query_text}.\n Select which one of the following option is human centric:\n 0. {row['option1']} \n 1. {row['option2']} \n 2. {row['option3']} \n 3. {row['option4']}"


    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
        
    generated_responses.append(message.content)

df['claude_ans'] = generated_responses

csv='claude_ans_.csv' # keep your desired name
df.to_csv(csv)



    