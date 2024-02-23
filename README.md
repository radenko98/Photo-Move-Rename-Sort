Let's go through the sequence of execution for the provided Python scripts:

**1st Script - Move Files Script:**

The first script (move_files_to_destination) moves all files from source folder and its subfolders to a single folder. It iterates through all files in the source folder and its subfolders using os.walk and moves each file to the destination folder using shutil.move.
After execution, all files from source folder(E:\Photos) and its subfolders are moved to a single folder (E:\files).

**2nd Script - Rename Files Script:   !!!!Choose which script do you want to run, you have 2 options!!!!**  

**Option 1: Renaming files according to creation date**
This script (rename_files_by_creation_datetime) renames all files in E:\Photos based on their creation date and time. It iterates through each file, retrieves its creation time, and renames the file using a format like 'YYYYMMDD_HHMMSS'.
Duplicate names are handled by appending a counter to the filename if needed. After execution, all files in E:\Photos are renamed based on their creation date and time.

**Option 2: Renaming files according to date taken**
This script includes the get_date_taken function to extract the date taken from image metadata using the Pillow library. The rename_files_by_date_taken function then renames files based on this date taken information.

**3rd Script - Organize Files Script:   !!!!Choose which script do you want to run, you have 2 options!!!!**  

**Option 1: Photo sorter by month and year according to modification date**

This script script (organize_photos_by_year_month) organizes files in E:\files based on their modified date. It creates folders for each year and month and moves the corresponding files into these folders.
It iterates through each file in E:\files, retrieves its modification time, creates a destination folder based on the year and month, and moves the file to the destination folder.
After execution, files in E:\files are organized into folders based on their modification date.

**Option 2: Photo sorter by month and year according to date taken**

This Script uses the Pillow library to extract the date taken from image metadata and then organizes the photos into subfolders based on that date. The get_date_taken function attempts to extract the date taken from the image metadata, and the organize_photos_by_date_taken function then uses this information to move the files to the appropriate subfolders. If the date taken information is not available for a file, it will be skipped and a message will be printed.




In summary:

Initially, all files from E:\Photos are moved to E:\files.
Then, the files in E:\Photos are renamed based on their creation date and time.
Finally, the files in E:\files are organized into folders based on their modification date.

Note: It's important to understand the interactions between these scripts and the content of the folders you are working with. Depending on the number of files and the specific timestamps, there might be overwriting or duplication issues, especially if there are files with the same timestamps in the source and destination folders.** Always ensure you have backups before running scripts that modify or move files.**




***HOW TO RUN***


To run the provided Python scripts, you can follow these general steps:

Install Python:
If you haven't installed Python on your system, you can download and install it from the official Python website: https://www.python.org/downloads/.

Create Backup:
Before running any scripts that modify or move files, it's a good practice to create a backup of the relevant folders to avoid accidental data loss.


***Edit Script Paths: Open each script in a text editor and make sure to update the folder paths in the scripts to point to the correct directories on your system.***
![Screenshot 2024-01-26 014330](https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/2cffe302-103c-4939-b6d5-35c24c33d94a)



Run Scripts:
Open a command prompt or terminal window.
Navigate to the directory where the scripts are located using the cd command. For example:
***cd path\to\script\directory***

Run each script separately using the python command. For example:
*python move_files_script.py*
**THEN**
*python rename_files_script.py*
**THEN** 
*python organize_files_script.py*

Alternatively, if you are using Python 3, replace python with python3 in the commands.
Check the output of each script in the console to ensure there are no errors and to see the progress or any messages printed by the scripts.

***Remember to customize the scripts based on your specific use case, and always exercise caution when running scripts that modify or move files. Ensure you have backups in case anything goes wrong.***

![Example](https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/d6eeb744-0c3b-4478-998f-fa09211d8f43)





