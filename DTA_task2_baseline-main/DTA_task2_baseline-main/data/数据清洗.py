import json
import jieba
import re

def dict_change(dic):
    result={}
    dialogues_list=[]
    # print(dic["dialogues"])
    for i in dic["dialogues"]:
        dialogues_dic={}
        text = re.sub('[。，！？”“；：‘‘]', '', i["text"])#去除句子中的各个标点。
        dialogues_dic["content"]=list(text)#将句子转化为字粒度

        dialogues_dic["word"]=jieba.lcut(text)#将句子转化为词粒度
        if i["role_type"]=='user':
            dialogues_dic["type"]="客户"
        else:
            dialogues_dic["type"]="客服"
        dialogues_list.append(dialogues_dic)
    result["session"]=dialogues_list
    result[ "summary"]=dic["summary"]
    return result

date=r'C:\Users\子非鱼\Desktop\项目代码\DTA_task2_baseline-main\DTA_task2_baseline-main\data\DTA-conversation-summary_train.jsonl'
with open(date,'r',encoding='utf-8') as f:
    start_date_list=f.read().split('\n')#以换行符号分割
# first=start_date_list[0]
# print(first)
dealt_date=r'C:\User\子非鱼\Desktop\项目代码'
date_list=[]
for date in start_date_list:
    try:
        date_dict=json.loads(date)#从文件读出来的是字符串，转化为字典
        json_date=dict_change(date_dict)
        date_list.append(json_date)
    except:print(date)#查看是否有异常数据
num=0
str_num=0
for i in date_list:
    # print(i)
    # break
    for j in i["session"]:
        num+=1
        str_num+=len(j["content"])
print(num)
print(str_num)
# start=0
# end=int((len(date_list)/10)+1)
# print('一共有数据集',len(date_list),'条')
# for i in range(10):
#     name=str(i)
#     with open(dealt_date+'\\'+str(i)+'.json','a',encoding='utf-8') as name:#ValueError: I/O operation on closed file.
#         print('正在创建文件',dealt_date+'\\'+str(i)+'.json','提取数据集',start,'----',end)
#         json_dates = json.dumps(date_list[start:end], ensure_ascii=False)  # 不以ascii码显示
#         if i!=9:
#             start=end
#             end+=int((len(date_list)/10)+1)
#         else:
#             start=end
#             end=None
#         name.write(json_dates)


