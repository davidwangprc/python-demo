import csv
import json
import tkinter as tk
from tkinter import filedialog

def convert_csv_to_json():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 打开文件选择对话框来选择 CSV 文件
    csv_file_path = filedialog.askopenfilename(title='选择你要转换的CSV文件', filetypes=[('CSV Files', '*.csv')])
    
    # 打开文件选择对话框来选择存储 JSON 文件的位置和名称
    json_file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[('JSON Files', '*.json')])

    try:
        # 读取 CSV 文件数据 
        with open(csv_file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)   # 使用 DictReader，这将每行数据读取为一个字典
            data_list = list(reader)  # 转换为列表

        # 将数据写入 JSON 文件
        with open(json_file_path, 'w') as json_file:
            json.dump(data_list, json_file, indent=4)  # 使用indent参数来美化输出的json文件
        
        print('转换成功！')

    except Exception as e:
        print(f'转换过程中发生错误: {e}')

# 调用函数
convert_csv_to_json()