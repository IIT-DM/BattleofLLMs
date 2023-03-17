from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu
import numpy as np
import pandas as pd
import sklearn
import itertools
import pyter

# class EvaluationMetrics:
#     def __init__(self, data_file_path):
#         self.df = pd.read_csv(data_file_path)
#         self.answer_prompt = [str(i) for i in self.df['answer']]
#         self.chatgpt_prompt = [str(j) for j in self.df['new_output']]
    
#     def bleu(self, ref, gen):
#         ref_bleu = []
#         gen_bleu = []
#         for l in gen:
#             gen_bleu.append(l.split())
#         for i,l in enumerate(ref):
#             ref_bleu.append([l.split()])
#         cc = SmoothingFunction()
#         score_bleu = corpus_bleu(ref_bleu, gen_bleu, weights=(0, 1, 0, 0), smoothing_function=cc.method4)
#         return score_bleu
    
#     def _split_into_words(self, sentences):
#         return list(itertools.chain(*[_.split(" ") for _ in sentences]))

#     def _get_word_ngrams(self, n, sentences):
#         assert len(sentences) > 0
#         assert n > 0

#         words = self._split_into_words(sentences)
#         return self._get_ngrams(n, words)

#     def _get_ngrams(self, n, text):
#         ngram_set = set()
#         text_length = len(text)
#         max_index_ngram_start = text_length - n
#         for i in range(max_index_ngram_start + 1):
#             ngram_set.add(tuple(text[i:i + n]))
#         return ngram_set
    
#     def rouge_n(self, reference_sentences, evaluated_sentences, n=2):
#         if len(evaluated_sentences) <= 0 or len(reference_sentences) <= 0:
#             raise ValueError("Collections must contain at least 1 sentence.")

#         evaluated_ngrams = self._get_word_ngrams(n, evaluated_sentences)
#         reference_ngrams = self._get_word_ngrams(n, reference_sentences)
#         reference_count = len(reference_ngrams)
#         evaluated_count = len(evaluated_ngrams)
#         overlapping_ngrams = evaluated_ngrams.intersection(reference_ngrams)
#         overlapping_count = len(overlapping_ngrams)
#         if evaluated_count == 0:
#             precision = 0.0
#         else:
#             precision = overlapping_count / evaluated_count

#         if reference_count == 0:
#             recall = 0.0
#         else:
#             recall = overlapping_count / reference_count

#         f1_score = 2.0 * ((precision * recall) / (precision + recall + 1e-8))
#         return recall
    
#     def ter(self, ref, gen):
#         if len(ref) == 1:
#             total_score =  pyter.ter(gen[0].split(), ref[0].split())
#         else:
#             total_score = 0
#             for i in range(len(gen)):
#                 total_score = total_score + pyter.ter(gen[i].split(), ref[i].split())
#             total_score = total_score/len(gen)
#         return total_score
    
#     def evaluate(self):
#         jaccard_score = sklearn.metrics.jaccard_score(self.answer_prompt, self.chatgpt_prompt, average='macro')
#         bleu_score = self.bleu(self.answer_prompt, self.chatgpt_prompt)
#         rouge_score = self.rouge_n(self.answer_prompt, self.chatgpt_prompt)
#         ter_score = self.ter(self.answer_prompt, self.chatgpt_prompt)
#         print("Jaccard score: ", jaccard_score)
#         print("BLEU score: ", bleu_score)
#         print("Rouge score: ",rouge_score)
#         print("TER score: ", ter_score)

df = pd.read_csv('./QA-Comparision/DialFact.csv')
df["answer_prompt"] = df["text"].astype(str) +  " The answer is "+ df["response"].astype(str)
df["chatgpt_prompt"] = df["text"].astype(str) + " The answer is "+ df["chatgpt_response"].astype(str)
answer_prompt = []
for i in df['answer_prompt']:
    answer_prompt.append(str(i))

chatgpt_prompt = []
for j in df['chatgpt_prompt']:
    chatgpt_prompt.append(str(i))


x_ap = []
from BARTScore.bart_score import BARTScorer
bart_scorer = BARTScorer(device='cpu', checkpoint='facebook/bart-large-cnn')
for (i,j) in zip(answer_prompt,chatgpt_prompt):
    x = bart_scorer.score([i], [j], batch_size=4)
    print(x)
    x_ap.append(x)


import statistics
row_average = [sum(sub_list) / len(sub_list) for sub_list in x_ap]
print(statistics.mean(row_average))


