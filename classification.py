import os
import shutil

def copy_folder_without_mask_files(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    for root, dirs, files in os.walk(src):
        # Create corresponding directories in the destination
        for dir in dirs:
            os.makedirs(os.path.join(dst, os.path.relpath(os.path.join(root, dir), src)), exist_ok=True)
        
        for file in files:
            if not file.endswith('_mask.png') and not file.endswith('_mask_1.png') and not file.endswith('_mask_2.png'):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst, os.path.relpath(src_file, src))
                shutil.copy2(src_file, dst_file)

# Define source and destination directories
src_dir = 'DATA/raw'
dst_dir = 'DATA/classification'

# Call the function to copy the folder
copy_folder_without_mask_files(src_dir, dst_dir)

print(f"Folder copied from {src_dir} to {dst_dir} without '_mask.png' files.")