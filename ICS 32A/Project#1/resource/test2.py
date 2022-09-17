# Eric Trinh / 20091235 / Project#


import os
import shutil
from pathlib import Path

p1 = Path(r'E:\UCI\ICS32A\Exercise_Set#1\make_set1_submission.py')
p2 = Path(r'E:\UCI\ICS32A\Exercise_Set#1\problem1.pdf')
p3 = Path(r'E:\UCI\ICS32A\Exercise_Set#1\problem2.py')
p4 = Path(r'E:\UCI\ICS32A\Exercise_Set#1\problem3.pdf')
p5 = Path(r'E:\UCI\ICS32A\Exercise_Set#1\problem4.pdf')
p6 = Path(r'E:\UCI\ICS32A\Exercise_Set#1\problem5.py')

p = [p1,p2,p3,p4,p5,p6]

def search_text(path_list: [Path], text: str) -> [Path]:
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

def search(path: Path, text: str) -> bool:
    test = False
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

    return test

search_text(p, 'path')
