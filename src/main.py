# TODO
# 异常处理
# 指定输出位置, print or file
# 正则问题, 比如文件中有空格
import os.path

from src.filter.searcher import *
from src.functioner import function


def print_file_list2txt(file_list, target_file):
    with open(target_file, "w") as f:
        for file_path in file_list:
            f.write(file_path + "\n")


if __name__ == '__main__':
    is_single_file = False
    if is_single_file:
        print("single file")
        function.pdf_bookmark2md_title \
            ("/Users/akunda/Downloads/C++20实践入门 第六版.pdf")

    else:
        flag = SearchFlag()
        flag.file_needed = True
        flag.dir_needed = True
        flag.is_recur = True
        dir = r"/Users/akunda/Downloads/qq_download"
        include_list = [""]
        exclude_list = ["/."]

        list = []
        traverse_target_dir(flag, dir, list)
        filt_list(file_list=list, include_list=include_list, exclude_list=exclude_list)
        sort_list(list, "SIZE")

        for file in list:
            print(function.get_size(file))

