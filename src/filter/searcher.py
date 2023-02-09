import os

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
    try:
        file_list.remove(abs_dir)
    except Exception as e:
        print(e)


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


def sort_list(file_list: list, key_str: str, is_reverse=False):
    key_dict = {
        "CTIME": create_time_comparator,
        "MTIME": modify_time_comparator,
        "NAME": name_comparator,
        "PATH": path_comparator,
        "SIZE": size_comparator
    }
    file_list.sort(key=key_dict[key_str], reverse=is_reverse)
