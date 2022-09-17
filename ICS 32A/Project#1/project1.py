# Eric Trinh / 20091235 / Project#

import os
import shutil
from pathlib import Path


def run_retrieval():
    '''
    A program that prompts user to input a path
    to a directory, specify which files are
    interesting, and specify which actions to
    take on those files
    '''
    while True:
        try:
            user_in = input()
            file_path = Path(user_in[2:])
            path_list1 = []
            if user_in[0:2] == 'D ':
                path_list1 = _read_directory(file_path)
                break
            elif user_in[0:2] == 'R ':
                path_list1 = _read_recursive(file_path)
                break
            else:
                raise ValueError
        except:
            print('ERROR')

    for path in path_list1:
        print(path)

    while True:
        try:
            user_in = input()
            path_list2 = []
            if user_in == 'A':
                path_list2 = path_list1
                break
            elif user_in[0:2] == 'N ':
                path_list2 = _search_name(path_list1,user_in[2:])
                break
            elif user_in[0:2] == 'E ':
                path_list2 = _search_ext(path_list1,user_in[2:])
                break
            elif user_in[0:2] == 'T ':
                path_list2 = _search_text(path_list1,user_in[2:])
                break
            elif user_in[0:2] == '< ':
                path_list2 = _search_less(path_list1,int(user_in[2:]))
                break
            elif user_in[0:2] == '> ':
                path_list2 = _search_more(path_list1,int(user_in[2:]))
                break
            else:
                raise ValueError
        except:
            print('ERROR')
    
    if path_list2 != []:
        for path in path_list2:
            print(path)
    else:
        return None

    while True:
        try:
            user_in = input()
            if user_in == 'F':
                _print_line1(path_list2)
                break
            elif user_in == 'D':
                _duplicate_file(path_list2)
                break
            elif user_in == 'T':
                _touch_file(path_list2)
                break
            else:
                raise ValueError
        except:
            print('ERROR')


def _read_directory(dir_path: Path) -> [Path]:
    '''
    Given a Path object, returns a sorted
    list of Path objects with files only in
    that directory (not its subdirectories)
    '''
    path_list = []
    for path in dir_path.iterdir():
        try:
            if path.is_file():
                path_list.append(path)
        except:
            pass
    path_list = _lex_sorted(path_list)
    
    return path_list

def _read_recursive(dir_path: Path) -> [Path]:
    '''
    Given a Path object, returns a sorted
    list of Path objects with files in the
    directory and all of its subdirectories
    '''
    path_list = []
    dir_list = []
    
    for path in dir_path.iterdir():
        try:
            if path.is_file():
                path_list.append(path)
            elif path.is_dir():
                dir_list.append(path)
        except:
            pass

    path_list = _lex_sorted(path_list)
    dir_list = _lex_sorted(dir_list)

            
    for path in dir_list:
        try:
            path_list.extend(_read_recursive(path))
        except:
            pass
        
    return path_list



def _lex_sorted(path_list: [Path]) -> [Path]:
    '''
    Given a list of paths, sorts and returns
    the paths in lexicographical order
    '''
    ordered_list = []
    new_path_list = []
    for path in path_list:
        ordered_list.append(str(path))
    ordered_list.sort()
    for path in ordered_list:
        new_path_list.append(Path(path))
        
    return new_path_list


def _search_name(path_list: [Path], name: str) -> [Path]:
    '''
    Given a list of Path objects and a name,
    returns a list of Path objects with files that
    have the corresponding name
    '''
    new_path_list = []
    for path in path_list:
        if os.path.basename(path) == name:
            new_path_list.append(path)

    return new_path_list


def _search_ext(path_list: [Path], ext: str) -> [Path]:
    '''
    Given a list of Path objects and an extension,
    returns a list of Path objects with files that
    have the corresponding extension
    '''
    if ext[0] != '.':
        ext = '.' + ext
    new_path_list = []
    for path in path_list:
        if os.path.splitext(path)[1] == ext:
            new_path_list.append(path)

    return new_path_list


def _search_text(path_list: [Path], text: str) -> [Path]:
    '''
    Given a list of Path objects and a text,
    returns a list of Path objects with files
    that contain the corresponding text
    '''
    new_path_list = []
    for path in path_list:
        try:
            file = path.open('r')
            line_list = file.readlines()
            for line in line_list:
                if text in line:
                    new_path_list.append(path)
                    break
        except:
            pass
        finally:
            file.close()

    return new_path_list


def _search_less(path_list: [Path], max: int) -> [Path]:
    '''
    Given a list of Path objects and a positive
    integer, returns a list of Path objects with
    files that have a size smaller than 'max' bytes
    '''
    new_path_list = []
    for path in path_list:
        if os.path.getsize(path) < max:
            new_path_list.append(path)

    return new_path_list


def _search_more(path_list: [Path], min: int) -> [Path]:
    '''
    Given a list of Path objects and a positive
    integer, returns a list of Path objects with
    files that have a size greater than 'min' bytes
    '''
    new_path_list = []
    for path in path_list:
        if os.path.getsize(path) > min:
            new_path_list.append(path)

    return new_path_list


def _print_line1(path_list: [Path]):
    '''
    Given a list of Path objects,
    print the first line of readable
    text file, if not prints 'NOT TEXT'
    '''
    for path in path_list:
        try:
            print(path.open('r').readline(), end = '')
        except:
            print('NOT TEXT')
            

def _duplicate_file(path_list: [Path]):
    '''
    Given a list of Path objects,
    duplicate each file in the same
    directory with an additional
    extension of '.dup'
    '''
    for path in path_list:
        try:
            shutil.copy(path,Path(str(path) + '.dup'))
        except:
            pass


def _touch_file(path_list: [Path]):
    '''
    Given a list of Path objects,
    touch each file
    '''
    for path in path_list:
        try:
            os.utime(path)
        except:
            pass


if __name__ == '__main__':
    run_retrieval()
