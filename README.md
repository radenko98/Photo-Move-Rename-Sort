Hello! 

This repository has 3 python scripts. 

***First python script is file_mover.py***, asks end-user to select source and destination folders. It then moves all files from the selected source folder and its subfolders to the chosen destination folder.


***Second python script is renaming_files.py***, provides functionality to rename files within a selected folder. It includes two options for renaming:

Rename by Creation Datetime: Renames files based on their creation datetime. Files are renamed using a format of "YYYYMMDD_HHMMSS" followed by the original file extension. If multiple files have the same creation datetime, a counter is added to the filename to avoid duplicates.

Rename by Date Taken from Metadata: Attempts to extract the date taken from image files' metadata. If successful, it renames the files using the extracted date and time in the format "YYYYMMDD_HHMMSS" followed by the original file extension. If metadata extraction fails or if the file is not an image, it falls back to renaming by creation datetime.

***Third python script photo_sorter.py***, organizes photos within a chosen folder based on their date taken metadata. It creates year and month subfolders for each photo's date taken and moves the photos accordingly. 

***Easy way to run***

I've converted these scripts into EXE files for your convenience. Simply run the EXE files and follow the instructions. Unfortunately, I couldn't upload them to GitHub due to the 25MB limit, as the EXE files are around 50-60MB. You can download the files from the following link: https://drive.google.com/drive/folders/1FDDpCKrTq-wWm9KTNNYeifsRooe7gJ83?usp=sharing. 
After downloading, extract the files from the archive using the password "windows" and proceed to run them.


![exe](https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/39eb81ec-4931-4dda-bdce-bd54d3192427)


***Harder way to to RUN*** LOL


To run the provided Python scripts, you can follow these general steps:

***1. Install Python:***
If you haven't installed Python on your system, you can download and install it from the official Python website: https://www.python.org/downloads/.

***2. Create Backup:***
Before running any scripts that modify or move files, it's a good practice to create a backup of the relevant folders to avoid accidental data loss.

***3. Run Scripts:***
Open a command prompt in the folder that contains the scripts that you want to run, like this: 

<img width="626" alt="1" src="https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/40819b39-9779-42c4-8429-b9edb7e7945b">

***4.Path*** - 
Delete the path in the file explorer and type CMD

<img width="564" alt="2" src="https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/b2404765-7d47-49a7-aadf-6a9792a1c69d">

***5. Running the script*** - Type the command "python file_mover.py" and press enter

<img width="712" alt="3" src="https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/49f739c2-f830-498c-9a3c-daa2a5880ed1">




Alternatively, if you are using Python 3, replace python with python3 in the commands
Check the output of each script in the console to ensure there are no errors and to see the progress or any messages printed by the scripts.




***More information on how the scripts work***

***File_mover.py script will ask you to select source and destination folder like this.***

Select source folder:

<img width="761" alt="4" src="https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/ea7ccf63-3ff4-45fd-99ac-16bbb2d215ef">

Select the destination folder:

<img width="729" alt="5" src="https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/af5954e1-1f15-4759-8f11-0d7561e08cde">


***Renaming_files.py script will ask you to select the folder that contains the files you want renamed.***
After you select the folder, you will be asked to choose between renaming folder according to their Creation Datetime or their Date Taken value from Metadata. If you are renaming photos and videos, choose renaming files according to Date Taken value from Metadata. Like this:

<img width="260" alt="7" src="https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/983b15db-44e2-48ff-8051-fff7fcf77fd4">


***The "Photo_sorter.py" script prompts users to select a folder containing files to be organized based on their date take values, as recorded in metadata.***

<img width="752" alt="6" src="https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/6f0dbcf0-b40b-4a2f-ae46-22ce40e06ed6">




***In the end you will get a folder like this:***


![Example](https://github.com/radenko98/Photo-Move-Rename-Sort/assets/22021972/d6eeb744-0c3b-4478-998f-fa09211d8f43)





