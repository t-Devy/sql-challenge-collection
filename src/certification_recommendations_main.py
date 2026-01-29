
import pandas as pd

from src.extract.constants import DATA_RAW
from src.detect_common_certs import most_common_phrases

def main():
    df = pd.read_csv(DATA_RAW / 'certs_licenses.csv')
    # print(df.head)
    # most_common_words(df, 'certification_name')
    # ngrams_from_df(df, 'certification_name')

    most_common_phrases(df, 'certification_name')

    # phrase_vectorizer(df, 'certification_name')


    # nltk_collocations(df, 'certification_name')


if __name__ == "__main__":
    main()

