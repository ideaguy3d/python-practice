folders = [
    {'homework': [
        {'project1': ['file1.txt', 'file2.txt']},
        {'project2': ['file3.txt']},
        ['hw1.txt']
    ]},
    {'pictures': ['description.txt']},
    {'music': ['favs.txt']},
    ['welcome.txt', 'README.txt']
]

is_root = True


def count_txt(dir) -> int:
    global is_root
    if isinstance(dir, list) and not is_root:
        return 0
    if is_root:
        is_root = False
    files = [f for f in dir if isinstance(f, list)][0]
    count = 0
    for file in files:
        if 'txt' in file:
            count += 1
    for subdir in dir:
        count += count_txt(subdir)
    return count


txt_count = count_txt(folders)
debug = 1

# end of file
