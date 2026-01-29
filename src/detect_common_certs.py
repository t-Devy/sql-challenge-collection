

from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import bigrams, trigrams
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures

import pandas as pd
import re


def most_common_words(df: pd.DataFrame, col: str):
    all_words = []
    for text in df[col].dropna():
        words = re.findall(r'\b\w+\b', str(text))
        all_words.extend(words)

    all_words_lower = [w.lower() for w in all_words]
    word_counts = Counter(all_words_lower)
    print(word_counts.most_common(50))

def _get_all_ngrams(text, min_n=3, max_n=10):
    ngrams = []
    for n in range(min_n, max_n+1):
        ngrams.extend([text[i:i+n] for i in range(len(text)-n+1)])
    return ngrams

def ngrams_from_df(df: pd.DataFrame, col: str):
    all_ngrams = []
    for text in df[col].dropna():
        all_ngrams.extend(_get_all_ngrams(str(text).lower(), min_n=3, max_n=10))

    ngram_counts = Counter(all_ngrams)
    print(ngram_counts.most_common(30))

def _varying_ngrams(text, n):
    words = re.findall(r'\b\w+\b', str(text).lower())
    return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]

def most_common_phrases(df: pd.DataFrame, col: str):
    all_phrases = []
    for text in df[col].dropna():
        all_phrases.extend(_varying_ngrams(text, 1))
        all_phrases.extend(_varying_ngrams(text, 2))
        all_phrases.extend(_varying_ngrams(text, 3))
        all_phrases.extend(_varying_ngrams(text, 4))

    phrase_counts = Counter(all_phrases)
    print(phrase_counts.most_common(100))

def phrase_vectorizer(df: pd.DataFrame, col: str):
    # 1 - 4 word phrases
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 4),
        max_features=200,
        min_df=5,
        lowercase=True,
        token_pattern=r'\b\w+\b'
    )

    tfidf_matrix = vectorizer.fit_transform(df[col].fillna(''))
    feature_names = vectorizer.get_feature_names_out()

    # get feature scores
    feature_scores = tfidf_matrix.sum(axis=0).A1
    top_features = sorted(zip(feature_names, feature_scores), key=lambda x: x[1], reverse=True)

    for phrase, score in top_features[:100]:
        print(f'{phrase}: {score:.2f}')

# def nltk_collocations(df: pd.DataFrame, col: str):
#     all_words = []
#     for text in df[col].dropna():
#         words = re.findall(r'\b\w+\b', str(text).lower())
#         all_words.extend(words)
#
#     # find bigrams
#     bigram_finder = BigramCollocationFinder.from_words(all_words)
#     bigram_finder.apply_freq_filter(3)      #must appear 5 times
#     bigrams = bigram_finder.nbest(BigramAssocMeasures.pmi, 50)      # top 50 bigrams
#
#     # find trigrams
#     trigram_finder = TrigramCollocationFinder.from_words(all_words)
#     trigram_finder.apply_freq_filter(3)
#     trigrams = trigram_finder.nbest(TrigramAssocMeasures.pmi, 50)       # top 50 trigrams
#
#     print("Top bigrams:", [' '.join(bg) for bg in bigrams])
#     print("Top trigrams:", [' '.join(tg) for tg in trigrams])



