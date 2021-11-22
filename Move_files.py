import glob, os
import shutil

source_files = 'C:/Folder/*.bat'
if not os.path.exists('C:/Test_Folder/Bat_files'):
    os.mkdir('C:/Test_Folder/Bat_files')
target_folder = 'C:/Test_folder/Bat_files'

# retrieve file list
filelist = glob.glob(source_files)

for single_file in filelist:
    # move file with full paths as shutil.move() parameters
    shutil.move(single_file, target_folder)
