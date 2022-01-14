import nltk
from pyvi import ViTokenizer, ViPosTagger
import numpy as np
import os 
from string import punctuation
from tqdm import tqdm
class load_data:
    def read_data_train(path):
        # xử lý văn bản
        f = open(path, 'r', encoding='utf-8')
        data = f.read()
        find_content = data.find("Content:")
        doc = data [find_content + 8: ] 
        sentences = nltk.sent_tokenize(doc)
        X = []
        for sentence in sentences:
            sent=[]
            sentence_tokenized = ViTokenizer.tokenize(sentence)
            for word in sentence_tokenized.split(" "):
                if (word not in list(punctuation)):
                    sent.append(word)
            X.append(" ".join(sent))
        return X
    def read_data_test(path):
        # xử lý văn bản
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
        find_summary = data.find("Summary:")
        find_content = data.find("Content:")
        doc = data[find_summary + 8: find_content]
        sentences = nltk.sent_tokenize(doc)
        X = []
        for sentence in sentences:
            sent=[]
            sentence_tokenized = ViTokenizer.tokenize(sentence)
            for word in sentence_tokenized.split(" "):
                if (word not in list(punctuation)):
                    sent.append(word)
            X.append(" ".join(sent))
        return X

    def tao_danh_sach(document):
        # list các từ có trong văn bản
        list_word = []
        # mang lưu số từ của 1 câu
        word_in_sentence = []
        # danh sách các từ trong câu
        list_sentence = []
        for cau in document:
            #cau=cau.lower()
            cau = cau.split(" ")
            word_in_sentence.append(len(cau))
            list_sentence.append(cau)
            for word in cau:
                list_word.append(word)
        return list_word, word_in_sentence, list_sentence


   