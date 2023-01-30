# Requires Python 3.6 or higher due to f-strings
# ocrmypdf
# Import libraries
import PyPDF2

from PyPDF2 import PdfFileReader as pdf_read

# 每个书签的索引格式
# {'/Title': '书签名', '/Page': '指向的目标页数', '/Type': '类型'}

directory_str = ''
TARGET_PDF = "/Users/akunda/Downloads/C++20高级编程 第五版.pdf"


class PdfBookmarkGetter:
    @staticmethod
    def bookmark_listhandler(list):
        global directory_str
        for message in list:
            if isinstance(message, dict):
                directory_str += message['/Title'] + '\n'
                # print(message['/Title'])
            else:
                PdfBookmarkGetter.bookmark_listhandler(message)

    @staticmethod
    def get_bookmark(target_pdf=TARGET_PDF):
        with open(target_pdf, 'rb') as f:
            pdf = pdf_read(f)
            # 检索文档中存在的文本大纲,返回的对象是一个嵌套的列表
            text_outline_list = pdf.getOutlines()
            PdfBookmarkGetter.bookmark_listhandler(text_outline_list)

        with open('目录.txt', 'w', encoding='utf-8') as f:
            f.write(directory_str)





def md_reg_bookmark():
    with open("/Users/akunda/project/fileprocessor/src/functioner/目录.txt") as f:
        lines = f.readlines()
        output = []
        for line in lines:
            pre = "#" * (line.count(".") + 1)
            if pre != "":
                pre = pre + " "
            output.append(pre + line)
    for line in output:
        print(line)


PdfBookmarkGetter.get_bookmark();
md_reg_bookmark()
