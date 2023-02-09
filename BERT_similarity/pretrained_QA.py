import pandas as pd
import numpy as np

import torch
import torch.nn as nn
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer


def data_processing_coqa(dataset):

    coqa = pd.read_json(dataset)
    del coqa["version"]
    coqa_columns = ["text","question","answer"]
    new_data_list = []
    for index, row in coqa.iterrows():
        for i in range(len(row["data"]["questions"])):
            temp = []
            temp.append(row["data"]["story"])
            temp.append(row["data"]["questions"][i]["input_text"])
            temp.append(row["data"]["answers"][i]["input_text"])
            new_data_list.append(temp)
    coqa_new = pd.DataFrame(new_data_list, columns=coqa_columns)
    return coqa_new.to_csv("CoQA_dataset.csv", index=False)



def evaluating_QA_BERT(question, text):
    load_model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    input_ids = tokenizer.encode(question, text)
    tokens = tokenizer.convert_ids_to_tokens(input_ids)
    seq_count = input_ids.index(tokenizer.sep_token_id)
    num_seg_a = seq_count+1
    num_seg_b = len(input_ids) - num_seg_a
    segment_ids = [0]*num_seg_a + [1]*num_seg_b
    assert len(segment_ids) == len(input_ids)
    
    output = load_model(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]))
    
    answer_start = torch.argmax(output.start_logits)
    answer_end = torch.argmax(output.end_logits)

    if answer_end >= answer_start:
        answer = tokens[answer_start]
        for i in range(answer_start+1, answer_end+1):
            if tokens[i][0:2] == "##":
                answer += tokens[i][2:]
            else:
                answer += " " + tokens[i]
                
    if answer.startswith("[CLS]"):
        answer = "Unable to find the answer to your question."
    print("\nAnswer:\n{}".format(answer.capitalize()))


text = """
My name is Aman. I am 22 years old.
I am an out-of-the-box thinker with excellent programming and analytical skills. 
I create deployable, learning-enabled, and resource-constrained systems. 
My research interests include computer vision, image processing, deep learning, and human-computer interaction. 
I love traveling to new places, eating different food, and connecting with new people. Tech enthusiast, explorer, and pacifist.
"""
question = "What are the research interests of Aman?"

# evaluating_QA_BERT(question, text)

