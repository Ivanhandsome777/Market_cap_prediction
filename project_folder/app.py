from flask import Flask, render_template, request, redirect, url_for
import io
import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端
import matplotlib.pyplot as plt
import base64
from functions import *
from openai import OpenAI





app = Flask(__name__)

@app.route('/')
def choose_language():
    return render_template('language_yjl.html')

@app.route('/zh',methods=["POST","GET"]) #简体中文
def zh_index():
# '''
#     client = OpenAI()



#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": "tell me a joke"
#             }
#         ]
#     )

# '''



    generated_text = "暂停使用gpt"


    return render_template('ch_index.html',text=generated_text)



@app.route('/en',methods=["POST","GET"]) #English
def en_index():
# '''
#     client = OpenAI()



#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": "tell me a joke"
#             }
#         ]
#     )

# '''
    generated_text = "暂停使用gpt"


    return render_template('en_index.html',text=generated_text)




@app.route('/zh/company', methods=['POST'])
def company():
    try:

        company_name = request.form['company_name']
        function_num = int(request.form['function_num'])
        
        # 根据不同的功能号调用相应函数并返回结果
        if function_num == 1:
            result_data = company_profile(company_name)
            key_mapping = {
                "Short Name": "简称",
                "Long Name": "全称",
                "Country": "国家",
                "Website": "官网",
                "Industry": "行业",
                "Sector": "部门",
                "Business Summary": "业务概要",
                "Full-time Employees": "全职员工",
                "Market Cap": "市值",
                "Volume": "交易量",
                "Previous Close": "前收盘价",
                "Current Price": "当前价格",
                "Open": "开盘价",
                "Day Low": "最低价",
                "Day High": "最高价",
                "Error": "错误信息"
            }         
            result_data = dict(map(lambda item: (key_mapping.get(item[0], item[0]), item[1]), result_data.items()))
            result_type = 'simple'  # 简单字典
            
        elif function_num == 2:
            result_data = get_financial_numbers(company_name)
            result_type = 'nested'  # 嵌套字典
            
        elif function_num == 3:
            statement_choice = int(request.form['statement_choice'])
            result_data = get_financial_statements(company_name, statement_choice)
            result_type = 'html_table'  # HTML 表格

        elif function_num == 4:
            buffer = plot_income_data_web(company_name)
            img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

            # Pass the base64 string to the template
            return render_template('plot.html', image_data=img_base64,company_name=company_name)
        

        else:
            return "无效的功能编号"
        
        return render_template('ch_result.html', company=company_name, result_data=result_data, result_type=result_type)

    except Exception as e:
        return render_template('error.html', error_message=str(e))
    

# 英文
# @app.route('/zh/company', methods=['POST'])
# def company():
#     try:

#         company_name = request.form['company_name']
#         function_num = int(request.form['function_num'])
        
#         # 根据不同的功能号调用相应函数并返回结果
#         if function_num == 1:
#             result_data = company_profile(company_name)
#             result_type = 'simple'  # 简单字典
            
#         elif function_num == 2:
#             result_data = get_financial_numbers(company_name)
#             result_type = 'nested'  # 嵌套字典
            
#         elif function_num == 3:
#             statement_choice = int(request.form['statement_choice'])
#             result_data = get_financial_statements(company_name, statement_choice)
#             result_type = 'html_table'  # HTML 表格

#         elif function_num == 4:
#             buffer = plot_income_data_web(company_name)
#             img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

#             # Pass the base64 string to the template
#             return render_template('plot.html', image_data=img_base64,company_name=company_name)

#         else:
#             return "无效的功能编号"
        
#         return render_template('ch_result.html', company=company_name, result_data=result_data, result_type=result_type)

#     except Exception as e:
#         return render_template('error.html', error_message=str(e)


@app.route('/zh/financial_statements', methods=['GET', 'POST'])
def financial_statements():
    if request.method == 'POST':
        company_name = request.form['company_name']
        choice = int(request.form['statement_choice'])

        # 调用 get_financial_statements 函数获取相应的财务报表
        result_data = get_financial_statements(company_name, choice)

        # 将 HTML 表格数据传递给模板
        return render_template('result.html', company=company_name, result_data=result_data)

    return render_template('financial_statements.html')





if __name__ == '__main__':
    app.run(debug=True)
