from collections import OrderedDict
from itertools import chain
import re
import os

from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import download
from nltk.metrics import edit_distance
import nltk
import enchant
import spacy
import numpy as np
# NLTK GLOBAL VARIABLES --------------------------------
lemmatizer = WordNetLemmatizer()
replacement_patterns = [
        (r'won\'t', 'will not'),
        (r'can\'t', 'cannot'),
        (r'i\'m', 'i am'),
        (r'ain\'t', 'is not'),
        (r'(\w+)\'ll', '\g<1> will'),
        (r'(\w+)n\'t', '\g<1> not'),
        (r'(\w+)\'ve', '\g<1> have'),
        (r'(\w+)\'s', '\g<1> is'),
        (r'(\w+)\'re', '\g<1> are'),
        (r'(\w+)\'d', '\g<1> would')
]

patterns = []
for regular_expression, replacement in replacement_patterns:
    patterns.append((re.compile(regular_expression), replacement))

repeat_regular_expresssion = re.compile(r'(\w*)(\w)\2(\w*)')
repeat_replacement = r'\1\2\3'


# enchant GLOBAL VARIABLES -------------------------------
spell_dictionary = enchant.Dict('en')
# --------------------------------------------------------


# spacy GLOBAL VARIABLES ---------------------------------
spacy_dictionary = spacy.load('en')
# --------------------------------------------------------


def download_spacy_data():
    os.system('sudo python3 -m spacy.en.download all')
    # TODO run python3 -m spacy.en.download all


def download_nltk_data(package_name=None):
    if package_name is None:
        data = ['punkt', 'wordnet', 'stopwords', 'averaged_perceptron_tagger']
        for package in data:
            download(package)
    else:
        download(package)


def tokenize(sentence, lowercase=True):
    tokens = word_tokenize(sentence)
    if lowercase:
        tokens = [token.lower() for token in tokens]
    return tokens


def get_synonyms(word):
    synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())
    return synonyms


def get_definition(word):
    synset = wordnet.synsets(word)[0]
    return synset


def filter_stop_words(tokenized_sentence):
    english_stops = set(stopwords.words('english'))
    filtered_tokens = []
    for token in tokenized_sentence:
        if token not in english_stops:
            filtered_tokens.append(token)
    return filtered_tokens


def filter_repeated_words(tokenized_sentence):
    return list(set(tokenized_sentence))


def calculate_wordnet_similarity(word_1, word_2):
    word_synset_1 = wordnet.synset(word_1)
    word_synset_2 = wordnet.synset(word_1)
    return word_synset_1.wup_similiraty(word_synset_2)


def find_synonyms(reference_sentence, hypothesis_sentence, return_tokens=True):
    """
    Inputs: two lists of tokenized string sentences
    Returns: A dictionary with keys being the word in the reference_sentence
    and the values a list of the arguments where there is a synonym in the
    hypothesis_sentence.
    """
    synonyms_connections = OrderedDict()
    for reference_token in reference_sentence:
        reference_synonyms = list(set(get_synonyms(reference_token)))
        reference_synonyms = reference_synonyms + [reference_token]
        hypothesis_args = []
        for hypothesis_arg, hypothesis_token in enumerate(hypothesis_sentence):
            for reference_synonym in reference_synonyms:
                words_are_synonyms = hypothesis_token == reference_synonym
                words_are_the_same = hypothesis_token == reference_token
                if words_are_the_same:
                    if return_tokens:
                        hypothesis_args.append(hypothesis_token)
                    else:
                        hypothesis_args.append(hypothesis_arg)
                    break
                elif words_are_synonyms:
                    if return_tokens:
                        hypothesis_args.append(hypothesis_token)
                    else:
                        hypothesis_args.append(hypothesis_arg)

        synonyms_connections[reference_token] = hypothesis_args
    return synonyms_connections


def find_similarities(reference_sentence, hypothesis_sentence,
                      return_tokens=True):
    """
    Inputs: two lists of tokenized string sentences
    Returns: A dictionary with keys being the word in the reference_sentence
    and the values a list of the arguments where there is a synonym in the
    hypothesis_sentence.
    """
    synonyms_connections = OrderedDict()
    for reference_token in reference_sentence:
        reference_synonyms = list(set(get_synonyms(reference_token)))
        reference_synonyms = reference_synonyms + [reference_token]
        hypothesis_args = []
        for hypothesis_arg, hypothesis_token in enumerate(hypothesis_sentence):
            for reference_synonym in reference_synonyms:
                words_are_synonyms = hypothesis_token == reference_synonym
                words_are_the_same = hypothesis_token == reference_token
                if words_are_the_same:
                    if return_tokens:
                        hypothesis_args.append(hypothesis_token)
                    else:
                        hypothesis_args.append(hypothesis_arg)
                    break
                elif words_are_synonyms:
                    if return_tokens:
                        hypothesis_args.append(hypothesis_token)
                    else:
                        hypothesis_args.append(hypothesis_arg)

        synonyms_connections[reference_token] = hypothesis_args
    return synonyms_connections


def edit(hypothesis_sentence, token_connections,
         start_string='**', end_string='**'):
    edited_hypothesis = []
    hypothesis_highlights = list(chain(*list(token_connections.values())))
    for hypothesis_token in hypothesis_sentence:
        if hypothesis_token in hypothesis_highlights:
            hypothesis_token = start_string + hypothesis_token + end_string
        edited_hypothesis.append(hypothesis_token)
    edited_hypothesis = ' '.join(edited_hypothesis)
    return edited_hypothesis


def join(tokens):
    return ' '.join(tokens)


def lemmatize(word, pos='n'):
    return lemmatizer.lemmatize(word, pos=pos)


def expand_contractions(sentence):
    for (pattern, replacement) in patterns:
        sentence = re.sub(pattern, replacement, sentence)
    return sentence


def remove_repeated_characters(word):
    if wordnet.synsets(word):
        return word
    replaced_word = repeat_regular_expresssion.sub(repeat_replacement, word)
    if replaced_word != word:
        return remove_repeated_characters(replaced_word)
    else:
        return replaced_word


def in_dictionary(word):
    return spell_dictionary.check(word)


def suggest_words(word):
    return spell_dictionary.suggest(word)


def correct_misspelling(word, max_distance=2):
    if in_dictionary(word):
        return word
    suggested_words = suggest_words(word)
    if suggested_words is not None:
        num_modified_characters = []
        for suggest_word in suggested_words:
            num_modified_characters.append(edit_distance(word, suggest_word))
        max_num_modified_characters = min(num_modified_characters)
        best_arg = num_modified_characters.index(max_num_modified_characters)
        if max_distance > max_num_modified_characters:
            best_suggestion = suggested_words[best_arg]
            return best_suggestion
        else:
            return word
    else:
        return word


def tag_pos(tokens):
    return nltk.pos_tag(tokens)


def get_vector(word, mode='glove'):
    if mode == 'glove':
        return spacy_dictionary(word).vector


def get_vectors(tokens, mode='glove'):
    if mode == 'glove':
        return [get_vector(token) for token in tokens]


def calculate_norm(vector):
    return np.linalg.norm(vector)


def calculate_vector_similarity(vector_1, vector_2):
    norm_1 = calculate_norm(vector_1)
    norm_2 = calculate_norm(vector_2)
    if norm_1 == 0 or norm_2 == 0:
        return 0.0
    return np.dot(vector_1, vector_2) / (norm_1 * norm_2)


def calculate_synonyms_similarities(synonyms):
    similarities = []
    for word_1, word_2 in synonyms.items():
        if len(word_2) == 0:
            continue
        elif len(word_2) >= 1:
            selected_word_2 = word_2[0]
        vector_1 = get_vector(word_1)
        vector_2 = get_vector(selected_word_2)
        if word_1 == selected_word_2:
            similarity = 1.
            print(word_1)
        elif calculate_norm(vector_1) == 0 or calculate_norm(vector_2) == 0:
            continue
        else:
            similarity = calculate_vector_similarity(vector_1, vector_2)
        similarities.append(similarity)
    return similarities


def remove_repeated_elements(items):
    return list(OrderedDict.fromkeys(items))


def get_related_words(word, method='vector', max_num=3):
    if method == 'vector':
        spacy_word = spacy_dictionary(word)
        queries = [token for token in spacy_word.vocab if token.prob >= -15]
        queries = sorted(queries, key=lambda w: spacy_word.similarity(w),
                         reverse=True)
        queries = [query.lower_ for query in queries if query.lower_ != word]
        queries = remove_repeated_elements(queries)
        if len(queries) > max_num:
            queries = queries[:max_num]
        return queries


def find_ngram(word, n):
    return list(ngrams(word, n))


def calculate_jaccard_coefficient(a, b):
    union = list(set(a + b))
    intersection = list(set(a) - (set(a) - set(b)))
    jaccard_coeff = float(len(intersection)) / len(union)
    return jaccard_coeff


def correct_misspelling_ngram(word, max_distance=3):
    """
    Steps:
    1. Find Misspelled words
    2. Check Suggested Words
    3. Filter suggested words which are different within some distance using
    edit distance
    4. Compute Ngram of misspelled word and each suggested word
    5. Compute Jaccard coefficient of misspelled word and each suggested word
    6. Replace suggested word with maximum jaccard coefficient

    """
    if in_dictionary(word):
        return word
    suggested_words = suggest_words(word)
    max_jaccard = []
    list_of_sug_words = []
    if suggested_words is not None:

        word_ngrams = find_ngram(word, 2)

        for suggest_word in suggested_words:

            if (edit_distance(word, suggest_word)) < max_distance:
                suggest_ngrams = find_ngram(suggest_word, 2)
                jac = calculate_jaccard_coefficient(word_ngrams,
                                                    suggest_ngrams)
                max_jaccard.append(jac)
                list_of_sug_words.append(suggest_word)
        highest_jaccard = max(max_jaccard)
        best_arg = max_jaccard.index(highest_jaccard)
        word = list_of_sug_words[best_arg]
        return word

    else:
        return word


if __name__ == "__main__":

    """
    sentence_1 = 'there is a dog and the dog sat on the mat'
    sentence_2 = 'there is a mat and on the mat sat the '

    def preprocess_sentence(sentence):
        tokens = tokenize(sentence)
        tokens = filter_stop_words(tokens)
        tokens = filter_repeated_words(tokens)
        return tokens


    tokens_1 = preprocess_sentence(sentence_1)
    tokens_2 = preprocess_sentence(sentence_2)

    synonyms = find_synonyms(tokens_1, tokens_2)
    print('Synonyms found: \n', synonyms)

    cosine_similarities = calculate_synonyms_similarities(synonyms)
    print('Cosine similarities: \n', cosine_similarities)

    """
    print(get_related_words('dog'))
    print(get_related_words('cat'))
    print(get_related_words('person'))
