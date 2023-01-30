import os
from src.filter import _filter, _listsorter
import src.defaultvalues


class SearchFlag:
    def __init__(self):
        self.file_needed = True
        self.dir_needed = True
        self.is_recur = True


def traverse_target_dir(flag: SearchFlag, abs_dir, file_list: list):
    if flag.is_recur:
        for (root, dirs, files) in os.walk(abs_dir):
            if flag.dir_needed:
                file_list.append(root)
            for file in files:
                path = os.path.join(root, file)
                if flag.file_needed and os.path.isfile(path):
                    file_list.append(path)
    else:
        for path in os.listdir(abs_dir):
            path = os.path.join(abs_dir, path)
            if (flag.file_needed and os.path.isfile(path)) \
                    or (flag.dir_needed and os.path.isdir(path)):
                file_list.append(path)
    list.remove(abs_dir)


def filt_list(file_list: list, include_list: list, exclude_list: list):
    for file in file_list[:]:
        is_reserve = True
        for exclude in exclude_list:
            if exclude in file:
                is_reserve = False
                break
        if not is_reserve:
            file_list.remove(file)
            continue

        if include_list:
            is_reserve = False
            for include in include_list:
                if file.endswith(include):
                    is_reserve = True
                    break
            if not is_reserve:
                file_list.remove(file)
                continue


def create_time_comparator(path):
    return os.stat(path).st_birthtime


def modify_time_comparator(path):
    return os.path.getmtime(path)


def name_comparator(path):
    return path.rsplit("/", 1)[1].lower()


def path_comparator(path):
    return path.lower()


def size_comparator(path):
    # 文件夹似乎不能表示, 但是也不会报错
    return os.stat(path).st_size


def sort_list(file_list: list, key_str: str, is_reverse = False):
    key_dict = {
        "CTIME": create_time_comparator,
        "MTIME": modify_time_comparator,
        "NAME": name_comparator,
        "PATH": path_comparator,
        "SIZE": size_comparator
    }
    file_list.sort(key=key_dict[key_str], reverse=is_reverse)






class Searcher:
    def __init__(self, src_dir_path="", is_recur=True, is_include_dir=False, \
                 include_list=src.defaultvalues.INCLUDE_LIST, exclude_list=src.defaultvalues.EXLUDE_LIST, \
                 comparator=src.defaultvalues.COMPARATOR, is_reverse=False
                 ):
        self._target_dir_path = src_dir_path
        self._is_recur = is_recur
        self._is_include_dir = is_include_dir
        self._include_list = include_list
        self._exclude_list = exclude_list
        self._comparator = comparator
        self._is_reverse = is_reverse

        self._list_sorter = listsorter.ListSorter()
        self._filter = filter.Filter()

        self._path_set = set()

    def traverse_target_dir(self):
        if self._is_recur:
            for (root, dirs, files) in os.walk(self._target_dir_path):
                for file in files:
                    self._path_set.add(os.path.join(root, file))
                    if self._is_include_dir:
                        self._path_set.add(root)
        else:
            for path in os.listdir(self._target_dir_path):
                absolute_path = os.path.join(self._target_dir_path, path)
                if not self._is_include_dir:
                    if os.path.isdir(absolute_path):
                        continue
                self._path_set.add(absolute_path)

    def filt_path_set(self):
        for file_path in self._path_set.copy():
            if not self._filter.filt(file_path, include_list=self._include_list, exclude_list=self._exclude_list):
                self._path_set.remove(file_path)
                continue
        return

    def get_path_list(self):
        self.traverse_target_dir()

        self.filt_path_set()

        return self._list_sorter.sort(file_path_set=self._path_set, comparator=self._comparator,
                                      is_reverse=self._is_reverse)
