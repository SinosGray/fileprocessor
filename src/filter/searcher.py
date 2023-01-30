import os
from src.filter import filter, listsorter
import src.defaultvalues


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
