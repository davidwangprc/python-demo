import pandas as pd
import json
from docx import Document
import os

def excel_to_json(excel_path, json_path):
    try:
        # 读取Excel文件
        df = pd.read_excel(excel_path)
        
        # 将DataFrame转换为字典列表
        result = []
        for _, row in df.iterrows():
            item = {
                "题号": row["题号"],
                "题干": row["题干"],
                "题型": row["题型"],
                "难易度": row["难易度"],
                "知识点": row["知识点"],
                "正确率": row["正确率"],
                "题目分数": row["题目分数"],
                "课程目标": row["课程目标"]
            }
            result.append(item)
            
        # 写入JSON文件
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
            
        print(f"转换成功！JSON文件已保存至: {json_path}")
        
    except Exception as e:
        print(f"转换过程中出现错误: {str(e)}")
        

        
        
def main():
    # 文件路径
    input_excel = 'data/2023-2024-2题型分布.xlsx'
    temp_json = 'data/2023-2024-2题型分布.json'

    
    # 首先转换Excel到JSON
    excel_to_json(input_excel, temp_json)
    

if __name__ == "__main__":
    main()