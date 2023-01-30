# some functions assisit
import os

import imageio


def from_byte2mb(size):
    return size >> 20


def imgs2gif(src_img_list, target_path):
    imgs = []
    for img in src_img_list:
        imgs.append(imageio.v2.imread(img))
    imageio.mimsave(uri=target_path, ims=imgs, format='GIF', duration=2.5)

def erase_space(str):
    return "".join(str.split())

str = r"定义一个用于创建对象的接又，让子类快定实例化哪一个类。Factory Method使一个类的 实例化延迟到其子类。"
print(erase_space(str))

# scr_dir = r"/Users/akunda/Nutstore_Files/my_nut/blog/node_modules/hexo-theme-butterfly/source/img/cover/"
# l=[]
# for path in os.listdir(scr_dir):
#     l.append(r"- /img/cover/" + path)
# #l.remove(scr_dir+'.DS_Store')
# l.sort()
# for line in l:
#     print(line)
