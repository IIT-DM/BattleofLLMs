from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu
import numpy as np
import pandas as pd
import sklearn, math, itertools, pyter, statistics, nltk
from collections import Counter
from nltk.translate import meteor
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

class EvaluationMetrics:
    def __init__(self, data_file_path):
        self.df = pd.read_csv(data_file_path)
        self.answer_prompt = [str(i) for i in self.df['answer']]
        self.chatgpt_prompt = [str(j) for j in self.df['new_output']]
    
    def bleu(self, ref, gen):
        ref_bleu = []
        gen_bleu = []
        for l in gen:
            gen_bleu.append(l.split())
        for i,l in enumerate(ref):
            ref_bleu.append([l.split()])
        cc = SmoothingFunction()
        score_bleu = corpus_bleu(ref_bleu, gen_bleu, weights=(0, 1, 0, 0), smoothing_function=cc.method4)
        return score_bleu
    
    def _split_into_words(self, sentences):
        return list(itertools.chain(*[_.split(" ") for _ in sentences]))

    def _get_word_ngrams(self, n, sentences):
        assert len(sentences) > 0
        assert n > 0

        words = self._split_into_words(sentences)
        return self._get_ngrams(n, words)

    def _get_ngrams(self, n, text):
        ngram_set = set()
        text_length = len(text)
        max_index_ngram_start = text_length - n
        for i in range(max_index_ngram_start + 1):
            ngram_set.add(tuple(text[i:i + n]))
        return ngram_set
    
    def rouge_n(self, reference_sentences, evaluated_sentences, n=2):
        if len(evaluated_sentences) <= 0 or len(reference_sentences) <= 0:
            raise ValueError("Collections must contain at least 1 sentence.")

        evaluated_ngrams = self._get_word_ngrams(n, evaluated_sentences)
        reference_ngrams = self._get_word_ngrams(n, reference_sentences)
        reference_count = len(reference_ngrams)
        evaluated_count = len(evaluated_ngrams)
        overlapping_ngrams = evaluated_ngrams.intersection(reference_ngrams)
        overlapping_count = len(overlapping_ngrams)
        if evaluated_count == 0:
            precision = 0.0
        else:
            precision = overlapping_count / evaluated_count

        if reference_count == 0:
            recall = 0.0
        else:
            recall = overlapping_count / reference_count

        f1_score = 2.0 * ((precision * recall) / (precision + recall + 1e-8))
        return recall
    
    def ter(self, ref, gen):
        if len(ref) == 1:
            total_score =  pyter.ter(gen[0].split(), ref[0].split())
        else:
            total_score = 0
            for i in range(len(gen)):
                total_score = total_score + pyter.ter(gen[i].split(), ref[i].split())
            total_score = total_score/len(gen)
        return total_score
    
    def bart(self):
        x_ap = []
        from BARTScore.bart_score import BARTScorer
        bart_scorer = BARTScorer(device='cpu', checkpoint='facebook/bart-large-cnn')
        for (i,j) in zip(self.answer_prompt, self.chatgpt_prompt):
            x = bart_scorer.score([i], [j], batch_size=4)
            print(x)
            x_ap.append(x)
        row_average = [sum(sub_list) / len(sub_list) for sub_list in x_ap]
        return (statistics.mean(row_average))

    def calculate_meteor(self, candidate, reference):
        reference = word_tokenize(reference)
        candidate = word_tokenize(candidate)
        meteor_score = round(meteor([candidate],reference), 4)
        return meteor_score
    
    def nist_length_penalty(self, ref_len, hyp_len):
        ratio = hyp_len / ref_len
        if 0 < ratio < 1:
            ratio_x, score_x = 1.5, 0.5
            beta = math.log(score_x) / math.log(ratio_x) ** 2
            return math.exp(beta * math.log(ratio) ** 2)
        else:
            return max(min(ratio, 1.0), 0.0)

    def corpus_nist(self, list_of_references, hypotheses, n=5):
        assert len(list_of_references) == len(
            hypotheses
        ), "The number of hypotheses and their reference(s) should be the same"
        ngram_freq = Counter()
        total_reference_words = 0
        for (
            references
        ) in list_of_references: 
            for reference in references:
                for i in range(1, n + 1):
                    ngram_freq.update(ngrams(reference, i))
                total_reference_words += len(reference)
        information_weights = {}
        for _ngram in ngram_freq:  
            _mgram = _ngram[:-1]  
            if _mgram and _mgram in ngram_freq:
                numerator = ngram_freq[_mgram]
            else:
                numerator = total_reference_words
            information_weights[_ngram] = math.log(numerator / ngram_freq[_ngram], 2)
        nist_precision_numerator_per_ngram = Counter()
        nist_precision_denominator_per_ngram = Counter()
        l_ref, l_sys = 0, 0
        for i in range(1, n + 1):
            for references, hypothesis in zip(list_of_references, hypotheses):
                hyp_len = len(hypothesis)
                nist_score_per_ref = []
                for reference in references:
                    _ref_len = len(reference)
                    hyp_ngrams = (
                        Counter(ngrams(hypothesis, i))
                        if len(hypothesis) >= i
                        else Counter()
                    )
                    ref_ngrams = (
                        Counter(ngrams(reference, i)) if len(reference) >= i else Counter()
                    )
                    ngram_overlaps = hyp_ngrams & ref_ngrams
                    _numerator = sum(
                        information_weights[_ngram] * count
                        for _ngram, count in ngram_overlaps.items()
                    )
                    _denominator = sum(hyp_ngrams.values())
                    _precision = 0 if _denominator == 0 else _numerator / _denominator
                    nist_score_per_ref.append(
                        (_precision, _numerator, _denominator, _ref_len)
                    )
                precision, numerator, denominator, ref_len = max(nist_score_per_ref)
                nist_precision_numerator_per_ngram[i] += numerator
                nist_precision_denominator_per_ngram[i] += denominator
                l_ref += ref_len
                l_sys += hyp_len
        nist_precision = 0
        for i in nist_precision_numerator_per_ngram:
            precision = (
                nist_precision_numerator_per_ngram[i]
                / nist_precision_denominator_per_ngram[i]
            )
            nist_precision += precision
        return nist_precision * self.nist_length_penalty(l_ref, l_sys)

    def sentence_nist(self, references, hypothesis, n=1):
        return self.corpus_nist([references], [hypothesis], n)
    
    def evaluate(self):
        jaccard_score = sklearn.metrics.jaccard_score(self.answer_prompt, self.chatgpt_prompt, average='macro')
        bleu_score = self.bleu(self.answer_prompt, self.chatgpt_prompt)
        rouge_score = self.rouge_n(self.answer_prompt, self.chatgpt_prompt)
        ter_score = self.ter(self.answer_prompt, self.chatgpt_prompt)
        print("Jaccard score: ", jaccard_score)
        print("BLEU score: ", bleu_score)
        print("Rouge score: ",rouge_score)
        print("TER score: ", ter_score)


df = pd.read_csv('./QA-Comparision/CoQA.csv')

# CoQA
df["answer_prompt"] = df["text"].astype(str) + " " + df["question"].astype(str) + " The answer is "+ df["answer"].astype(str)
df["chatgpt_prompt"] = df["text"].astype(str) + " " + df["question"].astype(str) + " The answer is "+ df["chatgpt_response"].astype(str)

# DialFact
# df["answer_prompt"] = df["text"].astype(str) +  " The answer is "+ df["response"].astype(str)
# df["chatgpt_prompt"] = df["text"].astype(str) + " The answer is "+ df["chatgpt_response"].astype(str)

answer_prompt = []
chatgpt_prompt = []
avg_meteor=[]
for i in df['answer_prompt']:
    answer_prompt.append(str(i))
for j in df['chatgpt_prompt']:
    chatgpt_prompt.append(str(i))

for (i,j) in zip(answer_prompt, chatgpt_prompt):
    score = sentence_nist(i,j)
    print(score)
    avg_meteor.append(score)

print(statistics.mean(avg_meteor))



   





