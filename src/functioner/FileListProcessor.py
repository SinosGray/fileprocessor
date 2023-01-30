import shutil
import os
from src.functioner.functioner import *
import src.functioner.pdfdirgetter

# args
FILE = "file"
TARGET_DIR = "target_dir"


def fun_copy(file, *args):
    return shutil.copy2(args[0], args[1])


def print_size(file, *args):
    print(from_byte2mb(os.stat(file).st_size).__str__() + "   " + file)


def print_name(file, *args):
    print("- /img/cover/" + os.path.basename(file))


def txt_replace(file, *args):
    # file to_be_replace replace
    # print("\n" + file)
    # for arg in args:
    #     print(arg)

    f = open(file, 'r')
    file_data = f.read()
    f.close()

    new_data = file_data.replace(args[0], args[1])

    f = open(file, 'w')
    f.write(new_data)
    f.close()


# register table
# regist    fun_name need_copy need_list
# FUN_COPY = [fun_copy]
# PRINT_SIZE = [print_size]
# PRINT_NAME = [print_name]
# IMG2GIF = [imgs2gif]
# TXT_REPLACE = [txt_replace]


# TODO
# change args
class FileListProcessor:

    def __init__(self, target_path, file_list, function):
        self._target_path = target_path
        self._origin_file_list = file_list
        # self._copy_file_list = os.listdir(target_path)
        self._function = function

    # def copy_file_to_target_dir(self, target_dir_path, file_path):
    #     return shutil.copy2(file_path, target_dir_path)

    # def copy_files_get_new_list(self, target_dir_path, file_list):
    #     for file in file_list:
    #         shutil.copy2(file, target_dir_path)
    #     self._copy_file_list = os.listdir(target_dir_path)

    def run(self, *args):
        for file in self._origin_file_list:
            self._function(file, *args)
        # if self._is_need_copy:
        #     for file in self._origin_file_list:
        #         self.copy_file_to_target_dir(self._target_dir, file)
