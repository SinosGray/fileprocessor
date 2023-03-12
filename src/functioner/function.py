import shutil
import os
import imageio
from PyPDF2 import PdfFileReader as pdf_read
import PyPDF2
from PIL import Image
import re


def get_removed_symbols_str(in_str) -> str:
    return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", " ", in_str)


def copy_file2dir(file, target_dir):
    return shutil.copy2(file, target_dir)


def get_size(file) -> str:
    return get_mb_from_byte(os.stat(file).st_size).__str__() + "   " + get_name(file)


def get_name(file, prefix="", suffix="") -> str:
    return prefix + os.path.basename(file) + suffix


def txt_replace(file, old_str, new_str):
    f = open(file, 'r')
    file_data = f.read()
    f.close()

    new_data = file_data.replace(old_str, new_str)

    f = open(file, 'w')
    f.write(new_data)
    f.close()


def get_mb_from_byte(size):
    return size >> 20


def imgs2gif(src_img_list: list, target_path, duration=2.5):
    imgs = []
    for img in src_img_list:
        imgs.append(imageio.v2.imread(img))
    imageio.mimsave(uri=target_path, ims=imgs, format='GIF', duration=duration)


def get_erase_space_str(str):
    return "".join(str.split())


class PdfBookmarkGetter:

    def __init__(self):
        self.bookmark_txt = "目录.txt"

    def _bookmark_list_handler(self, outline_list):
        result = []
        for message in outline_list:
            if isinstance(message, dict):
                result.append(message['/Title'])
            else:
                result.extend(self._bookmark_list_handler(message))
        return result

    def get_bookmark(self, target_pdf):
        with open(target_pdf, 'rb') as f:
            pdf = pdf_read(f)
            # 检索文档中存在的文本大纲,返回的对象是一个嵌套的列表
            text_outline_list = pdf.getOutlines()
            book_mark_list = self._bookmark_list_handler(text_outline_list)

        return book_mark_list

    def md_reg_bookmark(self, target_pdf):
        outline_list = self.get_bookmark(target_pdf)
        output_list = []
        for line in outline_list:
            pre = "#" * (line.count(".") + 1)
            if pre != "":
                pre = pre + " "
            output_list.append(pre + line)

        for line in output_list:
            print(line)


def pdf_bookmark2md_title(pdf_path):
    getter = PdfBookmarkGetter()
    getter.md_reg_bookmark(pdf_path)


def merge_pdf(pdf_list, target_file_path):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(target_file_path)
    merger.close()


def images2pdf(image_list, target_pdf_path):
    images = [
        Image.open(image)
        for image in image_list
    ]

    images[0].save(
        target_pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
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
