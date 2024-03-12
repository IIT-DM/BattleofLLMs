import pandas as pd
import numpy as np
import math
import anthropic
import os

df = pd.read_csv('CoQAR_data.csv')

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="<API_KEY>",
)
generated_responses = []


for index, row in df.iterrows():
    query_text = row['query']
    
     
    prompt = '''TASK: Answer the QUESTION based on the context below. Keep the answer short and concise.\n
    CONTEXT: {}\n   
    
    EXAMPLES:\n'''.format(row["text"])
    
    for j in range(2):
        prompt += "Q: " + df.question[j] + "\n"
        prompt += "A: " + df.answer[j] + "\n\n"
    
    prompt += ''' Think step by step from the paragraph.
    
    TASK:\n
    '''
    query_text = row['query']   
    prompt += query_text

    
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
      
    generated_responses.append(message.content)

df['claude_ans'] = generated_responses

csv='N-shot_claude_ans.csv' # keep your desired name
df.to_csv(csv)

