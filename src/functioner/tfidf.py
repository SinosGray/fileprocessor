# -*- coding: utf-8 -*-
import math
import nltk
from nltk.corpus import stopwords
from src.functioner.function import remove_symbols_in_str
import src.functioner.function as func
import yaml
from src.functioner.test import debug
from tqdm import tqdm

# https://stevenloria.com/tf-idf/
# Term Frequency, Inverse Document Frequency.
# 字詞的重要性隨著它在文件中出現的次數成正比增加，但同時會隨著它在語料庫中出現的頻率成反比下降。

remove_words = ["截屏"]
TF_THREHOLD = 3
IDF_THREHOLD = 1


def tf(word, wordlist: list):
    """
    :param word:
    :param wordlist: article
    :return: word frequency in blob
    """
    if wordlist.count(word) <= TF_THREHOLD:
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
    if n_containing(word, dic) <= IDF_THREHOLD:
        return 0
    return math.log(len(dic) / (1 + n_containing(word, dic)))


def tfidf(word, wordlist, dic):
    return tf(word, wordlist) * idf(word, dic)


def pattern_search(string, pattern):
    index = 0
    while index < len(string) - len(pattern):
        index = string.find(pattern, index, len(string))
        if index == -1:
            break
        yield index
        index += len(pattern) - 1


def cleanup_doc(str):
    stopset = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(remove_symbols_in_str(str))
    cleanup = [token.lower() for token in tokens if token.lower() not in stopset and len(token) > 2]
    for token in cleanup:
        for word in remove_words:
            if word in token or token.isdigit():
                cleanup.remove(token)


    return cleanup


def get_tfidf(path_list):
    """
    :param path_list:
    :return: a dictionary: dic[path] = word_score_dic
    """
    dic = {}
    for path in path_list:
        file = open(path, 'r')
        dic[path] = cleanup_doc(file.read())
        file.close()
    result = {}
    for path, wordlist in tqdm(dic.items()):
        # print(path)
        scores = {word: tfidf(word, wordlist, dic) for word in wordlist}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        result[path] = sorted_words
        # for word, score in sorted_words[:3]:
        #     print("Word:{}, tf-idf:{}".format(word, score))
    return result


def change_keyword_in_md(path_list):
    keyword_dic = get_tfidf(path_list)
    for path in tqdm(path_list):
        debug(path)
        file = open(path, 'r+')
        md_content = file.read()
        pattern = '---'
        pattern_list = list(pattern_search(md_content, pattern))
        if len(pattern_list) >= 2:
            blog_info_str = md_content[pattern_list[0] + len(pattern):pattern_list[1]]

            blog_info_dic = yaml.load(blog_info_str.replace("\t", "    "), Loader=yaml.SafeLoader)
            tags = []
            for word, score in keyword_dic[path][:5]:
                if score > 0:
                    tags.append(word)
            debug(tags)
            blog_info_dic['tags'] = tags

            md_content = md_content.replace(blog_info_str,
                                            "\n" + yaml.dump(blog_info_dic, allow_unicode=True))
        file.close()

        file = open(path, 'w')
        file.write(md_content)
        file.close()

# str = "title: \"\u8BBE\u8BA1\u6A21\u5F0F\u8BFB\u4E66\u7B14\u8BB0\""
# strr = r"title: \"\u8BBE\u8BA1\u6A21\u5F0F\u8BFB\u4E66\u7B14\u8BB0\""
# print(str.encode('utf-8'))
# print("{}".format(strr))
