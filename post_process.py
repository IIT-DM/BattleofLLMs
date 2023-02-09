import numpy as np
import pandas as pd
import math

data = pd.read_csv('./CoQA_withGoldenR.csv')

inputs = data['BERT similarity']
new_multiply=[]
for i in inputs:
    values = str(i)
    values = values[1:5]
    values = math.ceil(float(values)*100)
    values = str(values)
    new_multiply.append(values+"%")

data['BERT similarity percentage'] = new_multiply
del data['chatgpt_prompt']
del data['answer_prompt']
del data['BERT similarity']
print(data.head)
data.to_csv("CoQA_with_GR.csv", index=True)
