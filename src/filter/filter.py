import  src.defaultvalues
class Filter:
    def __init__(self):
        # self._filt_function_list = [self.include_filt, self.exclude_filt]
        # self.include_list = defaultvalues.INCLUDE_LIST
        # self.exclude_list = defaultvalues.EXLUDE_LIST
        pass

    # 建议 filter 如果符合要求就返回 true

    @staticmethod
    def include_filt(path="", include_list=src.defaultvalues.INCLUDE_LIST):
        if not include_list:
            return True
        else:
            for in_str in include_list:
                if path.endswith(in_str):
                    return True
            return False

    @staticmethod
    def exclude_filt(path="", exclude_list=src.defaultvalues.EXLUDE_LIST):
        for ex_str in exclude_list:
            if ex_str in path:
                return False
        return True

    def filt(self, path="", include_list=src.defaultvalues.INCLUDE_LIST, exclude_list=src.defaultvalues.EXLUDE_LIST):
        if self.include_filt(path, include_list) and self.exclude_filt(path, exclude_list):
            return True
        return False

