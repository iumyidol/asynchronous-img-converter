import os
from module import toWebp

# Configuration, set the source dir && to remove unrelated files (not .webp) or not
# sourcedir is passed such that all directories inside will trigger the function - toWebp
# Usage: pass a sourcedir where all folder inside contains images (.png .jpg)
sourcedir = r"C:\Users\hugong\Desktop\sample-image"
removeUnrelated = True

dirs = os.listdir(sourcedir)

for each in dirs:
    path = rf'{sourcedir}\{each}'
    is_dir = os.path.isdir(path)
    if is_dir:
        toWebp(path, removeUnrelated=removeUnrelated)

# toWebp(path, removeUnrelated=removeUnrelated)
