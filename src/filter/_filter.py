import src.defaultvalues


def filt_list(file_list: list, include_list: list, exclude_list: list):
    for file in file_list:
        is_reserve = True
        for exclude in exclude_list:
            if exclude in file:
                is_reserve = False
                break
        if not is_reserve:
            list.remove(file)
            continue

        if include_list:
            is_reserve = False
            for include in include_list:
                if file.endswith(include):
                    is_reserve = True
                    break
            if not is_reserve:
                list.remove(file)
                continue


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
