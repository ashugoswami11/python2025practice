import os
import shutil

#source folder
SOURCE_FOLDER = "input_files"

#destination folder
DESTINATION_FOLDER = "mock_s3_bucket"

#creating s3 bucket folder if not exists
if not os.path.exists(DESTINATION_FOLDER):
    os.mkdir(DESTINATION_FOLDER)
    

#upload files
for file_name in os.listdir(SOURCE_FOLDER):
    source_path = os.path.join(SOURCE_FOLDER, file_name)
    destination_path = os.path.join(DESTINATION_FOLDER, file_name)
    
    shutil.copy(source_path, destination_path)
    print(f"uploaded {file_name} to s3 bucket")
        