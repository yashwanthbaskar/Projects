import os
import shutil
target='demo'
os.chdir(target)
folder_name=os.listdir('.')
for file in folder_name:
    try:
        Image.open(file)
    except Exception as e:
        #print(f'{e}')
        dirname='trash'
        os.makedirs(dirname,exist_ok=True)
        src=file
        dst=os.path.join(dirname,file)
        shutil.move(src,dst)
