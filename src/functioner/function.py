import shutil
import os
import imageio
from PyPDF2 import PdfFileReader as pdf_read
import PyPDF2
from PIL import Image
import re


def remove_symbols_in_str(str):
    return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", " ", str)


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
    bookmark_txt = "目录.txt"

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


def merge_pdf(pdf_list, target_file_path):
    merger = PyPDF2.PdfFileMerger()

    # Define the path to the folder with the PDF files
    path_to_files = r'pdf_files/'

    # Get the file names in the directory
    for pdf in pdf_list:
        merger.append(pdf)

    # Write out the merged PDF file
    merger.write(target_file_path)
    merger.close()


def images2pdf(image_list, pdf_path):
    images = [
        Image.open(image)
        for image in image_list
    ]

    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )


def imgs2img(img_path_list, output_path):
    # 2 imgs to 1 img horizontally
    img_list = [Image.open(fn) for fn in img_path_list]
    if len(img_list) == 1:
        img_list[0].save(output_path)
    width, height = img_list[0].size
    result = Image.new(img_list[0].mode, (width * len(img_list), height))
    for i, img in enumerate(img_list):
        result.paste(img, box=(i * width, 0))
    result.save(output_path)


def merge_horizontal_imgs(file_list: list, mid_path_dir):
    '''
    :param file_list: imgs
    :param mid_path_dir: output dir
    :return: merged imgs in mid_path_dir
    '''
    imgs2img([file_list[0]], mid_path_dir + "{:0>3d}.jpg".format(0))
    for i in range(1, len(file_list), 2):
        imgs2img(file_list[i:i + 2], mid_path_dir + "{:0>3d}.jpg".format(i))
