import os
from datetime import datetime

def rename_files_by_creation_datetime(folder_path):
    total_renamed = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the item is a file
        if os.path.isfile(file_path):
            creation_time = os.path.getctime(file_path)
            creation_datetime = datetime.fromtimestamp(creation_time).strftime('%Y%m%d_%H%M%S')

            # Form the new filename using the creation date and time
            new_filename = f"{creation_datetime}{os.path.splitext(filename)[1]}"

            # Handle duplicate names
            counter = 1
            while os.path.exists(os.path.join(folder_path, new_filename)):
                new_filename = f"{creation_datetime}_{counter}{os.path.splitext(filename)[1]}"
                counter += 1

            # Rename the file
            os.rename(file_path, os.path.join(folder_path, new_filename))
            total_renamed += 1

    print(f"Total files renamed: {total_renamed}")

if __name__ == "__main__":
    folder_path = r'E:\Photos' #Change Path
    rename_files_by_creation_datetime(folder_path)
