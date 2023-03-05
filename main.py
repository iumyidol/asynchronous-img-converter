import os, pathlib, time, ray
from module import getImages, convert_parallel, filelist, imgExtList
# Calculate the chunk size based on the number of CPUs available


source_path = ""
update = ""
new_source = ""
valid_source = ""
remove_converted = ""
remove_unrelated = ""
desired_ext = ""
reset = ""

def parallelConvertion():
    print(time.process_time())

    getImages(source_path, remove_unrelated)

    num_cpus = ray.cluster_resources()['CPU']
    chunk_size = int((len(filelist) + num_cpus - 1) // num_cpus)
    # Split the input files into chunks and execute the conversion in parallel
    chunks = [filelist[i:i + chunk_size] for i in range(0, len(filelist), chunk_size)]
    ray.get([convert_parallel.remote(chunk, desired_ext, remove_converted) for chunk in chunks])

    # for each in filelist:
    #     convert(each, desired_ext, remove_converted)
    print(time.process_time())


while update != "N":
    if update not in ['Y', 'N']:
        update = input("Have another directory to convert ? (Y/N)")

    while remove_unrelated not in [True, False]:
        remove_unrelated = input("Remove all un-related file ? (Y/N)")
        if remove_unrelated in ['Y', 'N']:
            remove_unrelated = True if remove_unrelated == 'Y' else False

    while remove_converted not in [True, False]:
        remove_converted = input("Remove original image file after conversion ? (Y/N)")
        if remove_converted in ['Y', 'N']:
            remove_converted = True if remove_converted == 'Y' else False

    while f'.{desired_ext}' not in imgExtList:
        desired_ext = input("Image extension you desire ? (eg: .png, .jpg, .webp)")

    if update == "Y":
        while not valid_source:
            new_source = input("Please paste the absolute path of the directory")
            valid_source = pathlib.Path(new_source).is_dir()
        print("Is valid dir")
        source_path = new_source
        try:
            parallelConvertion()
        except ValueError:
            print("Directory has no image !")
            reset = "Y"

        while reset not in ['Y', 'N']:
            reset = input("Reset Setting ?")

        if reset == "Y":
            update = "Y"
            filelist.clear()
            valid_source = ""
            remove_converted = ""
            remove_unrelated = ""
            desired_ext = ""
            new_source = ""
            reset = ""
        else:
            update = ""
            filelist.clear()
            valid_source = ""
            new_source = ""
            reset = ""


