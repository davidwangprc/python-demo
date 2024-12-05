import json
import pandas as pd

def organize_data(json_path):
    # 读取JSON文件
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 创建一个字典来存储课程目标的统计信息
    summary = {}

    for item in data:
        course_goal = item['课程目标']
        question_number = item['题号']
        question_type = item['题型']
        score = int(item['题目分数'].replace('分', ''))  # 去掉“分”字并转换为整数

        if course_goal not in summary:
            summary[course_goal] = {
                '题号': [],
                '题型': set(),  # 使用集合来存储题型以去重
                '题目数': 0,
                '总分值': 0
            }

        summary[course_goal]['题号'].append(question_number)
        summary[course_goal]['题型'].add(question_type)  # 添加题型到集合中
        summary[course_goal]['题目数'] += 1
        summary[course_goal]['总分值'] += score

    # 转换为DataFrame以便于输出
    result = []
    for goal, info in summary.items():
        result.append({
            '课程目标': goal,
            '题号': ', '.join(map(str, info['题号'])),
            '题型': ', '.join(info['题型']),  # 将集合转换为字符串
            '题目数': info['题目数'],
            '总分值': info['总分值']
        })

    df = pd.DataFrame(result)
    print(df)
    
    # 输出为JSON格式
    output_json_path = 'data/organized_2023-2024-1_data.json'
    df.to_json(output_json_path, orient='records', force_ascii=False, indent=2)
    print(f"结果已保存至: {output_json_path}")
    
    # 输出为CSV格式
    output_csv_path = 'data/organized_2023-2024-1_data.csv'
    df.to_csv(output_csv_path, index=False, encoding='utf-8-sig')
    print(f"结果已保存至: {output_csv_path}")

if __name__ == "__main__":
    json_path = 'data/2023-2024-1题型分布.json'
    organize_data(json_path)