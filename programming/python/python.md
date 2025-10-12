<<<<<<< HEAD
# data型
- bool
# 書式code
- strfftime 
=======
# useful template
## import anything from parent dir
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
>>>>>>> c52adb2fba94a91752c12fb86426c243eb8f3720
# with & context manager
## context manegerあり
    with ContextManeger() as file:
        ...
## context mangerなし
    file = ContextManager()
    try:
        ...
    finally:
        file.close()