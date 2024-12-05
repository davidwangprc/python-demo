from docxtpl import DocxTemplate
import pandas as pd
import streamlit as st

doc = DocxTemplate('./template/旧版教案首页模板.docx')
source_db = pd.read_csv('.\data\教案数据汇总.csv')
df = pd.DataFrame(source_db)
st.dataframe(df)
st.write(len(df))
select_index = st.selectbox("选择章节", df["chapter"])

columns_list = ["chapter", "section1", "section2", "section3", "section4", "section5", "教学目标", "教学重点", "教学难点", "导入","授课内容", "课程目标", "思考题", "教学反思"]
columns_list

if st.button("生成Word"):
    for i in range(len(df)):
        context = {
            "章节": df.loc[i,columns_list[0]],
            "教学目标": df.loc[i,columns_list[6]],
            "第一节": df.loc[i,columns_list[1]],
            "第二节": df.loc[i,columns_list[2]],
            "第三节": df.loc[i,columns_list[3]],
            "第四节": df.loc[i,columns_list[4]],
            "第五节": df.loc[i,columns_list[5]],
            "重点": df.loc[i,columns_list[7]],
            "难点": df.loc[i,columns_list[8]],
            "大纲": df.loc[i,columns_list[10]],
            "思考题":df.loc[i,columns_list[12]],
            "导入": df.loc[i,columns_list[9]],
            "课程目标": df.loc[i,columns_list[11]]
        }
        doc.render(context) # 渲染模板
        doc.save('out-01/新版教案-第{0}讲.docx'.format(i+1)) # 保存文件

        st.success('生成Word完成!')


