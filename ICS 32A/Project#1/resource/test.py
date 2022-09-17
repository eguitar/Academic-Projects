import os
import shutil
from pathlib import Path



def read_directory(dir_path: Path) -> [Path]:
    '''
    Given a Path object, returns a list of
    Path objects with files only in that
    directory (not its subdirectories)
    '''
    path_list = []
    for path in dir_path.iterdir():
        if path.is_file():
            path_list.append(path)
    path_list = lex_sorted(path_list)
    
    return path_list

def read_recursive(dir_path: Path) -> [Path]:
    '''
    Given a Path object, returns a list of
    Path objects with files in the directory
    and all of its subdirectories
    '''
    path_list = []
    dir_list = []
    
    for path in dir_path.iterdir():
        if path.is_file():
            path_list.append(path)
        elif path.is_dir():
            dir_list.append(path)

    path_list = lex_sorted(path_list)
    dir_list = lex_sorted(dir_list)

            
    for path in dir_list:
        path_list.extend(read_recursive(path))

        
    return path_list



def lex_sorted(path_list: [Path]) -> [Path]:
    '''
    Given a list of paths, prints the paths
    in lexicographical order
    '''
    ordered_list = []
    new_path_list = []
    for path in path_list:
        ordered_list.append(str(path))
    ordered_list.sort()
    for path in ordered_list:
        new_path_list.append(Path(path))
        
    return new_path_list


