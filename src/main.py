# TODO
# 异常处理
# 指定输出位置, print or file
# 正则问题, 比如文件中有空格
import os.path

from src.filter import searcher
import defaultvalues
from src.functioner import FileListProcessor
import src.functioner.functioner


def print_file_list2txt(file_list, target_file):
    with open(target_file, "w") as f:
        for file_path in file_list:
            f.write(file_path + "\n")


if __name__ == '__main__':



    src_dir_path = "/Users/akunda/Nutstore_Files/my_nut/blog/source/_posts/"
    is_recur = True
    is_include_dir = False
    include_list = ["md"]
    exclude_list = ["/.", "~$", " "] # defaultvalues.EXLUDE_LIST
    comparator = defaultvalues.SIZE
    is_reverse = False
    target_dir = defaultvalues.TARGET_DIR

    s = searcher.Searcher(src_dir_path=src_dir_path,
                          is_recur=is_recur,
                          is_include_dir=is_include_dir,
                          include_list=include_list,
                          exclude_list=exclude_list,
                          comparator=comparator,
                          is_reverse=is_reverse
                          )
    l = s.get_path_list()


    # print_file_list2txt(l, os.path.join(target_dir, "filelist.txt"))

    f = FileListProcessor.FileListProcessor(target_path=target_dir, \
                                            file_list=l, function=FileListProcessor.txt_replace)
    f.run("password: wzqdiary", "password: ")

    # src_dir_path = "/Users/akunda/Downloads/gifs/俺と妹の一日/"
    # is_recur = False
    # is_include_dir = True
    # include_list = []
    # exclude_list = defaultvalues.EXLUDE_LIST
    # comparator = defaultvalues.NAME
    # is_reverse = False
    # target_dir = defaultvalues.TARGET_DIR
    #
    # s = searcher.Searcher(src_dir_path=src_dir_path,
    #                       is_recur=is_recur,
    #                       is_include_dir=is_include_dir,
    #                       include_list=include_list,
    #                       exclude_list=exclude_list,
    #                       comparator=comparator,
    #                       is_reverse=is_reverse
    #                       )
    # l = s.get_path_list()
    # for i, dir in enumerate(l):
    #     dir_s = searcher.Searcher(src_dir_path=dir,
    #                               is_recur=False,
    #                               is_include_dir=False,
    #                               include_list=["png", "jpg"],
    #                               exclude_list=defaultvalues.EXLUDE_LIST,
    #                               comparator=defaultvalues.NAME,
    #                               is_reverse=False
    #                               )
    #     dir_l = dir_s.get_path_list()
    #     src.functioner.functioner.imgs2gif(dir_l, target_dir + i.__str__() + ".gif")
