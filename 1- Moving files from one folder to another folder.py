import os
import shutil

def move_files_to_destination(src_folder, dest_folder):
    # Ensure the destination folder exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Iterate through all files in the source folder and its subfolders
    for root, dirs, files in os.walk(src_folder):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Move the file to the destination folder
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(file_path, dest_path)
            print(f"Moved {filename} to {dest_folder}")

if __name__ == "__main__":
    source_folder = r'E:\Photos'    #Change path
    destination_folder = r'E:\files'  #Change path
    move_files_to_destination(source_folder, destination_folder)
