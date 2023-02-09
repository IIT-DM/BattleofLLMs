import numpy as np
import pandas as pd
import tensorflow as tf
import transformers
from train_BERT import DataLoader

load_model = tf.keras.models.load_model('./sematic-similarity.h5')
labels = ["contradiction", "entailment", "neutral"]
def check_similarity(sentence1, sentence2):
    sentences = np.array([[str(sentence1), str(sentence2)]])
    test_data = DataLoader(sentences, labels=None, batch_size=1, shuffle=False, include_labels=False)

    proba = load_model.predict(test_data[0])[0]
    idx = np.argmax(proba)
    proba = f"{proba[idx]: .2f}%"
    pred = labels[idx]
    print(pred)
    # print(proba)
    return proba, pred, sentence1, sentence2

df = pd.read_csv('../DialFact_withResponse.csv')
# df = df.iloc[10:]
# df["answer_prompt"] = df["context"].astype(str) + " " + df["question"].astype(str) + " The answer is "+ df["answer"].astype(str)
# df["chatgpt_prompt"] = df["text"].astype(str) + " " + df["question"].astype(str) + " The answer is "+ df["chatgpt_response"].astype(str)

answer_prompt = []
for i in df['response']:
    answer_prompt.append(i)

chatgpt_prompt = []
for j in df['chatgpt_response']:
    chatgpt_prompt.append(i)

similarity_p=[]
label_p=[]
for i, j in zip(answer_prompt, chatgpt_prompt):
    similarity = check_similarity(i, j)[0]
    label = check_similarity(i, j)[1]
    print(label)
    similarity_p.append(similarity)
    label_p.append(label)


df["BERT similarity"] = similarity_p
df["NLI Label"] = label_p

df.to_csv("DialFact_withGoldenR_label.csv", index=True)
