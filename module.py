import os, shutil
from PIL import Image

# Accept the direct parent directory of the images
def toWebp(path, **kwargs):
    files = os.listdir(path)
    images = [file for file in files if file.endswith((('jpg', 'png')))]
    to_remove = kwargs.get('removeUnrelated', False)

    # Convert every image (.png, .jpg) to webp format
    for each in images:
        filename = each.split(".")[0]
        img = Image.open(rf'{path}\{each}')
        img.save(rf'{path}\{filename}.webp', 'webp')
        print(f'{path}/{each.split(".")[0]}', "Success")


    # After conversion, remove all unrelated (not .webp) files
    if to_remove:
        unrelated = [file for file in files if not file.endswith('webp')]

        for each in unrelated:
            unrelatedpath = rf'{path}\{each}'
            print(unrelatedpath, "Deleted")

            if os.path.isdir(unrelatedpath):
                shutil.rmtree(unrelatedpath)
            elif os.path.isfile(unrelatedpath):
                os.remove(unrelatedpath)
            else:
                raise Exception("Invalid path specified")
