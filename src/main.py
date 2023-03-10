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


def get_file_list(srcdir,
                  file_needed=True,
                  dir_needed=False,
                  is_recur=True,
                  ):
    flag = SearchFlag()
    flag.file_needed = file_needed
    flag.dir_needed = dir_needed
    flag.is_recur = is_recur
    include_list = ["jpg"]
    exclude_list = ["/."]

    list = []
    traverse_target_dir(flag, srcdir, list)
    filt_list(file_list=list, include_list=include_list, exclude_list=exclude_list)
    sort_list(list, "NAME")
    return list


if __name__ == '__main__':
    get_file_list(srcdir=r"/Users/akunda/Downloads/netdisk/只狼/sekiro")
