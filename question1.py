'''
 每个enrollment_id  事件总数
'''
import pandas as pd
#导入数据
df=pd.read_csv('log_train.csv',dtype={'time': str},nrows=1000)
#将1000行的记录保存为csv格式文件
# df.to_csv('log_data.csv')
group1 = df.groupby('enrollment_id')
#按照enrollment_id来统计分组数量
d = group1.size()
print(d)
print(d*2)#有两列活动，所以就*2