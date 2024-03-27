# Goal1


# Making NLP model
# Use Case: Computer Model --> Classifyi Computer model that analayze how VR users feel when they talk with
# # AI or human.
# # Natural Language Processing (NLP) --> technique that give ability to
# #  understand human language
# # In other words, the goal of NLP is to enable computers to understand,
# # and interpret human language. ex) Chatbot(chatgpt)ng the topic of news.

#1. Data Collections.
# --> We need to collect bunch of news data. Then, we need to label them.

#2. Text preprocessing
#  --> the process of clearning and preparing text data before we use this data for
#      training a machine learning (AI) model.
#   1. Lowercasing --> Convert all text to lower case.
#      - Computer is case-sensitive --> 'Make' vs 'make'
#   2. Tokenization --> breaking down the text into words.
#      "i love to play soccer."  -> ["i", "love", "to", "play", "soccer"]
#   3. Remove punctuations: --> removing periods, comma, quotations....
#      punctuations does not affect to the meaning of the sentence in most of cases.
#   4. Removing stopwords:  stopwords are the words that do no have certain meanings.
#       ex) is, a , the , of, am, it ....
#        my name scott.
#   5. Lemmatization/Stemming --> changing the words into root form.
#      ex) past tense -->present tence. pluaral --> singular
#      Made vs Make
#      Let say we counts the frequency of the words.  Cat vs Cats

# NLTK --> one of the popular library for implementing NLP in Python
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
# with the given text, return its lowercase text
def lowercase(text):
    lowercase_text = text.lower()
    return lowercase_text
def tokenization(text):
    words_list = text.split() # .split()  splits the text by space
    return words_list
def remove_punctuation(word_list): # soccer,
    #  from the given text, replace ',' to ''.
    # removed_text = text.replace(',','')
    # removed_text = removed_text.replace('?', '')
    lst_punctuations = ",./!@#$%^&*()-+=~'0123456789"
    final_lst = []
    for text in word_list:
        result = ""
        for ch in text:
            if ch not in lst_punctuations:
                result += ch # "soccer"
        final_lst.append(result)
    return final_lst

def remove_stopwords(word_list): # ['i', 'love', 'to', 'play', 'soccer']
    lst_stopwords = stopwords.words('english')
    # print(lst_stopwords)
    final_lst = []
    for word in word_list:
        if word not in lst_stopwords:
            final_lst.append(word)
    return final_lst

def lst_to_string(word_lst): # ["i","like","you"]
    return ' '.join(word_lst) # "i like you"