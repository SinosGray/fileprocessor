# TODO
# 异常处理
# 指定输出位置, print or file
# 正则问题, 比如文件中有空格
import os.path

from src.filter.searcher import *
from src.functioner.function import *
from src.functioner.tfidf import change_keyword_in_md


def print_file_list2txt(file_list, target_file):
    with open(target_file, "w") as f:
        for file_path in file_list:
            f.write(file_path + "\n")


def get_file_list(src_dir,
                  search_flag
                  ) -> list:
    include_list = ["md"]
    exclude_list = ["/."]

    file_list = []
    traverse_target_dir(search_flag, src_dir, file_list)
    filt_list(file_list=file_list, include_list=include_list, exclude_list=exclude_list)
    sort_list(file_list, "NAME")
    return file_list


if __name__ == '__main__':
    search_flag = SearchFlag()
    search_flag.file_needed = True
    search_flag.dir_needed = False
    search_flag.is_recur = True

    # file_list = get_file_list("/Users/akunda/project/fileprocessor/targetdir", search_flag)
    # change_keyword_in_md(file_list)
    pdf_bookmark2md_title("/Users/akunda/Downloads/代码大全2中文版 2.pdf")
