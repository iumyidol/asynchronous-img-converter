import os, ray, pathlib
from PIL import Image

filelist = []
imgExtList = [".png", ".jpeg", ".webp", ".jpg"]

# function for getting all images in the directory
def getImages(dir, remove):

    for each in pathlib.Path(dir).iterdir():
        if each.is_dir():
            # call itself
            getImages(each, remove)
        else:
            # call convert if is type of img
            if len(each.suffixes) > 0 and each.suffixes[-1] in imgExtList:
                # print(each.stem)
                # print(dir)
                filelist.append(each)
            elif remove:
                each.unlink()


# function for converting a single image
def convert(path, ext, remove):
    oriExt = path.suffixes[-1]
    oriName = path.stem
    writeTodir = path.resolve().parent

    if ext == oriExt.strip("."):
        print(f"Skipped--{oriName}{oriExt}")
        return

    im = Image.open(path)
    out_filename = f'{oriName}.{ext}'
    print(rf'{writeTodir}\{out_filename} ext = {ext}')
    # im = im.convert("L")
    im.save(rf'{writeTodir}\{out_filename}', ext=ext if ext != "jpg" else "jpeg")
    if remove:
        path.unlink()

# asynchronous function
@ray.remote
def convert_parallel(paths, ext, remove):
    for path in paths:
        convert(path, ext, remove)
