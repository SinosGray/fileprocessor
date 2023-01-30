import os
import src.defaultvalues


class ListSorter:
    def __init__(self):
        pass

    @staticmethod
    def create_time_comparator(path):
        return os.stat(path).st_birthtime

    @staticmethod
    def modify_time_comparator(path):
        return os.path.getmtime(path)

    @staticmethod
    def name_comparator(path):
        return path.rsplit("/", 1)[1].lower()

    @staticmethod
    def path_comparator(path):
        return path.lower()

    @staticmethod
    def size_comparator(path):
        # 文件夹似乎不能表示, 但是也不会报错
        return os.stat(path).st_size

    def sort(self, file_path_set=set, comparator=src.defaultvalues.COMPARATOR, is_reverse=False):
        key = self.path_comparator
        if comparator == src.defaultvalues.CREATE_DATE:
            key = self.create_time_comparator
        elif comparator == src.defaultvalues.MODIFY_DATE:
            key = self.modify_time_comparator
        elif comparator == src.defaultvalues.SIZE:
            key = self.size_comparator
        elif comparator == src.defaultvalues.NAME:
            key = self.name_comparator

        return sorted(file_path_set, key=key, reverse=is_reverse)
