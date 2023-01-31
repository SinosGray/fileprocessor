import shutil
import os
import imageio
from PyPDF2 import PdfFileReader as pdf_read


def fun_copy(file, target_dir):
    return shutil.copy2(file, target_dir)


def get_size(file) -> str:
    return from_byte2mb(os.stat(file).st_size).__str__() + "   " + get_name(file)


def get_name(file, prefix="", suffix="") -> str:
    return prefix + os.path.basename(file) + suffix


def txt_replace(file, old, new):
    f = open(file, 'r')
    file_data = f.read()
    f.close()

    new_data = file_data.replace(old, new)

    f = open(file, 'w')
    f.write(new_data)
    f.close()


def from_byte2mb(size):
    return size >> 20


def imgs2gif(src_img_list: list, target_path):
    imgs = []
    for img in src_img_list:
        imgs.append(imageio.v2.imread(img))
    imageio.mimsave(uri=target_path, ims=imgs, format='GIF', duration=2.5)


def erase_space(str):
    return "".join(str.split())


class PdfBookmarkGetter:
    bookmark_txt = "/Users/akunda/project/fileprocessor/src/functioner/目录.txt"

    def __init__(self):
        self.directory_str = ""

    def _bookmark_list_handler(self, list):
        for message in list:
            if isinstance(message, dict):
                self.directory_str += message['/Title'] + '\n'
                # print(message['/Title'])
            else:
                self._bookmark_list_handler(message)

    def get_bookmark(self, target_pdf):
        with open(target_pdf, 'rb') as f:
            pdf = pdf_read(f)
            # 检索文档中存在的文本大纲,返回的对象是一个嵌套的列表
            text_outline_list = pdf.getOutlines()
            self._bookmark_list_handler(text_outline_list)

        with open(self.bookmark_txt, 'w', encoding='utf-8') as f:
            f.write(self.directory_str)


def md_reg_bookmark():
    with open(PdfBookmarkGetter.bookmark_txt) as f:
        lines = f.readlines()
        output = []
        for line in lines:
            pre = "#" * (line.count(".") + 1)
            if pre != "":
                pre = pre + " "
            output.append(pre + line)
    for line in output:
        print(line)


def pdf_bookmark2md_title(pdf_path):
    getter = PdfBookmarkGetter()
    getter.get_bookmark(pdf_path)
    md_reg_bookmark()
# register table
# regist    fun_name need_copy need_list
# FUN_COPY = [fun_copy]
# PRINT_SIZE = [print_size]
# PRINT_NAME = [print_name]
# IMG2GIF = [imgs2gif]
# TXT_REPLACE = [txt_replace]


# TODO
# change args
# class FileListProcessor:
#
#     def __init__(self, target_path, file_list, function):
#         self._target_path = target_path
#         self._origin_file_list = file_list
#         # self._copy_file_list = os.listdir(target_path)
#         self._function = function
#
#     # def copy_file_to_target_dir(self, target_dir_path, file_path):
#     #     return shutil.copy2(file_path, target_dir_path)
#
#     # def copy_files_get_new_list(self, target_dir_path, file_list):
#     #     for file in file_list:
#     #         shutil.copy2(file, target_dir_path)
#     #     self._copy_file_list = os.listdir(target_dir_path)
#
#     def run(self, *args):
#         for file in self._origin_file_list:
#             self._function(file, *args)
#         # if self._is_need_copy:
#         #     for file in self._origin_file_list:
#         #         self.copy_file_to_target_dir(self._target_dir, file)
