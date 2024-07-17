import os as o


o.chdir("New folder/")
files_in_the_folder = o.listdir()


def clear_the_clutter(file_type):
    file_cat = []
    for i in range(len(files_in_the_folder)):
        if files_in_the_folder[i].endswith(f".{file_type}"):
            file_cat.append(files_in_the_folder[i])
            if i == (len(files_in_the_folder)-1):
                for j in range(len(file_cat)):
                    o.rename(file_cat[j], f"{j+1}.{file_type}")

    return 'everything is done perfectly'


file_types = input("Enter the file type you want to clear the clutter:")
print(clear_the_clutter(file_types))
print(o.listdir())
