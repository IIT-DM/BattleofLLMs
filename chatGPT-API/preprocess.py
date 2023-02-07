import json
from tqdm import tqdm
import pandas as pd
from datetime import datetime
import numpy as np
from math import ceil
import pickle


# TODO:
"""
Change this script according to your preprocessing needs.
Make sure to save your preprocessed dataset in ./input_processed as a pickle file.
You need to create a column named "query" inside your dataframe object.
"""

DATASET = "DialFact"
CHUNK = 50

with open("./input_raw/valid_split.jsonl") as f:
    context_id, id, context, response, response_label, type_label = [], [], [], [], [], []
    for line in tqdm(f, total=10436):
        l = json.loads(line)
        if l["data_type"] == "written" and l["type_label"] == "factual":
            context_id.append(l["context_id"])
            id.append(l["id"])
            context.append(l["context"][0])
            response.append(l["response"])
            response_label.append(l["response_label"])
            type_label.append(l["type_label"])

    df_valid = pd.DataFrame(list(zip(context_id, id, context, response, response_label, type_label)), columns=[
        "context_id", "id", "context", "response", "response_label", "type_label"])


with open("./input_raw/test_split.jsonl") as f:
    context_id, id, context, response, response_label, type_label = [], [], [], [], [], []
    for line in tqdm(f, total=11809):
        l = json.loads(line)
        if l["data_type"] == "written" and l["type_label"] == "factual":
            context_id.append(l["context_id"])
            id.append(l["id"])
            context.append(l["context"][0])
            response.append(l["response"])
            response_label.append(l["response_label"])
            type_label.append(l["type_label"])

    df_test = pd.DataFrame(list(zip(context_id, id, context, response, response_label, type_label)), columns=[
        "context_id", "id", "context", "response", "response_label", "type_label"])


df = pd.concat([df_valid, df_test])
df = df.loc[df["response_label"] == "SUPPORTS"]
df["query"] = df["context"].astype(str) + " " + df["response"].astype(str)
df = df.astype(str).drop_duplicates(["query"]).reset_index(drop=True)
print(df["query"])
df.to_pickle(f"./input_processed/{DATASET}.pkl")

