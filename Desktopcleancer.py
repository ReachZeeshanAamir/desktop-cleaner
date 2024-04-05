import os
import shutil

def create_subfolder_if_exists(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.mkdir(subfolder_path)
    return subfolder_path


def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            fileextension = filename.split('.')[-1].lower()
            if fileextension:
                subfolder_name =  f"{fileextension.upper()} Files"
                subfolder_path = create_subfolder_if_exists(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                shutil.move(file_path, subfolder_path)





if __name__ == "__main__":
    print("Desktop Cleaner Script")

    folder_path = input('Enter file location(must have double \\\\ eg: C:\\\\): \n')
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning complete.")
    else:
        print("Invalid folder path.\nPlease ensure the path is correct and try again.")
