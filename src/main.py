# TODO
# 异常处理
# 指定输出位置, print or file
# 正则问题, 比如文件中有空格
import os.path

from src.filter.searcher import *
from src.functioner import function
from src.functioner import tfidf


def print_file_list2txt(file_list, target_file):
    with open(target_file, "w") as f:
        for file_path in file_list:
            f.write(file_path + "\n")


if __name__ == '__main__':
    is_single_file = False
    if is_single_file:
        print(function.remove_symbols_in_str(r"jwbdsafcuisabdiuf23e41230@#${adsfas!@{1(asda)f"))
        # function.pdf_bookmark2md_title \
        #     ("/Users/akunda/Downloads/游戏编程模式.pdf")

    else:
        flag = SearchFlag()
        flag.file_needed = True
        flag.dir_needed = False
        flag.is_recur = True
        dir = r"/Users/akunda/project/fileprocessor/targetdir"
        include_list = ["md"]
        exclude_list = ["/."]

        list = []
        traverse_target_dir(flag, dir, list)
        filt_list(file_list=list, include_list=include_list, exclude_list=exclude_list)
        sort_list(list, "NAME")
        tfidf.change_keyword_in_md(list)



