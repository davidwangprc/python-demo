import os
import shutil

def handle_error(exc_info):
    print(f"Error encountered: {exc_info}")

def create_folders_and_move_files(source_dir):
    # 获取源目录中的所有文件和子文件夹信息
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # 分离路径到文件名的部分，提取“_”之前的部分作为文件夹名称
            name_parts = os.path.splitext(file)
            prefix = name_parts[0].split('_')[0] if '_' in name_parts[0] else name_parts[0]
            print("filename:",prefix)    
            folder_name = os.path.join(root, prefix) if prefix else os.path.dirname(root)

            # 创建目录
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            
            # 获取完整文件路径和文件名，以提取文件夹路径，并将文件移动到正确的文件夹中
            file_path = os.path.join(root, file)
            new_file_path = os.path.join(folder_name, file)

            shutil.move(file_path, new_file_path)
            print("move file:",{file},"to",{folder_name})

# 示例用法：
# source_dir = 'your_source_directory'
source_dir = "C:\\AI-TOOLS\\SD\\ComfyUI_windows_portable\\ComfyUI\\models\\checkpoints\\Pony"
create_folders_and_move_files(source_dir)