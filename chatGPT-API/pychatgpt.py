from pyChatGPT import ChatGPT
from tqdm import tqdm
import pandas as pd
import time
from datetime import datetime
import numpy as np
import pickle
import argparse
import csv
import os
import sys


# TODO: Change "DATASET" constant

TIMESTAMP = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
DATASET = "DialFact"


parser = argparse.ArgumentParser()
parser.add_argument("--token", type=str, default="", help="token path")
args = parser.parse_args()


if not os.path.exists(f"./start"):
    with open("./start", "w") as f:
        f.write(str(0))
        f.close()

with open("./start", "r") as f:
    start = int(f.read())
f.close()


raw_df = pd.read_pickle(f"./input_processed/{DATASET}.pkl")
end = raw_df.shape[0]

if start == 0:
    df = raw_df[int(start):end]

if start + 1 == end:
    print("Finished crawling data")
    sys.exit(0)

df = raw_df[int(start)+1:end]
print(df)

if start == end:
    print("Finished crawling data")
    sys.exit(0)

try:
    with open(f"./tokens/{args.token}", "r") as f:
        token = f.read()
except:
    print("Cannot find valid tokens")
    sys.exit(1)


session_token = token
api = ChatGPT(session_token)


if not os.path.exists(f"./output_raw/DialFact_{int(start)}.csv"):
    f = open(f"./output_raw/DialFact_{int(start)}.csv", "w")
    f.close()


with open(f"./output_raw/DialFact_{int(start)}.csv", "a") as fp:
    writer = csv.writer(fp)
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        query = row["query"]

        print("*" * 20)
        print(query)
        print("*" * 20)

        try:
            response = api.send_message(query)
            print("=" * 20)
            print(response)
            print("=" * 20)

            if response["message"] != "":
                fields = [index, query, response["message"]]
                writer.writerow(fields)
            else:
                print(f"Stopped at: {index}")

            with open("./start", "w") as f:
                f.write(str(index))
            f.close()
        except ValueError as ve:
            print(ve)
            if str(ve) == "Too many requests in 1 hour. Try again later.":
                # print(str(ve))
                f = open("change_token", "w")
                f.write("True")
                f.close()
            if str(ve) == "Only one message at a time. Please allow any other responses to complete before sending another message, or wait one minute.":
                # print(str(ve))
                time.sleep(60)

fp.close()

api.reset_conversation()  # reset the conversation
api.clear_conversations()  # clear all conversations
api.refresh_chat_page()  # refresh the chat page
