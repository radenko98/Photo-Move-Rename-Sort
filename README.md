Hello! 

This repository has 3 python scripts. 

***First python script is file_mover.py***, asks end-user to select source and destination folders. It then moves all files from the selected source folder and its subfolders to the chosen destination folder.

***Second python script is renaming_files.py***, provides functionality to rename files within a selected folder. It includes two options for renaming:

Rename by Creation Datetime: Renames files based on their creation datetime. Files are renamed using a format of "YYYYMMDD_HHMMSS" followed by the original file extension. If multiple files have the same creation datetime, a counter is added to the filename to avoid duplicates.

Rename by Date Taken from Metadata: Attempts to extract the date taken from image files' metadata. If successful, it renames the files using the extracted date and time in the format "YYYYMMDD_HHMMSS" followed by the original file extension. If metadata extraction fails or if the file is not an image, it falls back to renaming by creation datetime.

***Third python script photo_sorter.py***, organizes photos within a chosen folder based on their date taken metadata. It creates year and month subfolders for each photo's date taken and moves the photos accordingly. 



***HOW TO RUN***


To run the provided Python scripts, you can follow these general steps:

Install Python:
If you haven't installed Python on your system, you can download and install it from the official Python website: https://www.python.org/downloads/.

Create Backup:
Before running any scripts that modify or move files, it's a good practice to create a backup of the relevant folders to avoid accidental data loss.

Run Scripts:
Open a command prompt or terminal window.
Navigate to the directory where the scripts are located using the cd command. For example:

***cd path\to\script\directory***

Run each script separately using the python command. For example:

*python file_mover.py*

**THEN**

*python renaming_files.py*

**THEN** 

*python Photo_sorter.py*

Alternatively, if you are using Python 3, replace python with python3 in the commands.
Check the output of each script in the console to ensure there are no errors and to see the progress or any messages printed by the scripts.

![Example](https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/d6eeb744-0c3b-4478-998f-fa09211d8f43)





