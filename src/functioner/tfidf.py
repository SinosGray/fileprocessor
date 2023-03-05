# -*- coding: utf-8 -*-
import math
from textblob import TextBlob as tb
import nltk
from nltk.corpus import stopwords
import string
from src.functioner.function import remove_symbols_in_str
import src.functioner.function as func
import yaml


# https://stevenloria.com/tf-idf/
# Term Frequency, Inverse Document Frequency.
# 字詞的重要性隨著它在文件中出現的次數成正比增加，但同時會隨著它在語料庫中出現的頻率成反比下降。


def tf(word, wordlist: list):
    """
    :param word:
    :param wordlist: article
    :return: word frequency in blob
    """
    if wordlist.count(word) <= 2:
        return 0
    return wordlist.count(word) / len(wordlist)


def n_containing(word, dic):
    """
    :param word:
    :param dic:
    :return: number of word appeared in list
    """
    return sum(1 for path in dic if word in dic[path])


def idf(word, dic):
    """
    :param word:
    :param bloblist:
    :return: inverse document frequency
    """
    if n_containing(word, dic) == 1:
        return 0
    return math.log(len(dic) / (1 + n_containing(word, dic)))


def tfidf(word, wordlist, dic):
    return tf(word, wordlist) * idf(word, dic)


def cleanup_doc(str):
    stopset = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(remove_symbols_in_str(str))
    cleanup = [token.lower() for token in tokens if token.lower() not in stopset and len(token) > 2]
    return cleanup


def get_tfidf(path_list):
    """
    :param path_list:
    :return: a dictionary: dic[path] = word_score_dic
    """
    bloblist = []
    dic = {}
    for path in path_list:
        file = open(path, 'r')
        dic[path] = cleanup_doc(file.read())
        file.close()
    result = {}
    for path, wordlist in dic.items():
        # print(path)
        scores = {word: tfidf(word, wordlist, dic) for word in wordlist}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        result[path] = sorted_words
        # for word, score in sorted_words[:3]:
        #     print("Word:{}, tf-idf:{}".format(word, score))
    return result


def change_keyword_in_md(path_list):
    keyword_dic = get_tfidf(path_list)
    for path in path_list:
        print(path)
        file = open(path, 'r+')
        str = file.read()
        pattern = '---'
        pattern_list = list(pattern_search(str, pattern))
        if len(pattern_list) >= 2:
            blog_info_str = str[pattern_list[0] + len(pattern):pattern_list[1]]

            blog_data = yaml.load(blog_info_str.replace("\t", "    "), Loader=yaml.SafeLoader)
            tags = []
            for word, score in keyword_dic[path][:5]:
                tags.append(word)
            blog_data['tags'] = tags

            str = str.replace(blog_info_str,
                              "\n" + yaml.dump(blog_data, allow_unicode=True))
        file.close()

        file = open(path, 'w')
        file.write(str)
        print(str)
        file.close()


def pattern_search(string, pattern):
    index = 0
    while index < len(string) - len(pattern):
        index = string.find(pattern, index, len(string))
        if index == -1:
            break
        yield index
        index += len(pattern) - 1

# str = "title: \"\u8BBE\u8BA1\u6A21\u5F0F\u8BFB\u4E66\u7B14\u8BB0\""
# strr = r"title: \"\u8BBE\u8BA1\u6A21\u5F0F\u8BFB\u4E66\u7B14\u8BB0\""
# print(str.encode('utf-8'))
# print("{}".format(strr))
